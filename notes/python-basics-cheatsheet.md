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
                
      
