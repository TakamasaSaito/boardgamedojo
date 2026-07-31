# STATUS.md — ボードゲームアプリ集

最終更新: 2026-08-01

## 現状
公開前レビュー指摘事項をすべて修正しコミット待ち状態。
修正内容: 言語フラグ Policy A 統一（現在表示中の言語フラグを表示するよう7ファイル修正）・
applyLang() 初期呼び出し追加（複数ファイル）・❓ボタン文字を `&#x2753;` エンティティに統一（quantik/hive）・
vidro の btn-home 表示制御追加・console.error 除去。
CLAUDE.md に言語フラグ仕様を明記・docs/decisions 3ファイル更新・README.md 新規作成。
残タスクは Google Analytics 測定ID設定（#6）のみ。

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
- [x] noccanocca の初回訪問判定復元・dice-gomoku 例外記録・privacy.html 記載更新（2026-07-30, fixes #33）
- [x] contact.html にGoogleフォームを主窓口として追加・privacy.html にフォームのデータ取り扱いを追記（2026-07-30, fixes #34）
- [x] 全16ファイル: GAスニペットを同一形式・コメントアウト状態に統一（dice-gomoku・ostle の有効実行解消、13ファイルにスニペット新規追加）。GA有効化Pythonスクリプト作成（2026-07-31, fixes #35）
- [x] 基準フォーマット未準拠箇所を是正（quantik id/翻訳キー・hex/hive/vidro/the-ONE howto id・vidroスプラッシュ・the-ONE screen-*プレフィックス除去）。全13ゲームのロゴフォント状況を docs/decisions/005-logo-font-status.md に記録（2026-07-31, fixes #37）
- [x] サイト全体仕上げ: meta description + OGタグ全16ファイル・aria-label 全13ゲーム・CSS変数補完8ファイル・Orbitron 3ゲーム適用・CLAUDE.md セクション11 更新（2026-07-31, fixes #38）
- [x] disclaimer.html 新設（知的財産権に関するご案内・JA/EN対応・権利状況一覧）・4ページフッターリンク統一（2026-07-31, fixes #38 一部）
- [x] disclaimer.html 権利者情報追記・専用OG画像作成（2026-08-01, fixes #39）
- [x] 公開前レビュー指摘事項 A〜G を修正（言語フラグ Policy A 統一・applyLang初期化・❓ボタン統一・vidro btn-home・console.error除去・CLAUDE.md更新・docs 3ファイル更新・README.md作成）（2026-08-01）

## 残タスク（GitHub Issues）

- [ ] Google Analytics 設定（全ファイル）→ [#6](https://github.com/TakamasaSaito/boardgamedojo/issues/6)

## 次の一手
Google Analytics 測定ID取得・設定（#6）
