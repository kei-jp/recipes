---
name: recipe-frontmatter
description: >
  レシピリポジトリ内のMarkdownへ、検索・集計・将来のDB同期に利用できる
  YAML Front Matterを付与・更新する際に利用する。
version: "1.0.0"

metadata:
  owner: keisuke
  language: ja
  category: documentation
  tags:
    - recipe
    - frontmatter
    - yaml
    - metadata
    - search
---

# このスキルを利用するタイミング

以下の場合に利用すること。

- `recipes/` 配下のMarkdownを新規作成する
- 既存レシピへFront Matterを追加する
- レシピの分類、タグ、評価、状態を更新する
- MarkdownからインデックスやDB同期データを生成する
- レシピディレクトリを再編成する前にメタデータを整備する

`README.md`、`agents.md`、Skill、一般的な設計資料には適用しないこと。

---

# 基本方針

- Markdown本文を一次情報として維持すること。
- Front Matterは検索、一覧生成、集計、DB同期のための構造化メタデータとして扱うこと。
- 本文から確認できない値を推測して埋めてはいけない。
- 不明な任意項目は省略すること。`unknown`、空文字、空配列で埋めないこと。
- 日付は `YYYY-MM-DD` 形式を利用すること。
- キー名と列挙値は英小文字のkebab-caseを利用すること。
- 人間向けの料理名や説明は日本語で記載してよい。
- タグだけで意味を持たせず、安定した分類は専用フィールドへ記録すること。
- 同じ意味の表記揺れを増やしてはいけない。

---

# 対象ドキュメント

`document_type` は次のいずれかを利用すること。

| 値 | 対象 |
| --- | --- |
| `standard` | 現在の推奨レシピである `standard.md` |
| `history` | 調理実績・試作・失敗・救済を残す履歴 |
| `reference` | レシピ群の索引、比較、共通知識など |

`recipes/` 配下の個別レシピには原則として `standard` または `history` を利用すること。

---

# 必須フィールド

すべての対象Markdownへ、次のフィールドをこの順序で記載すること。

```yaml
---
title: ひよこ豆と鶏肉のセロリトマトスープ
document_type: history
category: soup
status: tested
created_at: 2026-08-01
tags:
  - meal-prep
  - tomato-base
---
```

## `title`

- 人間が一覧で識別できる具体的な名称を記載すること。
- ファイル名だけでは分からない主要食材や特徴を含めること。
- Markdown本文の最初の見出しと同じ名称を利用してよい。

## `document_type`

- `standard`、`history`、`reference` のいずれかを利用すること。

## `category`

料理の主分類を一つだけ記載すること。

初期の標準値は次のとおりとする。

- `curry`
- `soup`
- `noodles`
- `rice`
- `bread`
- `side-dish`
- `drink`
- `sauce`
- `spice-blend`
- `dessert`
- `other`

既存の値で表現できない分類が継続的に必要な場合のみ、このSkillを更新して追加すること。

## `status`

次のいずれかを利用すること。

| 値 | 意味 |
| --- | --- |
| `draft` | 未調理または構想段階 |
| `tested` | 一度以上調理し、実績を記録済み |
| `standard` | 現在の標準レシピ |
| `needs-improvement` | 改善が必要だと確認済み |
| `failed` | 成立しなかった試行 |
| `archived` | 現在は利用しない記録 |

- `document_type: standard` では原則として `status: standard` を利用すること。
- 調理済みの履歴は原則として `tested`、`needs-improvement`、`failed` のいずれかを利用すること。

## `created_at`

- `history` では実際の調理日を記載すること。
- `standard` では文書を新規作成した日を記載すること。
- Git履歴やディレクトリ名から明確に確認できない場合は推測せず、既存履歴を確認すること。

## `tags`

- 0個にする場合はフィールド自体を省略せず、必須項目として最低1個付与すること。
- 検索時に利用価値がある特徴だけを記載すること。
- 専用フィールドと同じ情報だけを重複して記載しないこと。
- 1文の説明や一度しか使わない極端に細かい語をタグ化しないこと。

推奨するタグ例:

- `meal-prep`
- `quick`
- `one-pot`
- `no-rice`
- `freezer-friendly`
- `blender`
- `spicy`
- `mild`
- `rescue`
- `experimental`
- `summer`
- `high-protein`

---

# 任意フィールド

必要な情報が本文または履歴から確認できる場合のみ、次の順序で追加すること。

```yaml
updated_at: 2026-08-02
cuisine:
  - middle-eastern-inspired
meal:
  - lunch
  - dinner
protein:
  - chicken
  - chickpea
base:
  - tomato
methods:
  - simmer
  - blend
servings: 6
rating: 4
source:
  type: original
related:
  standard: recipes/soup/standard.md
```

## `updated_at`

- レシピ本文の内容またはメタデータの意味を変更した日を記載すること。
- Front Matterを機械的に初回付与しただけの場合は追加しなくてよい。

## `cuisine`

料理の文化圏・系統を配列で記載すること。

