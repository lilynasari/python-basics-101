- **变量：**  
       1.不可以使用python中的关键字  
        eg：class_name="Python"  
       2.不出现大写英文
-  **字符串：**  
       1.与数字拼接要转换  
         eg：name=“Alice”  
             age=19  
             print(f"{name} is {age} years old")    
        2.精确到小数点时%后小数点前时宽度后为留下小数点后几位，会进行四舍五入  
          eg：factor=2.1111  
              print('daily factor%2.1f"%factor)  
              则会输出：  
              daily factor2.1  
 - **输入：**  
        1.输入数据类型均为字符串需要转化为整数或者浮点数形式    
          eg：a=int(input("input a:"))  
 - **运算符:**  
         1.%是取余//是取整  
         2.区分==（等于号）和=(将右边的值赋给左边）  
 - **if循环：**  
         1.if后要有冒号缩进四格  
         2.if语句中执行完if或者elif或者else将直接退出循环  
         3.在if语句中判断ValueError或者TypeError永远为真  
  - **while循环:**  
         1.while语句中包含变量避免死循环（存在退出条件）
  - **for循环**    
         1.基本格式：for 临时变量 in 待待处理数据集（序列类型）    
         2.关于range：默认step为1，为一个[0,x)的集合  
  - **输出格式**  
         1.print语句输出自动换行，取消自动换行需要在输出语句末尾加，end=''  
         2.print(" ") 即可打出空格  
         3.print内容要上下对齐则在语句的""中加入\t
  - **函数**  
         1.函数的定义  
           def 函数名（传入参数（可省略））：    
                函数体    
                return 返回值（可省略返回值）    
         2.调用语法：函数名（参数）    
         3.传入参数：  
                 作用：使函数从外部接受参数进行调用  
                 注意：参数之间用逗号分隔，定义形式参数调用时提供实际参数  
            eg：def add(x,y):    
                    result=x+y    
                    print(f"{x}+{y}={result})    
                add(5,6)    
          4.返回值：        
                作用：函数完成内容后给调用者的一个结果    
                注意：函数遇到return之后就会结束  
          5.none类型    
                作用：返回none即返回内容为空    
                      (1)用于if判断时：none=false  
                                   eg:def check_age(age):  
                                          if age>18:  
                                               return "SUCCESS"  
                                          else:  
                                               return None  
                                       result=check(age)  
                                       if not result    
                                           #not result即表示true因为none表示false  
                                           print(sorry u can't get in)  
                        (2)用于声明无初始内容的变量：在变量定义时先标记为none表示暂时不提                              供值后续在进行处理。  
    
                注意：eg：return None    
            
                      
           
        
      
