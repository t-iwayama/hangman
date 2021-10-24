import random

n = random.randint(0,5)
w = ["dog","cat","bird","inco","parrot","father"]
x = w[n]

def hangman(word):
    wrong = 0
    stages = ["",
                "______________     ",
                "|            |     ",
                "|            |     ",
                "|            0     ",
                "|            ハ    ",
                "|            ハ    ",
                "|                  "
                ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages)-1:
        print("\n")
        char = input("１文字を予想して入力してね：")

        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1

        print(" ".join(board))
        e = wrong +1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("あなたの勝ち！")
            #print("".join(board))
            print("正解は{}でした。".format(word))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け。正解は{}".format(word))



hangman(x)
