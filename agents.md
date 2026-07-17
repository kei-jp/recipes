# Recipes - Agents

## Purpose

日常的に作る料理を、健康・継続性・再現性を重視して管理する。

---

## Design Principles

- 継続できることを最優先とする。
- 美味しさと健康のバランスを重視する。
- 作り置きを前提として設計する。
- 特定の商品・ブランドへの依存を避ける。
- 冷蔵庫・冷凍庫の在庫を積極的に活用する。
- 手間より効果が小さい工程は積極的に見直す。
- 一度に変更する要素は原則1つまでとし、改善点を把握しやすくする。

---

## Preferred Documentation

各レシピには以下を残す。

- 完成レシピ
- 使用した材料
- 使用したスパイス・調味料
- 所感
- 次回変更したい点

---

## Naming

レシピは料理名ではなく、用途やカテゴリを優先して分類してもよい。

例

recipes/
├── spice-curry/
├── soup/
├── side-dish/
└── dessert/

---

## Non Goals

以下は優先しない。

- 本場の完全再現
- SNS映え
- 必要以上の調理器具
- 毎回同じ味への固執

## Standard First

新しいレシピを作る前に、
標準レシピを十分に改善すること。

派生レシピは標準レシピの知見を活用して構築する。


## グローバルスキル参照
- skill 管理ルール: `./.skills/skill/skill.md`
- rfc-writer: `./.skills/governance/rfc-writer/skill.md`
- adr-writer: `./.skills/governance/adr-writer/skill.md`
- コミット ルール: `./.skills/commit/SKILL.md`
- GitHub Issue管理: `./.skills/github-issues-workflow/SKILL.md`
- GitHub Project管理: `./.skills/github-project-management/SKILL.md`
