# 目的
- クリップを「誰が」「何回」交換してくれたかを集計する

## 注意
- クリップ自体をクリックすると展開されてしまうので、PCより一番右をダブルクリックすることで、そこのクリップより上全てのクリップを選択する

# 使い方_備忘録
## 前提
- python3が使用できる方向け
- コピー元のテキストが日本語

## 手順
### 1. MyTwitchダッシュボードから「コンテンツ > クリップ」をクリック
<img src="" width=800>


### 2. 「自分のチャンネルのクリップ」をクリック
<img src="" width=800>

### 3. 展開しないように１ヶ月分のクリップを選択し、集計したい範囲のデータを選択（ドラッグ）しコピーする
<img src="" width=800>

### 3. メモ帳（拡張子：.txt）などエディターでコピーした文字列をペーストして「」というファイル名で保存する（プログラムと同じフォルダに配置すること）
<img src="" width=800>


### 4. プログラムを実行する
<img src="" width=800>


### 5. 「====」と「====」内の必要な情報を任意の用途で使用する（例：感謝カードに記名）
  - 左側が「アカウント名」で右側の()内が「クリップ作成回数」を表す 
> ```py
> minimim45(4)
> なちこちゃん(1)
> 圭一ちゃん(1)
> ```
