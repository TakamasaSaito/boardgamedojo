# STATUS.md — ボードゲームアプリ集

最終更新: 2026-07-24

## 現状
全12ゲームのヘッダーに ⌂ ボタンを追加。ゲーム画面でのみ表示、タップでタイトルへ戻る。冗長な戻るボタン5件（dice-gomoku/EGG/Hex/NOCCA/Ostle）を削除（#20）。

## 完了済み
- [x] ポータル (index.html) 作成
- [x] GitHub / Netlify 連携・自動デプロイ設定
- [x] WSLへの移行・.gitignore 設置
- [x] 全ゲーム: iOS Safari 禁止パターン解消（バッククォート・async/await 等）
- [x] 全ゲーム: JS 内絵文字エスケープ（\uXXXX 形式）
- [x] 全ゲーム: Web Audio API サウンド追加
- [x] EGG: 配色統一・ヘッダー新設・言語切替追加（2026-07-24, fixes #1）
- [x] Onitama: 配色統一・ヘッダー新設・言語切替追加（2026-07-24, fixes #2）
- [x] VIDRO: 配色統一・ヘッダー新設・言語切替追加（2026-07-24, fixes #3）
- [x] サイコロ五目並べ: 配色統一・ヘッダー新設・言語切替追加（2026-07-24, fixes #4）
- [x] Ostle: 配色統一・ヘッダー新設・言語切替追加・画面フロー修正・サウンド追加（2026-07-24, fixes #5）
- [x] 全ゲーム: ヘッダーロゴをポータルへのリンクに変更（2026-07-24, fixes #9）
- [x] the ONE / Hex / Quantik / Hive: 起動フロー統一（初回のみhowto・Hive固定ヘッダー）（2026-07-24, fixes #10）
- [x] EGG: howto画面追加・.screen.active パターン統一（2026-07-24, fixes #12）
- [x] VIDRO: vidro_seen localStorage・#start-screen.active 統一（2026-07-24, fixes #13）
- [x] Connect Four: タイトル・howto画面新設・.screen.active 統一・localStorage（2026-07-24, fixes #14）
- [x] Quoridor: タイトル・howto画面新設・.screen.active 統一・localStorage（2026-07-24, fixes #15）
- [x] 全ゲーム+ポータル: PC表示最適化・@media(min-width:769px)でmax-width拡大（2026-07-24, fixes #11）
- [x] 全ゲーム: ヘッダーをパンくず形式に改善・スマホ/PC出し分け（2026-07-24, fixes #16）
- [x] 全ゲーム: 盤面以外の画面のPC表示最適化（2026-07-24, fixes #17）
- [x] 全ゲーム: URLを /フォルダ名/ 形式に簡潔化・リダイレクト削除（2026-07-24）
- [x] Onitama: スプラッシュ遷移不具合修正・countPieces nullガード（2026-07-24, fixes #18）
- [x] 全ゲーム+ポータル: タイトルタグを「ゲーム名 | BoardGameDojo」形式に統一（2026-07-24, fixes #19）
- [x] 全ゲーム: ゲーム内タイトルへ戻る導線のヘッダー集約（⌂ボタン）（2026-07-24, fixes #20）

## 残タスク（GitHub Issues）

### 優先度：高

### その他
- [ ] Google Analytics 設定（全ファイル）→ [#6](https://github.com/TakamasaSaito/boardgamedojo/issues/6)
- [ ] プライバシーポリシーページ作成 → [#7](https://github.com/TakamasaSaito/boardgamedojo/issues/7)
- [ ] 問い合わせページ作成 → [#8](https://github.com/TakamasaSaito/boardgamedojo/issues/8)

## 次の一手
Google Analytics 設定（全ファイル）→ [#6](https://github.com/TakamasaSaito/boardgamedojo/issues/6)
