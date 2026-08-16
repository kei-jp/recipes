import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from scripts.recipe_index import (
    README_RELATIVE_PATH,
    RECIPE_INDEX_END,
    RECIPE_INDEX_START,
    RecipeIndexError,
    check_command,
    generate_command,
    main,
    validate_repository,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


class RecipeIndexTests(unittest.TestCase):
    def _root(self) -> Path:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        skill = REPO_ROOT / ".skills/recipe-frontmatter/SKILL.md"
        (root / ".skills/recipe-frontmatter").mkdir(parents=True)
        (root / ".skills/recipe-frontmatter/SKILL.md").write_text(
            skill.read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        (root / README_RELATIVE_PATH).write_text(
            "# Human README\n\n"
            f"{RECIPE_INDEX_START}\n\n{RECIPE_INDEX_END}\n\n"
            "## Human Notes\n\nKeep this section.\n",
            encoding="utf-8",
        )
        return root

    def _write_recipe(
        self,
        root: Path,
        relative_path: str = "soup/standard.md",
        *,
        title: str = "テストスープ",
        document_type: str = "standard",
        category: str = "soup",
        status: str = "standard",
        created_at: str = "2026-08-16",
        tags: str = "  - meal-prep\n",
        optional: str = "",
        body_title: str | None = None,
    ) -> Path:
        path = root / "recipes" / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\n"
            f"title: {title}\n"
            f"document_type: {document_type}\n"
            f"category: {category}\n"
            f"status: {status}\n"
            f"created_at: {created_at}\n"
            "tags:\n"
            f"{tags}"
            f"{optional}"
            "---\n"
            f"# {body_title if body_title is not None else title}\n\n本文\n",
            encoding="utf-8",
        )
        return path

    def test_validate_accepts_valid_front_matter(self) -> None:
        root = self._root()
        self._write_recipe(root)

        documents, errors = validate_repository(root)

        self.assertEqual(len(documents), 1)
        self.assertEqual(errors, [])

    def test_validate_rejects_missing_front_matter(self) -> None:
        root = self._root()
        path = root / "recipes/soup/standard.md"
        path.parent.mkdir(parents=True)
        path.write_text("# テストスープ\n", encoding="utf-8")

        _, errors = validate_repository(root)

        self.assertTrue(any("Front Matterがありません" in error for error in errors))

    def test_validate_rejects_yaml_parse_error(self) -> None:
        root = self._root()
        path = root / "recipes/soup/standard.md"
        path.parent.mkdir(parents=True)
        path.write_text("---\ntitle: [\n---\n# テストスープ\n", encoding="utf-8")

        _, errors = validate_repository(root)

        self.assertTrue(any("YAML parse error" in error for error in errors))

    def test_validate_rejects_missing_required_field(self) -> None:
        root = self._root()
        self._write_recipe(root)
        path = root / "recipes/soup/standard.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace("status: standard\n", ""),
            encoding="utf-8",
        )

        _, errors = validate_repository(root)

        self.assertTrue(any("必須フィールド不足" in error for error in errors))

    def test_validate_rejects_enum_violation(self) -> None:
        root = self._root()
        self._write_recipe(root, category="unknown")

        _, errors = validate_repository(root)

        self.assertTrue(any("categoryが許可値ではありません" in error for error in errors))

    def test_validate_rejects_rating_out_of_range(self) -> None:
        root = self._root()
        self._write_recipe(root, optional="rating: 6\n")

        _, errors = validate_repository(root)

        self.assertTrue(any("ratingは1から5" in error for error in errors))

    def test_validate_rejects_duplicate_tags(self) -> None:
        root = self._root()
        self._write_recipe(root, tags="  - meal-prep\n  - meal-prep\n")

        _, errors = validate_repository(root)

        self.assertTrue(any("tagsに重複" in error for error in errors))

    def test_validate_rejects_missing_related_path(self) -> None:
        root = self._root()
        self._write_recipe(root, optional="related:\n  standard: recipes/soup/missing.md\n")

        _, errors = validate_repository(root)

        self.assertTrue(any("relatedの参照先がありません" in error for error in errors))

    def test_validate_rejects_standard_status_mismatch(self) -> None:
        root = self._root()
        self._write_recipe(root, status="tested")

        _, errors = validate_repository(root)

        self.assertTrue(any("document_type: standardには" in error for error in errors))

    def test_validate_rejects_history_title_with_date_prefix(self) -> None:
        root = self._root()
        self._write_recipe(
            root,
            relative_path="soup/history/2026-08-16-trial/notes.md",
            title="2026-08-16 試作スープ",
            document_type="history",
            status="tested",
            body_title="2026-08-16 試作スープ",
        )

        _, errors = validate_repository(root)

        self.assertTrue(any("historyのtitleには調理日" in error for error in errors))

    def test_generator_groups_categories_sorts_dates_and_links(self) -> None:
        root = self._root()
        self._write_recipe(root, relative_path="soup/standard.md", title="標準スープ", created_at="2026-08-01")
        self._write_recipe(
            root,
            relative_path="soup/history/2026-08-16-trial/notes.md",
            title="新しい試作",
            document_type="history",
            status="tested",
            created_at="2026-08-16",
            optional="servings: 2\nrating: 4\n",
        )
        self._write_recipe(
            root,
            relative_path="soup/history/2026-08-01-trial/notes.md",
            title="古い試作",
            document_type="history",
            status="tested",
            created_at="2026-08-01",
        )
        self._write_recipe(root, relative_path="curry/standard.md", title="標準カレー", category="curry")

        self.assertEqual(main(["validate", "--root", str(root)]), 0)
        self.assertEqual(generate_command(root), 0)
        output = (root / README_RELATIVE_PATH).read_text(encoding="utf-8")

        self.assertLess(output.index("### curry"), output.index("### soup"))
        self.assertLess(output.index("新しい試作"), output.index("古い試作"))
        self.assertIn("[open](recipes/soup/history/2026-08-16-trial/notes.md)", output)
        self.assertIn("★★★★☆ (4)", output)
        self.assertIn("|  |", output)

    def test_generator_handles_standard_and_history_without_optional_values(self) -> None:
        root = self._root()
        self._write_recipe(root, relative_path="soup/standard.md")
        self._write_recipe(
            root,
            relative_path="soup/history/2026-08-16-trial/notes.md",
            title="試作",
            document_type="history",
            status="tested",
        )

        self.assertEqual(generate_command(root), 0)
        output = (root / README_RELATIVE_PATH).read_text(encoding="utf-8")

        self.assertLess(output.index("#### 標準レシピ"), output.index("#### 履歴・試作"))
        self.assertIn("|  |  |", output)

    def test_generator_preserves_content_outside_markers(self) -> None:
        root = self._root()
        self._write_recipe(root)
        before = "# Human README\n\n説明を保持する。\n\n"
        after = "\n\n## Human Notes\n\nこの領域も保持する。\n"
        (root / README_RELATIVE_PATH).write_text(
            before + f"{RECIPE_INDEX_START}\nold\n{RECIPE_INDEX_END}" + after,
            encoding="utf-8",
        )

        self.assertEqual(generate_command(root), 0)
        output = (root / README_RELATIVE_PATH).read_text(encoding="utf-8")

        self.assertTrue(output.startswith(before))
        self.assertTrue(output.endswith(after))
        self.assertIn("## Recipe Index", output)
        self.assertNotIn("\nold\n", output)

    def test_generator_rejects_missing_markers(self) -> None:
        root = self._root()
        self._write_recipe(root)
        path = root / README_RELATIVE_PATH
        path.write_text("# Human README\n", encoding="utf-8")

        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(generate_command(root), 1)

        self.assertEqual(path.read_text(encoding="utf-8"), "# Human README\n")

    def test_generator_is_deterministic(self) -> None:
        root = self._root()
        self._write_recipe(root)

        self.assertEqual(generate_command(root), 0)
        first = (root / README_RELATIVE_PATH).read_text(encoding="utf-8")
        self.assertEqual(generate_command(root), 0)
        second = (root / README_RELATIVE_PATH).read_text(encoding="utf-8")

        self.assertEqual(first, second)

    def test_check_validates_and_detects_stale_index(self) -> None:
        root = self._root()
        self._write_recipe(root)
        self.assertEqual(generate_command(root), 0)
        self.assertEqual(check_command(root), 0)
        (root / README_RELATIVE_PATH).write_text("stale\n", encoding="utf-8")

        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(check_command(root), 1)

    def test_schema_ssot_is_required(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(RecipeIndexError):
                validate_repository(Path(directory))


if __name__ == "__main__":
    unittest.main()
