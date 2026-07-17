# Recipes - Agents

## Purpose

日常的に作る料理について、レシピだけでなく改善の過程や知見も含めて管理する。
健康・継続性・再現性を重視し、長期的に育てられるナレッジベースを目指す。

---

## Design Principles

- 継続できることを最優先とする。
- 美味しさと健康のバランスを重視する。
- 作り置きを前提として設計する。
- 特定の商品・ブランドへの依存を避ける。
- 冷蔵庫・冷凍庫の在庫を積極的に活用する。
- 手間より効果が小さい工程は積極的に見直す。
- 一度に変更する要素は原則1つまでとし、変更の影響を評価できるようにする。

---

## Preferred Documentation

各レシピディレクトリでは、現在の標準レシピと過去の記録を管理する。

### standard.md

現在推奨するレシピを記載する。

### history/

調理した記録をスナップショットとして保存する。

各記録には可能な範囲で以下を残す。

- 調理日
- 使用した材料
- 使用したスパイス・調味料
- 所感
- 改善点
- 写真（任意）


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


## Knowledge First

レシピそのものではなく、
「なぜその構成にしたのか」
「何を試し、何が改善されたのか」
という知識を残すことを優先する。


## グローバルスキル参照
- skill 管理ルール: `./.skills/skill/skill.md`
- rfc-writer: `./.skills/governance/rfc-writer/skill.md`
- adr-writer: `./.skills/governance/adr-writer/skill.md`
- コミット ルール: `./.skills/commit/SKILL.md`
- GitHub Issue管理: `./.skills/github-issues-workflow/SKILL.md`
- GitHub Project管理: `./.skills/github-project-management/SKILL.md`
