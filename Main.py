from work.Game import Game

class Main:
    from work.Game import Game

# フィールド
    hantei = ''         # 入力数字の判定結果
    kekka = True        # ゲーム結果

    def __init__(self):
        pass

# ゲームメソッド
    def gameStart(self):
        # Gameインスタンス(レベル設定～答えの生成)
        game = Game()

        while self.kekka == True:           # 不正解(True)である限りゲームを繰り返す
            game.scan()                     # 数字入力
            self.hantei = game.check()      # 数字チェックの判定結果をhanteiに代入
            print(self.hantei)

            if self.hantei != '↓':          # 無効な数字であれば再度入力を促す
                continue

            else:                           # 有効な数字であればゲームスタート
                self.kekka = game.game(game.answer, game.scanU) # 答えと入力された数字を比較
                if self.kekka == False:     # 正解(False)なら
                    break                   # while文をbreakして終了

if __name__ == '__main__':
    m = Main()
    m.gameStart()
