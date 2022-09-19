import re
import pandas as pd

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

# 使う正規表現
r_del_str = r"(^\d*d$|^\d*h$)"
r_follow = r" followed.*"
r_cheered = r" cheered.*"
r_subscribed = r" has subscribed.*"
r_raided = r" raided.*"

# 使う配列
l_all = []
l_follow = []
l_cheered = []
l_cheered_sum = []
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
    cheer_sum(l_cheered)

def find_subscribed(l_str):
    # print("==== subscribed ==============")
    for s in l_str:
        pattern = re.compile(r_subscribed)
        s_subscribed = pattern.search(s)
        if bool(s_subscribed):
            # print('[DEBUG]: ' + s)
            name = re.sub(r_subscribed, "", s)
            l_subscribed.append(name)
    l_subscribed.sort(key = lambda s: len(s))


def find_raided(l_str):
    # print("==== raided ==============")
    for s in l_str:
        pattern = re.compile(r_raided)
        s_raided = pattern.search(s)
        if bool(s_raided):
            name = re.sub(r_raided, "", s)
            l_raided.append(name)
    l_raided.sort(key = lambda s: len(s))

    
def cheer_sum(s_cheers):
    """
    重複してcheerしてくれた方のビッツの数を合算させる
    """
    colum = ["name", "value"]
    df = pd.DataFrame(data=s_cheers, columns=colum)
    d_sum = df.groupby('name').sum().to_dict()["value"]
    for n in list(d_sum.keys()):
        s = n + "(" + str(d_sum[n]) + ")"
        l_cheered_sum.append(s)
    

def all_print(l_items):
    """
    収納した情報をここにて欲しい形に修正して出力する
    """
    l_title = [ "フォロー", "ビッツ", "サブスク(ギフト)", "レイド"]
    for i, l_resultl in enumerate(l_items):
        print("# " + l_title[i])
        for s in l_resultl:
            print("- " + str(s))
        print("")


with open("./test.txt") as f:
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
find_raided(l_all)
print("==== Print Start==================")
l_result = [l_follow, l_cheered_sum, l_subscribed, l_raided]
all_print(l_result)

