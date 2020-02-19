shang_pin_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}
for k, v in shang_pin_info.items():
    print("商品ID：%d，名称：%s，价格：%d" % (k, v["name"], v["price"]))


class CommodityModel:
    def __init__(self, id=0, name="", price=0, number=0):
        self.id = id
        self.name = name
        self.price = price
        self.number = number


class CommodityManagerView:
    def __init__(self):
        self.__manager = CommodityController()

    def __display_menu(self):
        print("1键添加商品")
        print("2键显示购物车")
        print("3键删除商品")
        print("4键结算")
        print("5键清空购物车")

    def __select_menu(self):
        num = input("请输入选项：")
        if num == "1":
            self.__input_products()
        elif num == "2":
            self.__show_product()
        elif num == "3":
            self.__delete_products()
        elif num == "4":
            self.__buy_products()
        elif num == "5":
            self.__clear_product()
        else:
            print("输入有误")
            self.main()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_products(self):
        id = int(input("请输入商品ID："))
        number = int(input("请输入商品数量："))
        result = self.__manager.add_product(id, number)
        if result:
            print("添加成功")
        else:
            print("添加失败")

    def __show_product(self):
        for i in self.__manager.list_product:
            print("商品ID：%d，名称：%s，价格：%d，数量：%d" % (i.id, i.name, i.price, i.number))

    def __delete_products(self):
        product_id = int(input("需要删除的商品ID："))
        delete_number = int(input("输入删除的数量："))
        result = self.__manager.remove_products(product_id, delete_number)
        if result:
            print("删除成功")
        else:
            print("删除失败")

    def __buy_products(self):
        result = self.__manager.calculate_total_money()
        print("总价为：", result)
        while True:
            paid = int(input("付多少钱？"))
            money_change = self.__manager.purchase_products(paid, result)
            if money_change < 0:
                print("金额不足")
            else:
                print(f"应找回{money_change}元。")
                self.__manager.list_product.clear()
                break

    def __clear_product(self):
        self.__manager.remove_all_products()


class CommodityController:
    def __init__(self):
        self.__list_product = []

    def add_product(self, id, number):
        for key in shang_pin_info:
            if key == id:
                product = CommodityModel(key, shang_pin_info[key]["name"], shang_pin_info[key]["price"], number)
                if not self.__list_product:
                    self.__list_product.append(product)
                    return True
                for i in self.__list_product:
                    if i.id == id:
                        i.number += number
                    else:
                        self.__list_product.append(product)
                        return True
        return False

    @property
    def list_product(self):
        return self.__list_product

    def remove_products(self, product_id, delete_number):
        for i in self.__list_product:
            if i.id == product_id:
                if delete_number > 0:
                    i.number -= delete_number
                    if i.number <= 0:
                        self.__list_product.remove(i)
                        return True
                    return True
                return False
        return False

    def calculate_total_money(self):
        total_price = 0
        for i in self.__list_product:
            total_price += i.price * i.number
        return total_price

    def purchase_products(self, paid, result):
        return paid - result

    def remove_all_products(self):
        self.__list_product.clear()


view = CommodityManagerView()
view.main()
