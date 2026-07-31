# BoardGameDojo

ブラウザで遊べるボードゲームWebアプリ集。スマートフォン（iPhone Safari）向けに最適化された13作品を収録しています。

**公開URL**: https://takamasasaito.github.io/boardgamedojo/

## 収録タイトル（13作品）

| タイトル | ディレクトリ |
|---|---|
| Connect Four | `connect4/` |
| Onitama | `onitama/` |
| Quoridor | `quridor/` |
| Hive | `hive/` |
| VIDRO | `vidro/` |
| EGG | `egg/` |
| NOCCA×NOCCA | `noccanocca/` |
| the ONE | `the-ONE/` |
| Hex | `hex/` |
| Quantik | `quantik/` |
| サイコロ五目並べ | `dice-gomoku/` |
| Ostle | `ostle/` |
| CONNECTIONS | `connections/` |

## 技術スタック

- **構成**: 単一HTMLファイル（CSS・JS完全インライン）。ビルド工程・外部依存なし。
- **ホスティング**: GitHub Pages / Netlify Drop（静的ファイルのドラッグ＆ドロップでデプロイ可）
- **対象環境**: iPhone Safari を最優先ターゲットとする
- **サウンド**: Web Audio API（外部ライブラリ不使用）
- **言語**: 日本語／英語 切替対応（全タイトル）
- **AI対戦**: ミニマックス＋αβ枝刈り（depth 2〜4）

## ファイル構成

```
boardgamedojo/
├── index.html           # ポータル（ゲーム一覧）
├── privacy.html         # プライバシーポリシー
├── contact.html         # お問い合わせ
├── disclaimer.html      # 知的財産権表記
├── connect4/
│   └── index.html
├── ...（各ゲーム同構成）
├── _template/
│   └── index.html       # 新ゲーム追加用テンプレート
└── docs/
    └── decisions/       # アーキテクチャ決定記録（ADR）
```

## 開発ガイド

開発ルール・統一仕様・iOS Safari 禁止パターン・納品前チェックリストは [`CLAUDE.md`](CLAUDE.md) を参照してください。

## 知的財産権

収録タイトルはすべて非公式のファンメイド実装です。権利者情報・免責事項は [disclaimer.html](disclaimer.html) を参照してください。
