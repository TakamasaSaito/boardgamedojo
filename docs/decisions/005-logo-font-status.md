# 005: ロゴフォント適用状況（全13ゲーム）

作成日: 2026-07-31  
調査背景: Issue #37 対応時に全ゲームのロゴフォントを一覧化

## 基準仕様（CLAUDE.md セクション3）

> ロゴフォント: Orbitron（英字ロゴ）。世界観に合わせたテーマフォントは
> タイトルロゴのみ許容（例: Onitama の明朝）

## 適用状況一覧

| ゲーム | ディレクトリ | ロゴフォント | 状態 |
|--------|------------|------------|------|
| Connect Four | `connect4` | Noto Sans | 未適用・要対応 |
| Onitama | `onitama` | Shippori Mincho | 意図的テーマフォント（和風）✅ |
| Quoridor | `quridor` | Orbitron | 標準準拠 ✅ |
| Hive | `hive` | 指定なし（Noto Sans JP にフォールバック） | 未適用・要対応 |
| VIDRO | `vidro` | 指定なし（Noto Sans JP にフォールバック） | 未適用・要対応 |
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

### 未適用（要対応）

**Connect Four — Noto Sans**  
`.scr-logo { font-family: 'Noto Sans', sans-serif; }` と明示されており
Orbitron が未使用。Google Fonts 読み込みも Orbitron を含まない。
単なる未適用と判断。別途 Issue で対応予定。

**Hive — font-family 指定なし**  
`.screen-logo { font-size:44px; font-weight:700; }` に font-family 指定なく、
body の Noto Sans JP にフォールバック。Orbitron 読み込みも行われていない。
単なる未適用。別途 Issue で対応予定。

**VIDRO — font-family 指定なし**  
`#splash-logo { font-size:clamp(...); }` に font-family 指定なく、
body の Noto Sans JP にフォールバック。Orbitron 読み込みなし。
単なる未適用。別途 Issue で対応予定。

## 今後の対応

未適用 3 ゲーム（Connect Four / Hive / VIDRO）に対して個別 Issue を起票し、
Orbitron 適用を行う予定。
