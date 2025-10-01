"""
功能：通过设点三个变量计算超市购买找零数目
输入：交付金钱50元可乐5元冰淇淋10元
输出：钱包余额，可乐冰淇淋花费价钱及剩余钱
"""
def variables():
    money = 50
    icecream = 10
    cola = 5
    print("当前钱包余额：", money)
    money = money - icecream
    print("购买了冰淇淋，花费：", icecream)
    money = money - cola
    print("购买了可乐，花费：", cola)
    print("total last:", money)
if __name__ =="__main__":
    variables()



