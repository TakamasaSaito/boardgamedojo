# 005: ロゴフォント適用状況（全13ゲーム）

作成日: 2026-07-31  
最終更新: 2026-07-31（Issue #38 対応にて未適用3ゲームに Orbitron を適用）  
調査背景: Issue #37 対応時に全ゲームのロゴフォントを一覧化

## 基準仕様（CLAUDE.md セクション3）

> ロゴフォント: Orbitron（英字ロゴ）。世界観に合わせたテーマフォントは
> タイトルロゴのみ許容（例: Onitama の明朝）

## 適用状況一覧

| ゲーム | ディレクトリ | ロゴフォント | 状態 |
|--------|------------|------------|------|
| Connect Four | `connect4` | Orbitron | 標準準拠 ✅ |
| Onitama | `onitama` | Shippori Mincho | 意図的テーマフォント（和風）✅ |
| Quoridor | `quridor` | Orbitron | 標準準拠 ✅ |
| Hive | `hive` | Orbitron | 標準準拠 ✅ |
| VIDRO | `vidro` | Orbitron | 標準準拠 ✅ |
| EGG | `egg` | Bebas Neue | 意図的テーマフォント（デコ系）✅ |
| NOCCA×NOCCA | `noccanocca` | Orbitron | 標準準拠 ✅ |
| the ONE | `the-ONE` | Orbitron | 標準準拠 ✅ |
| Hex | `hex` | Orbitron | 標準準拠 ✅ |
| Quantik | `quantik` | Orbitron | 標準準拠 ✅ |
| サイコロ五目並べ | `dice-gomoku` | Orbitron | 標準準拠 ✅ |
| Ostle | `ostle` | Orbitron | 標準準拠 ✅ |
| Connections | `connections` | Orbitron | 標準準拠 ✅ |

## 判断詳細

### 意図的テーマフォントとして許容したもの

**Onitama — Shippori Mincho**  
日本の伝統ボードゲームを題材とした和風テーマに合わせた選択。
CSS に `font-family: 'Shippori Mincho', serif;` が明示指定されており、
Google Fonts への読み込みも含む意図的な実装。CLAUDE.md の許容範囲内。

**EGG — Bebas Neue**  
ゲームロゴ全般に Bebas Neue が使用されている。Google Fonts から読み込み済みの
意図的な選択。縦長ディスプレイ向けのポップなデザインコンセプトに対応している。
CLAUDE.md の「世界観に合わせたテーマフォント」として許容。

### Issue #38 対応（2026-07-31）で適用した3ゲーム

**Connect Four**  
`.scr-logo { font-family: 'Noto Sans', sans-serif; }` を
`font-family: 'Orbitron', sans-serif;` に変更。
Google Fonts リンクに Orbitron を追加。

**Hive**  
`.screen-logo` に `font-family:'Orbitron',sans-serif;` を追加。
Google Fonts リンクに Orbitron を追加。

**VIDRO**  
`#splash-logo` に `font-family:'Orbitron',sans-serif;` を追加。
CSS `@import` に Orbitron を追加。
