# 004 — Google Analytics 有効化手順 (Issue #6)

## 背景

全17ファイルに同一形式のGAスニペット（`GA_MEASUREMENT_ID` プレースホルダー）を
コメントアウト状態で配置済み（Issue #F 対応、2026-07-31）。
GA 測定 ID 取得後にこの手順で一括有効化する。

## 有効化手順

### 1. 測定 ID を取得する

Google Analytics → 管理 → データストリーム → ウェブストリームの詳細 → 測定 ID  
形式: `G-XXXXXXXXXX`

### 2. 全ファイルを一括置換する（リポジトリルートで実行）

```bash
# macOS / BSD sed
find . -name "*.html" -not -path "./_template/*" \
  -exec sed -i '' \
    -e 's/<!-- Google Analytics: 実装時に GA_MEASUREMENT_ID を置換してこのコメントを外す -->/<!-- Google Analytics -->/g' \
    -e 's/<!--\n//' \
    {} \;

# より確実な方法: Python スクリプトで実行
python3 docs/decisions/004-ga-activate.py G-XXXXXXXXXX
```

**推奨: Python スクリプト方式（下記）**

### 3. Python スクリプト（推奨）

```python
#!/usr/bin/env python3
# 使い方: python3 docs/decisions/004-ga-activate.py G-XXXXXXXXXX
import sys, re, glob

if len(sys.argv) != 2 or not sys.argv[1].startswith('G-'):
    print('使い方: python3 004-ga-activate.py G-XXXXXXXXXX')
    sys.exit(1)

MEASUREMENT_ID = sys.argv[1]

# コメントアウトブロックを有効なスニペットに置換
OLD = (
    '<!-- Google Analytics: 実装時に GA_MEASUREMENT_ID を置換してこのコメントを外す -->\n'
    '<!--\n'
    '<script src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>\n'
    '<script>\n'
    '  window.dataLayer = window.dataLayer || [];\n'
    '  function gtag(){dataLayer.push(arguments);}\n'
    '  gtag(\'js\', new Date()); gtag(\'config\', \'GA_MEASUREMENT_ID\');\n'
    '</script>\n'
    '-->'
)

NEW = (
    '<!-- Google Analytics -->\n'
    '<script src="https://www.googletagmanager.com/gtag/js?id={id}"></script>\n'
    '<script>\n'
    '  window.dataLayer = window.dataLayer || [];\n'
    '  function gtag(){{dataLayer.push(arguments);}}\n'
    '  gtag(\'js\', new Date()); gtag(\'config\', \'{id}\');\n'
    '</script>'
).format(id=MEASUREMENT_ID)

files = glob.glob('**/*.html', recursive=True)
files = [f for f in files if not f.startswith('_template/')]
updated = []

for path in files:
    content = open(path, encoding='utf-8').read()
    if 'GA_MEASUREMENT_ID' in content:
        new_content = content.replace(OLD, NEW)
        if new_content != content:
            open(path, 'w', encoding='utf-8').write(new_content)
            updated.append(path)

print(f'{len(updated)} ファイルを更新しました:')
for f in sorted(updated):
    print(f'  {f}')
```

このスクリプトを `docs/decisions/004-ga-activate.py` として保存しておくと、
`python3 docs/decisions/004-ga-activate.py G-XXXXXXXXXX` で実行できる。

### 4. 確認

```bash
# アクティブなGAスニペットが17ファイル全部にあることを確認
grep -rl "gtag('config'" . --include="*.html" | grep -v _template | wc -l
# → 17 であればOK

# GA_MEASUREMENT_ID プレースホルダーが残っていないことを確認
grep -r "GA_MEASUREMENT_ID" . --include="*.html" | grep -v _template
# → 出力なしであればOK
```

### 5. コミット

```bash
git add .
git commit -m "Google Analytics を有効化 (${MEASUREMENT_ID}) fixes #6"
```

## 対象ファイル（17ファイル）

| ファイル | 種別 |
|---|---|
| index.html | ポータル |
| privacy.html | プライバシーポリシー |
| contact.html | お問い合わせ |
| disclaimer.html | 知的財産権 |
| connect4/index.html | ゲーム |
| connections/index.html | ゲーム |
| dice-gomoku/index.html | ゲーム |
| egg/index.html | ゲーム |
| hex/index.html | ゲーム |
| hive/index.html | ゲーム |
| noccanocca/index.html | ゲーム |
| onitama/index.html | ゲーム |
| ostle/index.html | ゲーム |
| quantik/index.html | ゲーム |
| quridor/index.html | ゲーム |
| the-ONE/index.html | ゲーム |
| vidro/index.html | ゲーム |

## 注記

- `_template/index.html` はGA不要のため対象外
- onitama / vidro はフォントが `@import` 形式のため、GAブロックは `<title>` 直後・`<style>` 直前に配置
- 他14ファイルはフォント `<link>` 直後・`<style>` 直前に配置
