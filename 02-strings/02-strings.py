"""
功能：定义公司股票价格和日增长及增长天数并输出股票具体信息及增长情况
输入：暂无
输出：利用字符串拼接的股票具体细节信息
"""


def strings():

    name = "传智播客"
    stock_code = "003032"
    stock_prise = 19.99
    stock_price_daily_growth_factor = 1.2
    growth_days = 7
    print("company:" + name +
          ",the stock number:" +
          stock_code +
          ",the present price:" +
          f"{stock_prise}")
    stock_prise *= stock_price_daily_growth_factor ** growth_days
    print("daily growth factor:%2.1f" % stock_price_daily_growth_factor +
          "after %1d days' increasing" % growth_days +
          "the price reached up to:%4.2f" % stock_prise)
if __name__ == "__main__":
    strings()