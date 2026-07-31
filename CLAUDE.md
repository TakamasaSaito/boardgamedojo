# CLAUDE.md — ボードゲームアプリ集 開発指示書

このファイルは、ボードゲームWebアプリ集(全12作品)の開発・修正をClaudeに依頼する際の共通指示書です。チャット開始時にこのファイルを貼り付けてください。Claudeはこの内容を絶対的なルールとして扱い、例外が必要な場合は必ず作業前に確認を取ります。

---

## 1. プロジェクト概要

- **構成**: 中央ポータル1枚 + 各ゲーム個別HTML 12枚。マージはしない。各ゲームは完全に独立した単一HTMLファイル(CSS/JSすべてインライン)。
- **12作品**: Connect Four / Onitama / Quoridor / Hive / VIDRO / EGG / NOCCA×NOCCA / the ONE / Hex / Quantik / サイコロ五目並べ / Ostle
- **デプロイ**: Netlify Drop(静的HTMLのドラッグ&ドロップ)。ビルド工程・外部依存なし。
- **主要ターゲット**: iPhone Safari。すべての実装はiOS Safari互換を最優先とする。
- **各ゲームの構成**: 「ゲーム名.html + index.htmlリダイレクト」の2ファイル構成を維持。

## 2. 開発ワークフロー(必須の順序)

1. **要件確認** — 作業内容を要約し、解釈をユーザーに提示して承認を得る
2. **ルール調査**(新規ゲームの場合) — Web検索で公式ルールを確認し、ユーザーに確認を取ってから実装
3. **機能実装** — まず素のHTMLでロジックを動く状態にする(デザインは後)
4. **動作確認** — ユーザーがチャット内/実機で動作確認
5. **デザイン適用** — 統一デザイン(セクション3)を上から適用
6. **セルフチェック** — 納品前に禁止パターン検査(セクション5)を実行
7. **納品** — 完成HTMLを1ファイルで出力

- 各ステップは明示的な承認を得てから次へ進む。
- 確認はオープンな質問ではなく**選択式(A/B/C)** で提示する。
- 既存ファイルの更新は「完成HTMLを土台に差分更新」。ゼロから書き直さない。
- デザイン判断が曖昧な場合(駒の見た目など)は、比較用デモHTMLを作って選んでもらう。

## 3. 統一デザイン仕様(全ゲーム共通・例外なし)

既存ファイルが独自デザインでも、統一仕様を優先して修正する。

| 項目 | 仕様 |
|---|---|
| 背景色 | `#0f0f0f` |
| サーフェス | `#1a1a1a` / `#222222` |
| UIアクセント | `#00bcd4`(シアン)。ボタン・枠線・選択状態・見出し・グロー等、UI/ブランディングはシアン中心 |
| プレイヤー識別色 | 機能上の例外。既存の赤/黄、赤/青などをゲームごとに維持してよい |
| テキスト | `#e0e0e0` / 淡色 `#888888` |
| 角丸 | 12px基調(`--radius: 12px` をCSS変数化) |
| UIフォント | Noto Sans JP / Noto Sans |
| ロゴフォント | Orbitron(英字ロゴ)。世界観に合わせたテーマフォントはタイトルロゴのみ許容(例: Onitamaの明朝) |
| 言語切替 | 🇯🇵/🇺🇸トグルを全ゲーム必須。全UI文言をJA/EN両対応。**ボタンには現在表示中の言語のフラグを表示する（切替先ではない）**: 日本語表示中→🇯🇵、英語表示中→🇺🇸 |
| 難易度表記 | 「かんたん / ふつう / むずかしい」(3段階固定) |
| サウンド | Web Audio API効果音を全ゲーム必須(選択音・移動/配置音・勝利音を最低限) |
| 画面構成 | 複数画面切替方式: `.screen` / `.screen.active` パターン(スプラッシュ→タイトル→ゲーム) |
| ヘッダー | 左上=ロゴ(タップでホーム)、右側=言語切替+❓ヘルプ |
| ヘルプ | トリガーは❓アイコン。閉じたら開いた画面に戻る(`prevScreen`変数で記憶)。表示形式はルール量に応じてモーダル/専用画面を選択可 |

**お手本実装**: NOCCA×NOCCA(画面切替・prevScreen・CSS変数・サウンド)、Quantik(prevScreen・絵文字エスケープ)、Hive(絵文字エスケープの徹底)、サイコロ五目並べ(arcTo手描き角丸・removeChild・サウンド)

## 4. iOS Safari 禁止パターン(全ファイル・毎回検査)

過去に実機で不具合を起こした実績のあるパターン。**理由を問わず使用禁止。**

