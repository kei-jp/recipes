---
name: skill-author
description: >
  AI向けSkillを新規作成・改善・分割・リファクタリングする際に利用する。
version: "1.0.0"

metadata:
  owner: keisuke
  language: ja
  category: meta
  tags:
    - skill
    - agents
    - prompt
    - authoring
---

# このスキルを利用するタイミング

以下の場合に利用する。

- 新しいSkillを作成する
- 既存Skillを改善する
- Skillを分割する
- Skillを統合する
- Skillのレビューを行う

---

# 基本方針

SkillはAIが利用するための知識モジュールである。

人間向けのドキュメントではなく、AIへの指示書として記述する。

再利用性・保守性・責務の明確化を最優先とする。

---

# Skillを新規作成する条件

以下に該当する場合は新しいSkillとして作成する。

- 独立した責務を持つ
- 他プロジェクトでも利用できる可能性がある
- 他Skillへの依存が少ない
- 単体で利用しても意味がある

---

# 既存Skillを更新する条件

以下の場合は新しいSkillを作らず既存Skillを更新する。

- 単なるルール追加
- 軽微な改善
- 誤字修正
- 例の追加
- 同一責務内の内容追加

---

# Skillを分割する条件

以下に該当する場合は分割を検討する。

- 複数の責務を持っている
- 内容が長大になっている
- 一部だけ再利用したいケースが多い
- 更新頻度が異なる内容が混在している

---

# Skill構成

基本構成は以下とする。

1. Front Matter
2. 利用タイミング
3. 基本方針
4. 詳細ルール
5. 出力方針（必要な場合）
6. サンプル（必要な場合）

---

# 配置方針

- 通常の Skill は `.skills/<skill-name>/SKILL.md` 配下に配置すること。
- 通常の Skill は単一ファイル構成にしないこと。
- 通常の Skill には必要に応じて `CHANGELOG.md`、`references/`、`assets/` を含めること。
- review-governance は `.skills/reviewer/review-governance/skill.md` に配置し、reviewer 系 Skill の共通ルールとして扱うこと。
- reviewer 系の Skill は `.skills/reviewer/<skill-name>/skill.md` 配下にまとめること。
- reviewer 系の Skill は単一ファイル構成にしないこと。
- reviewer 系の Skill には `examples.md`、`checklist.md`、`references.md` を将来追加できるようにしておくこと。
- ファイル名は責務が分かる短い名前にすること。

---

# Front Matter

必ず以下を記載する。

```yaml
---
name:
description:
version:

metadata:
  owner:
  language:
  category:
  tags:
---
```

---

# 記述ルール

命令形で記述する。

推奨例

- ～すること
- ～を利用する
- ～を優先する
- ～してはいけない

避ける表現

- ～と思われる
- ～すると良い
- ～が望ましい
- ～かもしれない

---

# 1 Skill = 1責務

一つのSkillには一つの責務のみ持たせる。

悪い例

- Python + GitHub + Docker

良い例

- Python
- GitHub Issue
- Docker Build

---

# 重複を避ける

既存Skillで表現できる内容は新規Skillを作成しない。

共通化できる場合は既存Skillを更新する。

---

# サンプル

長いサンプルコードは必要最低限とする。

サンプルはルールを理解するために必要な場合のみ記載する。

---

# 出力品質

Skillは以下を満たすこと。

- 責務が明確
- 再利用可能
- 命令が曖昧でない
- 人間が読んでも理解しやすい
- AIが解釈しやすい

---

# レビュー

Skill完成後は以下を自己確認する。

- 責務は一つか
- 重複Skillは存在しないか
- 命令が曖昧ではないか
- 将来も再利用できるか
- 名前は内容を適切に表しているか

必要であれば、既存Skillとの統合・分割も提案する。

---

# CHANGELOG

新規作成・更新・分割・統合の際は、必ず配下に `CHANGELOG.md` を残すこと。

## CHANGELOG.md の記録ルール

```text
## <YYYY-MM-DD_HHmmss> <type>: <description>
```

## 例

```CHANGELOG.md
## 2024-06-06_000000 :v1.0.0 新規作成
## 2024-06-06_000001 <feat>: v1.0.1 軽微な改善
## 2024-06-06_000002 <refactor>: v1.0.2 分割
```

## type の選択肢

| Type         | 用途                           | 例                                             |
| ------------ | ------------------------------ | ---------------------------------------------- |
| **feat**     | 新機能の追加                   | `feat: 新しいSkillを追加`                     |
| **fix**      | バグ修正                       | `fix: Skillの誤字を修正`                       |
| **refactor** | リファクタリング               | `refactor: Skillを分割`                        |
| **docs**     | ドキュメントの変更のみ         | `docs: Skillの説明を更新`                       |
| **chore**    | その他の変更                   | `chore: Skillのメタ情報を更新`                |

