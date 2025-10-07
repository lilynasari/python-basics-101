"""""
功能：输出一张九九乘法表
输入：无
输出：九九乘法表
"""
def multiplication_form():
    a=1
    while a<=9:
        b=1
        while b<a:
            print(a,"*",b,"=",a*b,"\t",end='')
            b+=1
        print(a,"*",a,"=",a*a)
        a+=1
if __name__ == "__main__":
    multiplication_form()