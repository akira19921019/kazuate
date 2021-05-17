class Game:

# フィールド
    level = True    # レベルの判定
    keta = 0        # 桁数
    kaisuu = 0      # 正解までにかかった入力回数
    answer = ''     # 答え
    scanU = 0       # 入力した数字

# コンストラクタ(レベル設定～答えの生成)
    def __init__(self):

        while self.level == True:

            print('難易度を設定してください')
            print('[ 1:EASY  2:NORMAL  3:HERD ]')
            num = input()

            if num.isdecimal():
                self.keta = int(num)+1

            if self.keta == 2:
                print('【難易度[EASY]でゲームを開始します】')
            elif self.keta == 3:
                print('【難易度[NORMAL]でゲームを開始します】')
            elif self.keta == 4:
                print('【難易度[HERD]でゲームを開始します】')
            else:
                print('【エラー：そんなレベルはありません】')
                continue

            # 答えの生成
            while len(self.answer) != int(self.keta):
                import random
                ans = random.randint(1,9)
                if str(ans) in self.answer:
                    pass
                else:
                    self.answer += str(ans)

            self.level = False
            break


# 入力メソッド
    def scan(self):
        print()
        print('{}桁の数字を入力してください'.format(self.keta))
        print('但し各桁ごとに1～9の範囲であること')
        self.scanU = input()

# 入力チェックメソッド
    def check(self):

        if '0' in self.scanU:
            return '【エラー：入力された数字に0が含まれています。】'

        elif len(self.scanU) != self.keta:
            return '【エラー：入力された数字が{}桁ではありません。】'.format(self.keta)

        else:
            self.kaisuu += 1
            return '↓'

# ゲームメソッド
    def game(self,an,sc):

        bubunn = 0        # 部分正解数
        oshii = 0         # おしい数

    # 部分正解、おしい数があるか見てみる
        for i in range(int(self.keta)):
            for j in range(int(self.keta)):

                # 部分正解
                if an[i] == sc[i]:
                    bubunn += 1
                    break
                # おしい数
                elif an[i] == sc[j]:
                    oshii += 1

    # でどうだったか・・・
        if bubunn == self.keta:
            print('正解です。正解までにかかった回数{}回'.format(self.kaisuu))
            return False   # 正解
        else:
            print('部分正解{}つ、おしい数字{}つ'.format(bubunn,oshii))
            return True    # 不正解
