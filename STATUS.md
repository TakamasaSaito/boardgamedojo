# STATUS.md — ボードゲームアプリ集

最終更新: 2026-07-24

## 現状
Group E のうち EGG (#12)・VIDRO (#13)・Connect Four (#14) の起動フロー統一完了。残りは Quoridor (#15)。

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

## 残タスク（GitHub Issues）

### 優先度：高
- [ ] 全ゲーム+ポータル: PC画面での表示最適化 → [#11](https://github.com/TakamasaSaito/boardgamedojo/issues/11)

### その他
- [ ] Google Analytics 設定（全ファイル）→ [#6](https://github.com/TakamasaSaito/boardgamedojo/issues/6)
- [ ] プライバシーポリシーページ作成 → [#7](https://github.com/TakamasaSaito/boardgamedojo/issues/7)
- [ ] 問い合わせページ作成 → [#8](https://github.com/TakamasaSaito/boardgamedojo/issues/8)

## 次の一手
全ゲーム+ポータルのPC表示最適化（[#11](https://github.com/TakamasaSaito/boardgamedojo/issues/11)）
