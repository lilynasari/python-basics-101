"""
功能:模拟银行ATM机的功能可以进行取款存款以及查询余额的操作会在开始时要求输入名字然后输入操作业务可以进行反复操作直到主动退出
输入：所要操作的业务，存款额度，取款额度，确认操作
输出：开始部分打招呼询问所要查询业务内容，查询业务输入不符合规范报错
     存款部分输出存款金额所剩余额
     取款部分当有足够的钱时输出取款金额余额
            当余额不足报错
     在每个操作结束确认是否无误要是错误要求联系工作人员。
"""
balance=0
name=0

def deposit():
    deposit_money = int(input("enter your deposit:"))
    global balance
    balance+=deposit_money
    print(f"hello,u deposit {deposit_money} yuan successfully")
    print(f"your balance is {balance}")


def withdrawal():
    withdraw_money=int(input("enter your withdrawal:"))
    global balance
    if withdraw_money>balance:
        print("sorry you don't have enough money")
    else:
        balance -= withdraw_money
        print(f"hello,u withdraw {withdraw_money} yuan successfully")
        print(f"your balance is {balance}")

def introduction():
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
        if number==1:
            print("your balance is ",balance)
            q=input("if it's right? plz enter confirm or problems:")
            if q=="confirm":
                continue
            else:
                print("please contact us")
        elif number==2:
            deposit()
            q = input("if it's right? plz enter confirm or problems:")
            if q == "confirm":
                continue
            else:
                print("please contact us")
        elif number==3:
            withdrawal()
            q = input("if it's right? plz enter confirm or problems:")
            if q == "confirm":
                continue
            else:
                print("please contact us")
        elif number==4:
            break
        else:
            print("please enter correct number")
            continue
    print("you are welcome")
if __name__ == "__main__":
    introduction()

