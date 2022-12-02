import re
import collections


def all_print(l_items):
    """
    事前にクリップを整理整頓している前提
    クリップしてくれた人と回数を表示する
    """
    print("[INFO]: START: クリップを作成してくれた人一覧")
    print("============================================\n")
    for s in l_items:
        print(s)
    print("\n============================================")
    print("[INFO]: END")
    print("[INFO]: 上記の結果をコピーしてご自由にお使いください")



def delete_blankline():
    with open(filename) as f:
        # print('\n'.join(map(str, f)))
        count = 1
        for s in f:
            """
            改行と日付と時刻を除いた文字列を削除
            """
            # ３種類の改行(と空白)を無くす
            s = re.sub(r'(\r\n|\r|\n)', '', s)
            if not (bool(s)):
                # Falseの場合次へ
                continue
            l_all.append(s)
            count += 1


def found_membername(l_all):
    for i, s in enumerate(l_all):
        print("[DEBUG] クリップのサムネ一覧")
        if s_foundword in s:
            print("[DEBUG] " + str(i) + ": " + s)
            num_membername = i + 2
            l_members.append(l_all[num_membername])

def counter_exchanges(l_members):
    """
    名前とその人が交換した回数の辞書を文字列に変換し、配列に追加する
    辞書の時点で回数を多い順にソートする処理を行う
    """
    members_counter = collections.Counter(l_members).items()
    cp_rank_menmers = sorted(members_counter, key=lambda x: x[1], reverse=True)
    for n, c in cp_rank_menmers:
        l_result.append(n + "(" + str(c) + ")")


def default_messege():
    print(("[INFO] この処理は特定のクリップ作成してくれた人を一覧化をし、"
           "その回数を名前の横に(n)で表示する処理です\n"))
    print("[INFO] 今回集計するチャンネルポイント（以後、チャネポ）はメッセージを入力しないといけないものですか？")


def main():
    default_messege()
    delete_blankline()
    print(l_all)
    found_membername(l_all)
    counter_exchanges(l_members)
    all_print(l_result)


if __name__ == "__main__":
    filename = "cliplist.txt"
    l_all = []
    l_exclusiondata = []
    l_members = []
    l_result = []
    s_foundword = "http"
    main()
