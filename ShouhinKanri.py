class product:
    """商品クラス"""

    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

    def display(self):
        """商品情報を表示"""
        print("商品コード: " + self.code)
        print("商品名: " + self.name)
        print("価格: " + str("{:,}".format(self.price)) + "円")

    def discount(self, rate):
        """割引価格を計算する"""
        discounted_price = int(self.price * (1 - rate))
        return discounted_price


# ---------------------------------------
# メイン処理
# ---------------------------------------

# 商品を作成（インスタンス処理）
product1 = product("A001", "ノートパソコン", 100000)
product2 = product("A002", "スマートフォン", 50000)
product3 = product("A003", "タブレット", 30000)

# リストで管理
products = [product1, product2, product3]

#　商品情報を表示
print("商品情報一覧")
print("-" * 30)

for product in products:
    product.display()
    print(f"10%割引価格: :{"{:,}".format(product.discount(0.1))}円")
    print("-" * 30)
