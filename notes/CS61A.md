**LECTURE 1**  
- 导入函数库：  
   形式：from 库名称 import 对应函数  
   基本库类型：  
       math：数学函数  
       operator：中缀运算符 eg：+ -...

**LECTURE2**  
- 赋值：为一次性的作用不会在之后进行同步  
        特殊地（函数覆盖为新的函数同理），在对原本python库中存在的函数进行赋值之后的该函数原本内  容      被覆盖（可以通过del删除）   
        eg：max=7               
            f=max  
            print(max，end'')  
            del max  
            print(max(2,3))  
            输出：73  
 - how to bind name and value：  
          WAY1：from.... import...  
          WAY2:赋值  
          WAY3:def ....():  
 - 函数与变量的区别:函数在调用时重新更新计算的数据，变量不会  
          
                        
       
    
