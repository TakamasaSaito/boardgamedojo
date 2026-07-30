# STATUS.md — ボードゲームアプリ集

最終更新: 2026-07-30

## 現状
問い合わせページ（contact.html）を作成（#8）。privacy.html / index.html のフッターに相互リンクを追加し、著作権年を 2025-2026 に統一。残タスクは Google Analytics 設定（#6）のみ。

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
- [x] 全ゲーム+ポータル: Web Appスタンドアロン用メタタグ・manifest.json追加（2026-07-24, fixes #21）
- [x] 全ゲーム: スマホ幅パンくずを「← BoardGameDojo」表示に修正・CSS変更のみ（2026-07-24, fixes #22）
- [x] アプリアイコン作成・配置（盤面グリッドデザイン、apple-touch-icon/icon-192/icon-512/favicon.ico、manifest.json更新）（2026-07-24）
- [x] 全ゲーム: スマホ幅ボタンテキスト折り返し解消（Onitamaのみ修正: .btn-group .btn {flex:1}追加）（2026-07-25, fixes #23）
- [x] 新ゲーム追加用テンプレート正本化: `_template/index.html` / CLAUDE.md セクション11 / `docs/decisions/001-game-template.md` 作成（2026-07-27, fixes #26）
- [x] CONNECTIONS: 起動フロー（splash→howto初回→title→game）・btn-home 追加・遊び方JA/EN作成（2026-07-27, fixes #27）
- [x] hex・noccanocca・the-ONE のヘッダーをグローバル固定 `#app-header` に統一（2026-07-30, fixes #29）
- [x] hive・vidro スプラッシュを `.screen.active` 方式に統一、hive・quridor の CSS変数を標準セットに統一（2026-07-30, fixes #30）
- [x] egg・ostle・hex のスプラッシュ後遷移を localStorage 初回判定方式に統一（2026-07-30, fixes #31）
- [x] noccanocca・onitama の howto 構成方針を決定（案C）・準拠条件を文書化・実装（2026-07-30, fixes #32）
- [x] プライバシーポリシーページ作成（2026-07-30, fixes #7）
- [x] 問い合わせページ作成・フッター相互リンク・著作権年統一（2026-07-30, fixes #8）

## 残タスク（GitHub Issues）

- [ ] Google Analytics 設定（全ファイル）→ [#6](https://github.com/TakamasaSaito/boardgamedojo/issues/6)

## 次の一手
Google Analytics 設定（#6）
