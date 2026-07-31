# 002 howto 画面の準拠定義と noccanocca・onitama の例外対応

- **日付**: 2026-07-30
- **決定者**: TakamasaSaito
- **関連 Issue**: #28

## 背景

#28 の是正作業で、noccanocca と onitama の howto 構成が標準テンプレートから
大きく乖離していることが判明した。

| ゲーム | 乖離内容 |
|---|---|
| noccanocca | howto が `onboardScreen`（3スライド）と `howScreen`（テキスト参照）の2画面に分割 |
| onitama | howto が `howtoScreen`（4スライド）・`rulesScreen`（詳細ルール）・`cardsScreen`（カード一覧）の3画面構成 |

スライドビジュアルやカード一覧などの演出を捨てると説明クオリティが低下するため、
「外枠を標準化・内部構成は自由」とする案Cを採用した（Issue #28-4 にて決定）。

## howto 準拠の定義

### 必須（これを満たせば準拠とみなす）

| 条件 | 詳細 |
|---|---|
| **id が `"howto"`** | `<div id="howto" class="screen">` であること |
| **開閉関数** | `openHowto(from)` / `closeHowto()` 経由で開閉すること |
| **prevScreen 復帰** | `closeHowto()` 実行時に `prevScreen` の画面に戻ること |
| **showScreen() 管理下** | `SCREENS` 配列または `querySelectorAll('.screen')` に含まれること |
| **JA/EN 両対応** | howto 内の全文言を翻訳オブジェクト `T` で管理し、`applyLang()` で切り替わること |

### 許容（ゲーム固有の拡張として自由）

以下は標準テンプレートとの差異があっても準拠違反としない。

- howto 内部の多段スライド（ドット・前後ナビ）
- ミニボード・カードグリッドなどのインタラクティブビジュアル
- 「スキップ」ボタンによる早期終了
- `rulesScreen` / `cardsScreen` など howto とは別の参照専用画面の追加
  （ただし、これらは howto の外にある独立画面であり、
    `prevScreen` 復帰の起点は必ず howto とすること）

### 固定オーバーレイ方式（hive のみ）

hive の howto は `showScreen()` を使わず、howto 要素に直接 `.active` クラスを
付け外しする固定オーバーレイ方式を採用している。

```js
function openHowto(from) { howtoFrom = from; document.getElementById("howto").classList.add("active"); }
function closeHowto() { document.getElementById("howto").classList.remove("active"); }
```

- `showScreen()` の管理外だが、howto が常時 DOM に存在する固定レイヤーのため
  画面復帰の問題は発生しない
- `prevScreen` ではなく `howtoFrom` で開いた文脈を保持する
- この方式は hive 固有の意図的例外であり、他ゲームへの踏襲禁止

## 既存ゲームへの適用（是正内容）

### noccanocca（是正済み）

- `onboardScreen` → `id="howto"` に改名
- `howScreen` を `howto` 内のセクションとして統合
- `openHowto()` / `closeHowto()` を標準パターンで実装

### onitama（是正済み）

- `howtoScreen` → `id="howto"` に改名
- JS の参照を `showScreen("howto")` に統一
- `rulesScreen` / `cardsScreen` は「許容される拡張」として維持

## 今後の新規ゲーム追加への影響

`CLAUDE.md` セクション11 の howto チェック項目に準拠条件を追記した。
複雑なゲームでスライド説明が必要な場合は、上記「許容」の範囲内で実装してよい。
