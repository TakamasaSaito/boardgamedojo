# 003 サイコロ五目並べのスプラッシュ・howto フローを標準化対象外とする

- **日付**: 2026-07-30
- **決定者**: TakamasaSaito

## 決定内容

dice-gomoku/index.html のスプラッシュ〜howto 遷移フローは、
標準化（Issue #28-3 で確立した handleSplash() 相当）の対象外とし、
現行の独自実装を維持する。

将来 Issue #28 の続きとして是正するかどうかは、
そのタイミングで改めて判断する。

## 現行の独自設計

| 項目 | 標準 | dice-gomoku の実装 |
|---|---|---|
| スプラッシュ要素 | `.screen.active` クラス + `onclick` | `<div id="splashScreen">` — `.screen` クラスなし、タップ不可 |
| スプラッシュ終了 | ユーザーのタップ（handleSplash）+ 2.6s タイムアウト | `setTimeout` 2秒後に自動フェードアウト（ユーザー操作不要） |
| howto 遷移 | 初回のみ（`GAMENAME_seen` で判定） | 毎回表示（localStorage 判定なし） |
| スプラッシュ CSS | 標準 `.screen` の `display:none / flex` で切替 | 独自 CSS（`position:fixed; z-index:999`）+ `opacity` fade |

```javascript
// dice-gomoku/index.html の起動フロー（load イベント内）
applyLang();
showScreen('titleScreen');
setTimeout(function() {
  var sp = document.getElementById('splashScreen');
  sp.className = 'fade';
  setTimeout(function() {
    sp.className = 'gone';
    document.getElementById('app-header').classList.remove('hidden');
    prevScreen = 'titleScreen';
    showScreen('howtoScreen');  // 毎回 howto を表示
  }, 620);
}, 2000);
```

## 経緯

- Issue #26（テンプレート整備）の調査時、dice-gomoku が
  「初回判定（localStorage）を持つ実装例」として誤って言及された。
  実際には localStorage 判定は存在せず、当該記述は誤りだった。
- Issue #7（プライバシーポリシー作成）の調査でも「未使用」と報告されており、
  実態は「localStorage を使用しない」が正しい。
- Issue #28-3（標準化）ではこのゲームへの是正は行われなかった。
  標準化対象外であった経緯として本ドキュメントに記録する。

## 是正する場合の作業内容

1. `splashScreen` を `.screen.active` 方式に変更（他ゲームと統一）
2. `onclick="handleSplash()"` を追加し、2.6s タイムアウトと併用
3. `handleSplash()` 内で `dice_gomoku_seen` を判定し、
   - 初回: `showScreen('howtoScreen')` → 閉じると `titleScreen` へ
   - 2回目以降: `showScreen('titleScreen')` に直行
4. privacy.html の記載を 12/13 → 13/13 に更新
