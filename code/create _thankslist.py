import re
import pandas as pd
import collections
import datetime

# 今日の日付のファイルのみに反応して動く様に設定しています。
d_today = datetime.date.today()
date_yyyymmdd = d_today.strftime('%Y%m%d')
# 現在のファイル名の想定は「twitch_20220922.txt.」など
# 整形する対象ファイル名を" "内に記載します
filename = "./twitch_" + date_yyyymmdd + ".txt"
print(filename)

"""md
# 説明
  StreamElementsに存在する「ビッツ、フォロー、レイド、サブスク」をしてくれた人に
  thanksメッセージを送る前の、メンバー一覧を作成するプログラムです。
  同じディレクトリに存在するテキストファイルの内容を読み取り、必要な情報のみを抽出します。
  別ファイルに書き込むなどの処理はしていません。
  とりあえず、形として即席でコンソール結果からコピペして一覧取得できるようにしただけです
# 想定するテキスト
  - フォロー：* followed your channel!
  - サブスク：has resubscribed (*) for * months (* month streak)
            has subscribed to you (Tier *)
  - レイド　：* raided your channel with * viewers!
  - ビッツ　：* cheered * bits!
"""


r_del_str = r"(^\d*d$|^\d*h$)"
r_follow = r" followed.*"
r_cheered = r" cheered.*"
r_gifted = r" gifted.*!$"
r_subscribed = r"has [resubscribed|subscribed].*"
r_raided = r" raided.*"
# pat = re.compile(reg)

# 各配列を作成
l_all = []
l_follow = []
l_cheered = []
l_cheered_sum = []
l_gifted = []
l_subscribed = []
l_raided = []

def find_follow(l_str):
    # print("==== follow ==============")
    for s in l_str:
        pattern = re.compile(r_follow)
        s_follow = pattern.search(s)
        if bool(s_follow):
            # print(s)
            s_name = re.sub(r_follow, "", s)
            l_follow.append(s_name)
    l_follow.sort(key = lambda s: len(s))

def cheer_sum(s_cheers):
    """
    重複してcheerしてくれた方のビッツの数を合算させる
    """
    if bool(s_cheers):
        """
        cheerした人がいない時には実行されないようにしました。
        """
        colum = ["name", "value"]
        df = pd.DataFrame(data=s_cheers, columns=colum)
        d_sum = df.groupby('name').sum().to_dict()["value"]
        for n in list(d_sum.keys()):
            s = n + "(" + str(d_sum[n]) + ")"
            l_cheered_sum.append(s)


def find_cheered(l_str):
    # print("==== cheered ==============")
    for s in l_str:
        pattern = re.compile(r_cheered)
        s_cheered = pattern.search(s)
        if bool(s_cheered):
            name = re.sub(r_cheered, "", s)
            value = int(re.search(r'cheered\s(\d*)\sbits!', s).groups(0)[0])
            l_cheered.append([name,value])
    l_cheered.sort()
    print(bool(l_cheered))
    cheer_sum(l_cheered)
    

def find_gifted(l_str):
    """
    ギフトしてくれた人の名前だけを取得して配列に入れ、
    重複した数（ギフトしてくれた数）を名前のよこに括弧書きで記載する
    """
    # print("==== gifted ==============")
    gift_names = []
            
    for s in l_str:
        pattern = re.compile(r_gifted)
        s_gifted = pattern.search(s)
        if bool(s_gifted):
            reg = '(.*) gifted'
            gifted_name = re.findall(reg, s)[0]
            gift_names.append(gifted_name)
    gift_counter = collections.Counter(gift_names).items()
    for n, c in gift_counter:
        l_gifted.append(n + "(" + str(c) + ")")


def find_subscribed(l_str):
    # print("==== subscribed ==============")
    for s in l_str:
        # print(s)

        pattern = re.compile(r_subscribed)
        s_subscribed = pattern.search(s)
        if bool(s_subscribed):
            # print('[DEBUG]: ' + s)
            reg = '(?<=\().+?(?=\))'
            sub_type = re.findall(reg, s)[0]
            name = re.sub(r_subscribed, "", s)
            sub_type = sub_type.replace(" ","")
            # elif len(ret) == 2: 
            if "for" in s:
                sub_str = re.search(r'for \d+ months',s).group()
                sub_total = re.findall(r'\s(\d+)\s', sub_str)[0]
                l_subscribed.append(name + "(" + sub_type + "/" + sub_total + "ヶ月)")
            elif not("for" in s):
                l_subscribed.append(name + "(" + sub_type + ")")
            else:
                print("[ERROR]: (" + name + ") サブスクライブの文字列で想定外のエラーが出力されました。(monthじゃない？)")


def find_raided(l_str):
    # print("==== raided ==============")
    for s in l_str:
        pattern = re.compile(r_raided)
        s_raided = pattern.search(s)
        if bool(s_raided):
            name = re.sub(r_raided, "", s)
            l_raided.append(name)
    l_raided.sort(key = lambda s: len(s))



def all_print(l_items):
    """
    三項演算子のelseで「continue」を使用できないため(ent="")で代用
    サブスクギフトとギフトの間は親子関係(# ,## )のようにしたいため、改行なしで表示する
    """
    l_title = [ "フォロー", "ビッツ", "サブスク", "サブスクギフト", "レイド"]
    for i, l_resultl in enumerate(l_items):
        if l_title[i] == "サブスクギフト":
            print("## " + l_title[i])
        else:
            print("# " + l_title[i])
        for s in l_resultl:
            print("- " + str(s))
        print("") if not(l_title[i] == "サブスク") else print("",end="") 


# with open("./test.txt") as f:
with open(filename) as f:
    # print('\n'.join(map(str, f)))
    count = 1
    for s in f:
        """
        改行と日付と時刻を除いた文字列を削除
        """
        # ３種類の改行を無くす
        s = re.sub(r'(\r\n|\r|\n)', '', s)
        s = re.sub(r_del_str, '', s)
        if not(bool(s)):
            # Falseの場合次へ
            continue
        l_all.append(s)
        count += 1
        
# find_*系の関数で必要な情報を取得する
find_follow(l_all)
find_cheered(l_all)
find_subscribed(l_all)
l_subscribed = list(set(l_subscribed)) # 応急処置: 重複するサブスクを削除
find_gifted(l_all)
find_raided(l_all)
print("==== Print Start==================")
l_result = [l_follow, l_cheered_sum, l_subscribed, l_gifted, l_raided]
all_print(l_result)