- 完全再現でない場合は `-inspired` を付けること。
- 例: `indian-inspired`、`thai-inspired`、`middle-eastern-inspired`、`japanese`
- 根拠が曖昧な場合は省略すること。

## `meal`

主な用途を配列で記載すること。

- `breakfast`
- `lunch`
- `dinner`
- `snack`
- `meal-prep`

## `protein`

主なたんぱく源を配列で記載すること。

例:

- `chicken`
- `mixed-mince`
- `mackerel`
- `egg`
- `chickpea`
- `lentil`
- `tofu`

食材を網羅する一覧にはしないこと。

## `base`

味や液体の主要ベースを配列で記載すること。

例:

- `tomato`
- `miso`
- `dashi`
- `coconut-milk`
- `almond-milk`
- `soy-sauce`
- `noodle-soup`

## `methods`

特徴的な調理法だけを配列で記載すること。

例:

- `simmer`
- `stir-fry`
- `blend`
- `rice-cooker`
- `bake`
- `boil`
- `temper-spices`

## `servings`

- 数値で記載すること。
- 幅しか分からない場合はFront Matterでは省略し、本文へ記載すること。

## `rating`

- 実食評価が明確な場合のみ、1から5の整数で記載すること。
- 明示的な評価がない場合は推測しないこと。

## `source`

出典が必要な場合のみ記載すること。

```yaml
source:
  type: original
```

利用可能な `type`:

- `original`
- `adapted`
- `external`

外部由来の場合は、必要に応じて `name` と `url` を追加すること。URLだけを唯一の情報源にしないこと。

## `related`

関連文書が明確な場合のみ、リポジトリルートからの相対パスで記載すること。

```yaml
related:
  standard: recipes/soup/standard.md
  previous: recipes/soup/history/2026-07-19-example/notes.md
```

存在しないパスや将来作成予定のパスを記載してはいけない。

---

# Standardの例

```yaml
---
title: 鯖とレンズ豆の和風だしスパイススープ
document_type: standard
category: soup
status: standard
created_at: 2026-07-19
cuisine:
  - japanese-inspired
meal:
  - lunch
  - dinner
  - meal-prep
protein:
  - mackerel
  - lentil
base:
  - tomato
  - dashi
methods:
  - simmer
servings: 6
tags:
  - meal-prep
  - one-pot
  - high-protein
---
```

---

# Historyの例

```yaml
---
title: 鶏肉・ひよこ豆・セロリのトマトスープ初回試作
document_type: history
category: soup
status: tested
created_at: 2026-08-01
cuisine:
  - middle-eastern-inspired
meal:
  - dinner
  - meal-prep
protein:
  - chicken
  - chickpea
base:
  - tomato
methods:
  - temper-spices
  - blend
  - simmer
servings: 6
tags:
  - meal-prep
  - one-pot
  - blender
  - no-rice
---
```

---

# 既存Markdownへの一括付与

既存ファイルへFront Matterを追加する場合は次の手順を守ること。

1. 対象Markdownをすべて列挙すること。
2. 本文、パス、Git履歴から確認できる値だけを抽出すること。
3. 同義語と表記揺れを一覧化し、既存の標準値へ寄せること。
4. Front Matterだけを追加し、本文の内容やディレクトリ構成を同時に変更しないこと。
5. YAMLとして構文解析できることを検証すること。
6. 必須フィールドの欠落、未知の列挙値、重複タグを検査すること。
7. 変更件数と未判定項目を報告すること。
8. Front Matter付与完了後に、別の変更としてディレクトリ再編成を行うこと。

履歴ファイルの日付や評価を推測で補完してはいけない。

---

# 構成変更との分離

- Front Matter追加とファイル移動を同じ変更で実施してはいけない。
- 先に全対象へFront Matterを付与し、検索・分類可能な状態にすること。
- 構成変更ではFront Matterの `category` や `related` を根拠として移動先を決定すること。
- ファイル移動後は `related` のパス切れを検査すること。
- カレーやマサラの下位分類は、既存レシピの分布を確認してから別途決定すること。

---

# 禁止事項

- 本文にない評価や食材を推測で追加してはいけない。
- `tags` を材料一覧として利用してはいけない。
- カテゴリとタグへ同じ値を機械的に重複させてはいけない。
- 日本語、英語、単数形、複数形の表記揺れを混在させてはいけない。
- ディレクトリ名だけを根拠に文化圏を断定してはいけない。
- 将来のDBスキーマをFront Matterへそのまま持ち込み、編集しにくくしてはいけない。

---

# 検証

変更後は少なくとも次を確認すること。

- YAMLとして読み込めるか
- 必須フィールドが存在するか
- `document_type`、`category`、`status` が許可値か
- `created_at` が `YYYY-MM-DD` 形式か
- 配列項目が文字列の配列になっているか
- `rating` が1から5の整数か
- `related` のパスが存在するか
- 本文の先頭見出しと `title` が矛盾していないか

検証を実施していない場合は、未検証であることを明示すること。
