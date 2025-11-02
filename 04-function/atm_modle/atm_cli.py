"""
功能:模拟银行ATM机的功能可以进行取款存款以及查询余额的操作会在开始时要求输入名字然后输入操作业务可以进行反复操作直到主动退出
输出：开始部分打招呼询问所要查询业
     存款部分输出存款金额所剩余额
     取款部分当有足够的钱时输出取款金额余额
            当余额不足报错
     在每个操作结束确认是否无误要是错误要求联系工作人员。
"""
balance=0
name=0

def init(b=0):
    global  balance
    global  name
    balance = b
    name = ""

#存钱业务模块=======================================================================================
def process_deposit(deposit_money:float)->float:
    """执行存钱业务逻辑
    """
    global balance
    balance+=deposit_money
    print(f"hello,u deposit {deposit_money} yuan successfully")
    print(f"your balance is {balance}")


def get_input_deposit_money():
    """执行存钱的输入获取
    """
    deposit_money = input("enter your deposit:")
    return deposit_money



def validate_amount_deposit(deposit_money_str):
    """执行存钱的输入校验"""
    # 1. 空串校验
    if not deposit_money_str.strip():
        return "空串错误"

    # 2. 非数字/非法格式校验（仅允许正数、最多2位小数）
    cleaned = deposit_money_str.replace(".", "")
    cleaned=cleaned.replace("-", "")
    if not cleaned.isdigit():
        return "非数字错误"

    # 3. 小数精度校验（最多2位）
    if "." in deposit_money_str and len(deposit_money_str.split(".")[-1]) > 2:
        return "精度过多错误"

    # 4. 金额范围校验（必须大于0，假设ATM单次操作上限10万）
    amount = float(deposit_money_str.strip())
    if amount <= 0:
        return "负数/零错误"
    if amount > 100000:
        return "金额超限错误"
    return "合法"

#取钱业务模块=========================================================================================
def process_withdrawal(withdraw_money:float)->float:
    """执行取钱的业务逻辑
    """
    global balance
    balance -= withdraw_money
    print(f"hello,u withdraw {withdraw_money} yuan successfully")
    print(f"your balance is {balance}")


def get_input_withdraw_money():
    """执行取钱的输入获取
    """
    withdraw_money =input("enter your withdrawal:")
    return withdraw_money


def validate_amount_withdraw(withdraw_money_str):
    """执行取钱的输入校验"""
    # 1. 空串校验
    if not withdraw_money_str.strip():
        return "空串错误"

    # 2. 非数字/非法格式校验（仅允许正数、最多2位小数）
    cleaned = withdraw_money_str.replace(".", "")
    cleaned = cleaned.replace("-", "")
    if not cleaned.isdigit():
        return "非数字错误"

    # 3. 小数精度校验（最多2位）
    if "." in withdraw_money_str and len(withdraw_money_str.split(".")[-1]) > 2:
        return "精度过多错误"

    # 4. 金额范围校验（必须大于0，假设ATM单次操作上限10万）
    amount = float(withdraw_money_str.strip())
    if amount <= 0:
        return "负数/零错误"
    if amount > 100000:
        return "金额超限错误"
    if amount>balance:
        return "余额不足"
    return "合法"

#确认环节=====================================================================================
def confirm():
    """用户确认银行业务执行正确
    """
    q = input("if it's right? plz enter confirm or problems:")
    if q == "confirm":
        return None
    else:
        print("please contact us")

#主要业务选择流程模块============================================================================
def main():
    """主要操作交互调用业务模块区域
    """
    global balance
    balance = 0
    number=0
    name = input("Hi,please enter your name:")
    print(f"hi {name},please choose your operation")
    while number!=4:

        print("inquiring balance:enter 1")
        print("deposit money:enter 2")
        print("withdrawal money:enter 3")
        print("get out:enter 4")
        number=int(input("enter your number:"))

        if number==1:    #查询余额
            print("your balance is ",balance)
            confirm()

        elif number==2:  #存钱
            while True:
                deposit_money_str=get_input_deposit_money()
                deposit_money_str_validate=validate_amount_deposit(deposit_money_str)
                if deposit_money_str_validate!="合法":
                    print(f"{deposit_money_str}")
                else:
                    deposit_money=float(deposit_money_str)
                    break
            process_deposit(deposit_money)
            confirm()


        elif number==3:  #取钱
            while True:
                withdraw_money_str =get_input_withdraw_money()
                withdraw_money_str_validate=validate_amount_withdraw(withdraw_money_str)
                if withdraw_money_str_validate!="合法":
                    print(f"{withdraw_money_str}")
                else:
                    withdraw_money=float(withdraw_money_str)
                    break
            process_withdrawal(withdraw_money)
            confirm()

        elif number==4:   #退出
            break
        else:
            print("please enter correct number")
    print("you are welcome")


# demo示例输入python atm_cli.py --demo运行
def demo():
    steps =[]
    steps.append("开始ATM 模拟程序")
    steps.append("Hi,please enter your name:")
    steps.append("sam")
    steps.append("hi sam gats,please choose your operation")
    steps.append('''
   inquiring balance:enter 1
deposit money:enter 2
withdrawal money:enter 3
get out:enter 4
enter your number:
''')
    steps.append("2")
    steps.append("enter your deposit:")
    steps.append("10000")
    steps.append("hello,u deposit 10000.0 yuan successfully")
    steps.append("your balance is 10000.0")
    steps.append("if it's right? plz enter confirm or problems:")
    steps.append("confirm")
    steps.append("""inquiring balance:enter 1
deposit money:enter 2
withdrawal money:enter 3
get out:enter 4
enter your number:""")
    steps.append("3")
    steps.append("enter your withdrawal:")
    steps.append("200")
    steps.append("hello,u withdraw 200.0 yuan successfully")
    steps.append("your balance is 9800.0")
    steps.append("if it's right? plz enter confirm or problems:")
    steps.append("confirm")
    steps.append("""inquiring balance:enter 1
deposit money:enter 2
withdrawal money:enter 3
get out:enter 4
enter your number:""")
    steps.append("4")
    steps.append("you are welcome")

    for step in steps:
        print(step)
        time.sleep(3)
if __name__ == "__main__":
    main()

