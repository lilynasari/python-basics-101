"""
功能:通过绩效判断来进行对20位员工薪水的发放
输入：员工输入自己的绩效
输出：当绩效小于5显示低于5所以不发放薪水，当绩效大于等于5发放1000元薪水并显示账户剩余余额
     在没有薪水剩余时显示没有
"""




def company_salary():
    account=10000
    worker=1
    for i in range(20):

            if account>=1000:
                point = int(input(f"worker{worker}, enter your point:"))
                if point>=5:
                    account-=1000
                    print(f"worker {worker} ,get 1000yuan,the account have {account} left")
                    worker += 1
                else:
                    print(f"worker {worker} ,point:{point},below 5,no salary")
                    worker+=1
                    continue
            else:
                print("no salary left")
                break

if __name__ == "__main__":
    company_salary()