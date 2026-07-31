# 001 新ゲーム追加用テンプレート方式の採用

- **日付**: 2026-07-27
- **決定者**: TakamasaSaito

## 決定内容

`_template/index.html` を正本として管理し、新ゲーム追加時の土台とする。
新ゲーム追加チェックリストは `CLAUDE.md` セクション11 に記載。

## 背景

13本目(CONNECTIONS)追加時に、スプラッシュ→howto起動フローと
ゲーム画面のホーム復帰ボタン(btn-home)が欠落した。
「統一ルール」がリポジトリ内に正本なく既存実装に暗黙的に
存在するだけだったことが原因(Issue #26)。

## 採用した標準仕様（多数派ベース・12ゲーム調査より）

| 項目 | 採用仕様 | 根拠 |
|---|---|---|
| スプラッシュ | `.screen.active` 方式 | 12ゲーム中10ゲームが採用 |
| ヘッダー | グローバル固定 `#app-header`（hidden→active） | 12ゲーム中9ゲームが採用 |
| howto | 独立した `.screen` + prevScreen で復帰 | 全ゲーム共通パターン |
| 初回判定 | `localStorage` の `GAMENAME_seen` フラグ | connect4/quridor 等の多数派 |
| CSS変数 | `--bg / --surface / --surface2 / --accent / --text / --text-dim / --radius` | 全ゲーム共通 |

## 既存ゲームの例外（意図的・永続）

| ゲーム | 乖離内容 | 状態 |
|---|---|---|
| dice-gomoku | スプラッシュがタップ不可の2秒自動遷移・独自CSS・localStorage判定なし（→ 003 参照） | 意図的例外 |
| hive | howto が固定オーバーレイ方式（`showScreen()` 非使用、`.active` クラスの直接付け外し） | 意図的例外（→ 002 参照） |

## 是正済み

| ゲーム | 是正内容 | Issue |
|---|---|---|
| noccanocca | ヘッダーをグローバル固定 `#app-header` に統一 | #28-1 |
| noccanocca | howto を `id="howto"` + `openHowto/closeHowto` 標準構成に統一 | #28-4 |
| noccanocca | `noccanocca_seen` による初回訪問判定を復元 | #33 |
| hive, vidro | スプラッシュを `.screen.active` 方式に統一 | #30 |
| hex, the-ONE | ヘッダーをグローバル固定 `#app-header` に統一 | #30, #37 |
| egg | `egg_seen` による初回訪問判定を追加 | #31 |
| ostle | howto 画面を追加 | #5 |
| onitama | howtoScreen を `id="howto"` に改名・標準開閉関数を実装（→ 002 参照） | #28 |

## howto の準拠定義について

howto 画面は「必須条件（id・開閉関数・prevScreen復帰）を満たせば準拠」とし、
内部のスライド構成やビジュアルはゲーム固有の拡張として許容する。
詳細は `docs/decisions/002-howto-screen-standard.md` を参照。
