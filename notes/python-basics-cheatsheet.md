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
    
                
      