| 禁止 | 代替 |
|---|---|
| テンプレートリテラル(バッククォート) | 文字列連結 `'a' + b` |
| `async` / `await` | Promiseチェーンまたは同期処理 |
| `confirm()` / `alert()` | 自作モーダル |
| 8桁hexカラー `#RRGGBBAA` | `rgba()` |
| `ctx.ellipse()` | `ctx.arc()` またはベジェ曲線で手描き |
| `ctx.roundRect()` | `arcTo()` で手描き(サイコロ五目並べの `drawRoundRect()` 参照) |
| `el.remove()` | `el.parentNode.removeChild(el)` |
| onclick属性内のシングルクォート | 引数なしのラッパー関数を作って呼ぶ |
| `type="module"` | 通常の `<script>` |
| JS文字列リテラル内の絵文字直書き | `\uXXXX` サロゲートペア(例: `"\uD83C\uDDEF\uD83C\uDDF5"`)または `\u{1F3C6}` 形式。HTML側の絵文字直書きはOK |
| `const` / `let` | `var` を推奨(既存コードとの統一) |

## 5. 納品前セルフチェック(必須)

コード出力の直前に以下を必ず実行し、結果を報告する。

1. **禁止パターンgrep**: バッククォート、`async`、`await`、`confirm(`、`alert(`、`.ellipse(`、`.roundRect(`、`.remove()`、`type="module"` を検索してゼロ件を確認
2. **JS内絵文字検査**: `<script>` 内に生の絵文字(サロゲートペア文字)がないことを確認
3. **構文チェック**: `node -e "new Function(jsCode)"` 相当でJSの構文エラーがないことを確認
4. **統一仕様チェック**: 背景 `#0f0f0f`、アクセント `#00bcd4`、角丸12px、言語切替、難易度3表記、サウンドの有無を確認
5. 違反が見つかった場合は修正してから再チェック。チェック結果を「✅/❌リスト」で報告してから納品する。

## 6. お手本実装と参考情報

詳細な残タスクは GitHub Issue を参照（STATUS.md にリンクあり）。

**お手本実装**
- NOCCA×NOCCA: 画面切替・prevScreen・CSS変数・サウンド
- Quantik: prevScreen・絵文字エスケープ
- Hive: 絵文字エスケープの徹底
- サイコロ五目並べ: arcTo手描き角丸・removeChild・サウンド
- EGG: T{}オブジェクト・applyLang() による言語切替パターン

## 7. AI実装の知見

- 強いAIには「ゴールへの前進度を測る `reach()`」+「前進度と経路コストを組み合わせた `threatMetric()`」+「防御優先切替」+「孤立配置ペナルティ」が有効(TwixTでの実績)。純粋なヒューリスティック/距離ベースは弱い。
- ミニマックス系はdepth 2〜4 + αβ枝刈りが応答速度の実用ライン。
- CPU思考中は「思考中...」インジケータ表示 + 入力ロック(`cpuThinking` フラグ)を必ず入れる。

## 8. UXパターンの知見

- **方向選択UI**(Quoridorの壁など): 暗黙のトグルではなく、視覚アイコン付きの明示的モーダルで縦/横を選ばせてから配置モードに入る。
- **特殊ルールの説明**(Hexのスワップなど): 混乱しやすいメカニクスは、発動タイミングのモーダル内に平易な説明を直接埋め込む。
- **タップターゲット**: 最小44×44px。
- **アンドゥ**: CPU対戦では2手戻す(自分+CPU)。

## 9. その他の運用ルール

- Google Analytics埋め込みを各HTMLに含める(ページ単位計測)。
- ポータル(index/プライバシーポリシー/問い合わせ)はAdSense対応を維持。
- プロジェクト紹介はnote.comの記事(カジュアルな「作ってみた」トーン)。
- フッターのコピーライトは「© 公開開始年-現在年 BoardGameDojo」形式（例: © 2025-2026）。年をまたぐ際は現在年を更新する。

## 10. プロジェクト管理方針

**GitHub = 唯一の台帳**  
タスク・成果物・状態はGitHub上で管理する。ローカルメモ等への分散禁止。

**Issue = タスクの管理単位**  
- 粒度: 1〜2セッションで終わる作業を1 Issue
- 本文: Claude Codeへの指示書として機能する内容（作業内容・参考ファイル・完了条件）を書く
- クローズ: コミットメッセージに `fixes #N` を書いて自動クローズ

**STATUS.md = 現状のスナップショット**  
- 項目: 最終更新日 / 現状(1〜2行) / 完了済み / 残タスク(Issueリンク) / 次の一手(1つだけ)
- 更新タイミング: 作業終了時に必ず更新してコミットに含める

**GitHub Projects「Portfolio」ボード**  
全Issueをボードに登録する(ボードは今後作成)。フィールド: Status / Category / Priority / Next Action

**Claudeへの指示**  
- 作業終了時は STATUS.md を必ず更新してコミットに含める
- 新タスク発生時は Issue 起票を提案する
- 方針変更時は該当ドキュメントを同時更新する

## 11. 新ゲーム追加チェックリスト

新ゲームを追加するときは `_template/index.html` を土台にする。
テンプレート採用の背景・例外ゲーム一覧は `docs/decisions/001-game-template.md` を参照。

