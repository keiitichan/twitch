import re
import collections


def all_print(l_items):
    """
    チャンネルポイントを交換してくれた人たちを表示する
    """
    print("[INFO]: START: チャンネルポイント報酬リクエストを交換してくれた人一覧")
    print("============================================\n")
    for s in l_items:
        print(s)
    print("\n============================================")
    print("[INFO]: END")
    print("[INFO]: 上記の結果をコピーしてご自由にお使いください")


def delete_str(l_items, bool_messege):
    """
    日付とコメントを削除する処理
    コメントについては、実行時の質問の解答により削除するかしないかの判断を行う
    """
    bool_deleteline = False
    for i, s in enumerate(l_items):
        if bool_deleteline:
            # 「17 日前」などの日付の後に存在するユーザーからの任意のコメントをする処理
            bool_deleteline = False
            continue
        if bool(re.search(r_del_str, s)):
            s = re.sub(r_del_str, '', s)
            if bool_messege:
                bool_deleteline = True
            continue
        l_exclusiondata.append(s)


def delete_blankline():
    with open(filename) as f:
        # print('\n'.join(map(str, f)))
        count = 1
        for s in f:
            """
            改行と日付と時刻を除いた文字列を削除
            """
            # ３種類の改行を無くす
            s = re.sub(r'(\r\n|\r|\n)', '', s)
            if not (bool(s)):
                # Falseの場合次へ
                continue
            l_all.append(s)
            count += 1


def delete_batchname(l_items):
    for s in l_items:
        for r in l_r_del_str:
            p = re.compile(r)
            s = p.sub("", s)
        l_members.append(s)


def counter_exchanges(l_members):
    """
    名前とその人が交換した回数の辞書を文字列に変換し、配列に追加する
    辞書の時点で回数を多い順にソートする処理を行う
    """
    members_counter = collections.Counter(l_members).items()
    cp_rank_menmers = sorted(members_counter, key=lambda x: x[1], reverse=True)
    for n, c in cp_rank_menmers:
        l_result.append(n + "(" + str(c) + ")")


def quession_messege():
    while True:
        print(("[INFO] この処理は特定のチャンネルポイントの報酬リクエストを交換した人の一覧化をし、"
               "その回数を名前の横に(n)で表示する処理です\n"))
        print("[INFO] 今回集計するチャンネルポイント（以後、チャネポ）はメッセージを入力しないといけないものですか？")
        print("[INFO] メッセージ入力するチャネポの場合　　：「yes」or「y」")
        print("[INFO] メッセージ入力しないチャネポの場合　：「no」or「n」\n")
        choice = input("> ")
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            continue


def main():
    bool_messege = quession_messege()
    delete_blankline()
    delete_str(l_all, bool_messege)
    delete_batchname(l_exclusiondata)
    counter_exchanges(l_members)
    all_print(l_result)


if __name__ == "__main__":
    filename = "channelpoint.txt"
    l_all = []
    l_exclusiondata = []
    l_members = []
    l_result = []
    r_del_str = r"(^\d+ 時間前|^\d+ 日前|^..?日|^.月)"
    # 必要に応じてバッチの名前を以下の配列に追加してください.
    l_r_del_str = [r"モデレーター",
                   r"(\d+-Month Subscriber|\d+ヵ月サブスクライバー)",
                   ",",
                   r"cheer \d*",
                   r"ビッツリーダー\d?",
                   "VIP",
                   "ファウンダー",
                   "Artist",
                   r" \(.*\)",
                   "Prime Gaming",
                   "ストリーマー",
                   "サブスクギフター",
                   "サブスクライバー"
                   ]
    main()
