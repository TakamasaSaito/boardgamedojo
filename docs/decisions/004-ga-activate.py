#!/usr/bin/env python3
# GA 有効化スクリプト — 使い方: python3 docs/decisions/004-ga-activate.py G-XXXXXXXXXX
# 詳細: docs/decisions/004-ga-activation.md
import sys, glob

if len(sys.argv) != 2 or not sys.argv[1].startswith('G-'):
    print('使い方: python3 docs/decisions/004-ga-activate.py G-XXXXXXXXXX')
    sys.exit(1)

MEASUREMENT_ID = sys.argv[1]

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

print(str(len(updated)) + ' ファイルを更新しました:')
for f in sorted(updated):
    print('  ' + f)
