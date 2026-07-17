---
name: adr-writer
description: 重要な設計判断をADRとして記録し、意思決定の理由と代替案を残す共通ルールを定める
version: "1.0.0"

metadata:
  owner: keisuke
  language: ja
  category: governance
  tags:
    - adr
    - architecture-decision-record
    - decision-making
    - governance
    - design
---

# このスキルを利用するタイミング

以下の場合に利用すること。

- 重要な設計判断を記録する
- 技術選定の理由を残す
- DB 設計方針を残す
- API 設計方針を残す
- 認証・認可方針を残す
- セキュリティ判断を残す
- 運用設計の判断を残す
- レビュー結果による設計変更を記録する
- RFC から昇格した重要判断を記録する

---

# 基本方針

- この Skill は決定済み事項を扱うこと。
- ADR は仕様書ではないことを明確にすること。
- 「何を作るか」ではなく、「なぜそう決めたのか」を残すこと。
- 判断過程、検討した代替案、採用しなかった理由を記録すること。
- 推測を事実として扱ってはいけない。
- 設計の意図と結果を後から追跡できるようにすること。
- 実装コード全文を記載してはいけない。

---

# ADR の対象

以下を ADR の主な対象とすること。

- 技術選定
- DB 設計方針
- API 設計方針
- 認証・認可方針
- セキュリティ判断
- 運用設計
- レビュー結果による設計変更
- RFC から昇格した重要判断

---

# 保存先

- ADR は原則として `docs/adr/` に保存すること。
- ディレクトリが存在しない場合は作成すること。
- 既存 ADR を上書きせず、更新が必要な場合は新しい ADR を追加するか、Superseded として扱うこと。
- ADR は時系列で追跡できるようにすること。

---

# 命名規則

- ファイル名は `ADR-{number}-{slug}.md` 形式とすること。
- `number` は連番とすること。
- `slug` は英小文字・数字・ハイフンのみを使うこと。
- 例は次のとおりとすること。

```text
ADR-0001-use-supabase-rls.md
ADR-0002-materialized-view-refresh-strategy.md
```

---

# ADR テンプレート

ADR は以下の構造を標準とすること。

```text
# ADR-{number}: {title}

## Status

* Proposed
* Accepted
* Deprecated
* Superseded

## Date

YYYY-MM-DD

## Related RFC

関連RFCが存在する場合は記載する。

## Context

判断が必要になった背景を書く。

## Problem

解決したい問題を書く。

## Decision

採用した判断を書く。

## Alternatives Considered

検討した代替案を書く。

### Option A

### Option B

### Option C

採用・不採用理由も記載する。

## Consequences

採用による影響を書く。

### Positive

### Negative

### Operational Impact

## Risks

残るリスクを書く。

## Follow-up

追加で必要な対応を書く。
```

- 実装コード全文は記載しないこと。
- 判断の背景、比較対象、採用理由を必ず残すこと。
- 読み手が前提を追える粒度で書くこと。

---

# 記載ルール

- 決定内容だけでなく理由を書くこと。
- 採用しなかった案も残すこと。
- 推測を事実として扱わないこと。
- 読み手が背景を理解できる粒度にすること。
- 感想ではなく判断記録として書くこと。
- 変更内容と影響範囲を後から追えるようにすること。

---

# RFC との関係

- RFC は議論を扱うこと。
- ADR は決定を扱うこと。
- 重要な議論が確定した場合は RFC から ADR へ昇格すること。
- RFC の内容をそのまま ADR に転記するのではなく、決定事項に再構成すること。

---

# SPEC との関係

- ADR は仕様書を置き換えないこと。
- 仕様は `docs/spec.md` に記載すること。
- ADR は判断理由を保持すること。
- SPEC は確定仕様を保持すること。
- ADR と SPEC の責務を混同しないこと。

