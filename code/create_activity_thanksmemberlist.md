# 目的
- 特定（ビッツ、フォロー、サブスク、サブスクギフト、レイド）のアクティビティの名前を一覧化する

## 注意
- とくにあるかな...？しらんけども

# 使い方_備忘録
## 前提
- python3が使用できる方向け
- コピー元のテキストが英語表記

## 手順
### 1. [StreamEements](https://streamelements.com/dashboard/activity)の[Data&reports]>[ActivityFeed]に移動する
<img src="https://user-images.githubusercontent.com/113818239/192728095-e93316dd-2bda-4e80-bb79-d321c668e477.png" width=800>

### 2. 集計したい範囲のデータをコピーする
<img src="https://user-images.githubusercontent.com/113818239/192728468-2ab60e91-3ca9-4542-80bf-b2dea83a14f5.png" width=800>

### 3. メモ帳（拡張子：.txt）などエディターでコピーした文字列をペーストして「twitch_yyyymmdd」というファイル名で保存する（プログラムと同じフォルダに配置すること）
  - ファイル名の「yyyyは年・mmは・ddは日」を表し、実行する日の年月日を入れてください（2022年9月28日なら9月を0埋めして「20220928」になります）
<img src="https://user-images.githubusercontent.com/113818239/192729040-8c2129a1-fa0e-439b-b9ea-ee1dae564d82.png" width=800>


### 4. プログラムを実行する
<img src="https://user-images.githubusercontent.com/113818239/192729451-f75b98a1-9e01-4890-bf4d-aced027658bd.png" width=800>

### 5. 「====」以下の必要な情報をコピーし任意の用途で使用する（例：感謝カードに記名）
  - 今回はビッツとサブスク（ギフト）の情報はフィルターにて除外してスクショと集計元データとしています
  - ビッツに関しては名前の横の()が合計額、ギフトに関しては名前の横の()が合計ギフト回数になります
```md
==== Print Start==================
# フォロー
- しゃるル
- しらぴドットコム
- noemalibri
- a_person1379
- KamiNashiOjisan

# ビッツ

# サブスク
## サブスクギフト

# レイド
- さおまる
- azarashi009
```