### ファイル作成
- [ ] `game-name/index.html` を `_template/index.html` からコピーして作成
- [ ] `GAME_NAME` プレースホルダを実際のゲーム名に全置換
- [ ] `GAMENAME_seen` を実際のゲーム名ベースのキー（例: `connections_seen`）に変更

### 起動フロー（必須3点）
- [ ] **splash → howto（初回のみ） → title → game** の遷移が動作する
      ※ `localStorage.getItem('GAMENAME_seen')` で初回判定
- [ ] **howto から閉じたとき `prevScreen` の画面に正しく戻る**
      （❓ボタンからゲーム中に開いた場合は game へ、初回自動表示なら title へ）
- [ ] **ゲーム画面（`id="game"`）のときだけ `#btn-home` が表示され、
      クリックで `goToTitle()` が呼ばれる**
      ※ `showScreen()` 内の `(id === 'game') ? '' : 'none'` で制御

### howto 画面の準拠条件

**必須（これをすべて満たせば準拠）**
- [ ] howto 画面の id が `"howto"` である（`<div id="howto" class="screen">`）
- [ ] `openHowto(from)` / `closeHowto()` 経由で開閉する
- [ ] `closeHowto()` で `prevScreen` の画面に戻る
- [ ] `showScreen()` の管理下にある（`.screen` クラスで制御される）
- [ ] howto 内の全文言が翻訳オブジェクト `T` にあり `applyLang()` で切り替わる

**許容（準拠違反としない拡張）**
- 内部の多段スライド・ドットナビ・ミニボード・カードグリッドなどの演出
- 「スキップ」ボタンによる早期終了
- `rulesScreen` / `cardsScreen` など howto 外の参照専用画面の追加
  （詳細: `docs/decisions/002-howto-screen-standard.md`）

### ヘッダー・パンくず
- [ ] `#app-header` が存在し、スプラッシュ時は `class="hidden"`、以降は `.hidden` 除去
- [ ] パンくずに `← BoardGameDojo | ゲーム名` が入っている
      ※ `.bc-full` クラスは `@media (min-width: 769px)` でのみ表示（スマホは「← BoardGameDojo」のみ）
- [ ] 言語切替ボタン（🇯🇵/🇺🇸）が `#lang-btn` として存在する
- [ ] ヘルプボタン（❓）が `id="help-btn"` で存在し `openHowto()` を呼ぶ
- [ ] `#btn-home` / `#lang-btn` / `#help-btn` に `aria-label` を付与し、
      `applyLang()` 内で JA/EN に切り替えること
      JA: ホームへ戻る / 言語切替 / 遊び方を開く
      EN: Back to home / Switch language / Open how to play

### デザイン
- [ ] CSS変数 `--bg / --surface / --surface2 / --accent / --text / --text-dim / --radius` を使用
- [ ] 難易度表記は **「かんたん / ふつう / むずかしい」**（3段階固定・漢字・かな混在禁止）
- [ ] フォント: Orbitron（ロゴ）+ Noto Sans JP（UI）

### メタタグ（パス必須確認）
- [ ] `manifest` / `apple-touch-icon` / `favicon.ico` のパスが **相対パス**（`../xxx`）
      ※ ルート絶対パス（`/xxx`）禁止。理由: GitHub Pages サブディレクトリ配信では
        `/` がリポジトリルートを指さない（Issue #24参照）
- [ ] `<meta name="description">` が存在し、各ページ固有の日本語 description（120文字程度）
- [ ] OG タグ一式（`og:title` / `og:description` / `og:image` / `og:url` / `og:type`）が存在する
- [ ] `<meta name="twitter:card" content="summary_large_image">` が存在する
- [ ] `og:image` は `../apple-touch-icon.png`（サブディレクトリ）または `apple-touch-icon.png`（ルート）
- [ ] `og:url` のみ絶対URL（`https://takamasasaito.github.io/boardgamedojo/...`）を使用し、
      相対パス禁止ルールの例外である旨をHTMLコメントで明記する

### サウンド
- [ ] `playSound()` が実装されており、最低限 `select` / `place`（or `move`） / `win` の3種が鳴る

### ポータル（index.html）の更新
- [ ] ゲームカードを追加（画像・タイトル・説明・リンク）
- [ ] ゲーム数の表記を更新（例: `13 GAMES` → `14 GAMES`）
- [ ] カテゴリの `count` を更新
- [ ] 翻訳オブジェクト `T` にゲーム名・説明を追加（ja/en 両方）
- [ ] `applyLang()` の更新箇所に新カードの文言を含める

### セルフチェック（セクション5）
- [ ] 禁止パターン grep でゼロ件確認（バッククォート・`async`・`await` 等）
- [ ] JS 内絵文字検査（`\uXXXX` エスケープになっているか）
- [ ] 統一仕様チェック（`#0f0f0f` / `#00bcd4` / 12px / 言語切替 / 難易度3表記 / サウンド）
