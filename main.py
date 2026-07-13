#
# テストコード3
#
from sum import sumClass as sc # この文を追加して読み込み

# メイン関数
def main():
	sumInstance = sc.SumClass() # scという名前にしたのでそこでインスタンス関数を呼び出す
	print("---start---")
	sumInstance.sumLoop()
	print("---end---")

if __name__ == '__main__':
    main()