def hangman(word):
    """
    ハングマン関数
    param word プレーヤー2に当てて欲しい単語
    author: otani
    since: 2021/07/17

    """

    # プレーヤー2が間違えた回数
    wrong = 0
    
    stages = ['',
              '                ',
              '--------        ',
              '|               ',
              '|       |       ',
              '|       O       ',
              '|     ／|＼     ',
              '|     ／ ＼     ',
              '|    　 :       ',
              '|       :       ',
              '----------------'
              ]

    # 答えなければいけない残りの文字に使用する
    rletters = list(word)

    # プレーヤー2に見せるヒント
    board = ['_'] * len(word)
    win = False
    
    print('[GK]ハングマンへようこそ！')

    while wrong < len(stages) - 1:
        print('\n')
        
        msg = '[P2]1文字予想してね'
        char = input(msg)

        if len(char) != 1:
            print('[P2]"1文字だけ"入力してね')
            continue

        if char in rletters:
            cind = rletters.index(char) # 一致する文字の先頭を返す
            board[cind] = char
             # 複数文字列一致する場合に後続文字を参照させるためコンバートする
            rletters[cind] = '$'
        else:
            wrong += 1

        print(' '.join(board))

        e = wrong + 1
        print('\n'.join(stages[0:e]))

        if '_' not in board:
            print('[P2]あなたの勝ち！')
            print(' '.join(board))
            win = True

            break

    if not win:
        print('\n'.join(stages[0 : wrong + 1]))
        print('[P2]あなたの負け！正解は {}.'.format(word))


word = input('[P1]単語を入力してね')
hangman(word)

    
