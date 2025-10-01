"""
功能：在1-10中随机挑选一个整数并给用户三次机会猜测该数字，猜测错误会提示相比答案大了还是小了
输入：用户输入1-10整数最多三次机会
输出：用户输入1-10整数时进入游戏一共可以猜测3次并提示猜大了还是小了，猜对给出提示胜利猜错显示机会耗尽失败
"""



def guess_numbers():
    import random
    num = random.randint(1, 10)
    a = int(input("please input the number:"))
    if a > num:
        print("the number you guessed is greater than the number")
        b = int(input("one more chance:"))
        if b > num:
            print("the number you guessed is greater than the number")
            b = int(input("one more chance:"))
            if b > num:
                print("u failed")
            elif b < num:

                print("u failed")
            else:
                print("u got the right number")
        elif b < num:
            print("the number you guessed is less than the number")
            b = int(input("one more chance:"))
            if b > num:
                print("u failed")
            elif b < num:
                print("u failed")
            else:
                print("u got the right number")
        else:
            print("u got the number")
    elif a < num:
        print("the number you guessed is less than the number")
        b = int(input("one more chance:"))
        if b > num:
            print("the number you guessed is greater than the number")
            b = int(input("one more chance:"))
            if b > num:
                print("u failed")
            elif b < num:
                print("u failed")
            else:
                print("u got the right number")
        elif b < num:
            print("the number you guessed is less than the number")
            b = int(input("one more chance:"))
            if b > num:
                print("u failed")
            elif b < num:
                print("u failed")
            else:
                print("u got the right number")
        else:
            print("u got the number")
    else:
        print("u got the right number")
if __name__ == "__main__":
    guess_numbers()
