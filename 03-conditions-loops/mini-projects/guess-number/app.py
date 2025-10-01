"""
功能：在1-10中随机挑选一个整数并给用户三次机会猜测该数字，猜测错误会提示相比答案大了还是小了以及还剩几次机会，在输入不符合规范时要求重新输入
输入：用户输入整数小数或者字符
输出：用户输入1-10整数时进入游戏一共可以猜测3次并提示猜大了还是小了以及还有几次机会，用户输入错误内容时捕捉错误并让其重新输入，
"""
def get_num():
    a=0
    while True:
        try:
            a=int(input("please input the number between 1 and 10:"))
        except ValueError:
            print(f'a is invalid')
        except :
            print('except')
        else:
            if a<1 or a>10:
                pass
            else:
                return  a

def play_game():
    import random
    num = random.randint(1, 10)
    chance = 0
    while chance < 3 :
        a = get_num()

        if a > num:
           print("the number u guess is greater than the number")
        elif a < num:
          print("the number u guess is less than the number")
        else:
            print("you got the right number")
            break
        chance += 1
        chance_left = 3 - chance
        print(f" you have {chance_left}  times")
    if chance >= 3:
        print("u failed")
if __name__ == "__main__":
    play_game()