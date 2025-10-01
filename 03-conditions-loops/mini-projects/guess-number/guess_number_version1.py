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