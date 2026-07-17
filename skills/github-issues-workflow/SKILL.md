---
name: github-issue-management
description: GitHub Issue の作成・更新・Close・重複確認を扱う
version: "1.0.0"

metadata:
  owner: keisuke
  language: ja
  category: workflow
  tags:
    - github
    - issue
    - gh
---

# このスキルを利用するタイミング

以下の場合に利用すること。

- GitHub Issue を新規作成する
- GitHub Issue を更新する
- GitHub Issue を Close する
- GitHub Issue の重複を確認する
- GitHub CLI (`gh`) で Issue を操作する

---

# 基本方針

- Issue は、現在の依頼範囲外だが後で対応すべき内容を記録するために使うこと。
- 現在の依頼を勝手に拡張して実装してはいけない。
- Issue は思いつきメモではなく、後から着手できる作業単位として扱うこと。
- この Skill では GitHub Project の更新を扱わないこと。

---

# 判断フロー

1. 現在の依頼内でそのまま解決できるか確認すること。
2. 現在の依頼外で、後から対応すべき内容か判断すること。
3. Issue 化が必要なら既存 Issue を検索すること。
4. 重複がなければ新規 Issue を作成すること。
5. 既存 Issue があるなら更新すること。
6. Close 条件を満たした場合のみ Close すること。
7. 判断に迷う場合は、勝手に作成せずユーザーへ確認すること。

---

# Issue を作成する条件

以下に該当する場合は Issue を作成してよいこと。

- 現在の依頼とは無関係な不具合を発見した
- 技術的負債を発見した
- 将来的な改善案を見つけた
- 調査が必要な内容を見つけた
- ドキュメント整備が必要と判断した
- 今回対応しないが記録しておくべき内容を見つけた

---

# Issue を作成しない条件

以下は Issue 化しないこと。

- 現在の依頼内でそのまま修正できる軽微な問題
- コードスタイルのみの指摘
- 個人的な好みレベルのリファクタリング
- 効果が不明確な改善案
- 根拠のない推測

---

# 重複確認

- Issue を作成する前に既存 Issue を検索すること。
- 同じ内容の Issue がある場合は新規作成しないこと。
- 既存 Issue がある場合は、その Issue に情報を追加すること。

---

# タイトル規則

- タイトルは内容が一目で分かるよう簡潔に記述すること。
- 以下のプレフィックスを利用すること。
  - `feat:`
  - `fix:`
  - `docs:`
  - `refactor:`
  - `research:`
  - `idea:`
  - `chore:`

例:

- `feat: 棚卸CSV出力を追加する`
- `fix: PostgREST の in 句が失敗する`
- `research: イベント履歴取得方法を調査する`

---

# ラベル

- 可能な限り以下のラベルを付与すること。

## 種類

- `kind/feature`
- `kind/bug`
- `kind/docs`
- `kind/refactor`
- `kind/research`
- `kind/idea`
- `kind/chore`

## 対象領域

- `area/` をプレフィックスとして使うこと。
- 対象が明確な場合は、対象となるプロジェクト名やアプリ名も許容すること。
- `area/backend`
- `area/frontend`
- `area/sql`
- `area/infra`
- `area/ec`
- `area/docs`
- 例:
  - `area/backend`
  - `area/listing_policy_worker`
  - `area/wasabiswitch`

## 優先度

- `priority/P0`
- `priority/P1`
- `priority/P2`
- `priority/P3`

---

# Issue 本文

- Issue 本文には最低限以下を含めること。

## 背景

なぜ対応が必要なのかを書くこと。

## 現状

現在の問題点を書くこと。

## 対応案

想定する解決方法を書くこと。

## 完了条件

Issue を Close できる条件を書くこと。

## 補足

必要に応じて参考 URL やメモを書くこと。

---

# Close 時

- 完了条件を満たした場合のみ Close すること。
- Close 前に、対応内容が完了していることを確認すること。
- 関連するコミットや Pull Request がある場合は Issue に関連付けること。

---

# GitHub CLI

- `gh` が利用可能な環境では CLI による操作を優先してよいこと。
- `gh` を使う場合も、先に既存 Issue の重複確認を行うこと。
- 使う操作は Issue の検索、作成、更新、Close に限定すること。

---

# 出力方針

- Issue 本文は簡潔かつ具体的に記載すること。
- 背景、目的、完了条件が第三者にも理解できる内容にすること。
- 必要以上に長文化しないこと。

---

# 自律的な判断

- Issue を作成できる状況であれば、毎回ユーザー確認を求めないこと。
- ただし以下の場合は確認すること。
  - 作業内容が曖昧
  - ラベルが判断できない
  - Issue 化する価値が低い可能性がある
  - 同一内容の Issue が存在する可能性が高い
