# CS61A
## 1.2
### 1.2.3
````
- 导入函数库：  
   形式：from 库名称 import 对应函数  
   基本库类型：  
       math：数学函数  
       operator：中缀运算符 eg：+ -...
- 求解嵌套表达式：
    求值程序本质上是递归的，也就是说它会自己调用自己作为步骤之一
````
### 1.2.6
````
- 赋值：为一次性的作用不会在之后进行同步  
        特殊地（函数覆盖为新的函数同理），在对原本python库中存在的函数进行赋值之后的该函数原本内容被覆盖（可以通过del删除）   
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
   函数与变量的共同：def 语句和赋值语句都将名称与值绑定，并且绑定后任何之前的绑定都将丢失

````
## 1.3
### 1.3 info
````
- 基本格式:
  def <name>(<formal parameters>):
      return <return expression>
````
### 1.3.1

````
- 帧：局部帧：随函数（常见）生随函数灭
      全局帧：只有一个
      父帧（parent frame）：帧之间的上下级关系
- 环境：由帧序列组成
- 函数的名称：（1）内在名称（定义中出现的名称）：类似于底层的定义一定不变
             （2）绑定名称（帧中的名称）：调用时使用的名称，当该函数被赋值给另一个变量时存在函数调用名称变化的情况
- 函数的签名：对于函数的形参的描述
````
### 1.3.2
````
- 名称求解[第一步绑定在全局帧（或嵌套函数外函数局部帧）中进行]：在环境中寻找该名称，最早找到的含有该名称的帧，其里边绑定的值就是这个名称的计算结果。（先将遇到的名称绑定到在全局帧中定义的函数上）
- 调用函数[第二步绑定在局部帧中进行]：（1）插入一个新的帧并且创建一个新的环境执行函数体的内容
         （2）将实参绑定到形参上面
         （3）以新的帧开始在环境中进行操作
- 求解模型：环境，名称，函数三部分组成
````
### 1.3.4
````
- 基本原则：一个函数的含义应该与编写者选择的参数名称无关
  得到推论：形式参数的名称为局部名称作用域仅限于函数主体
````
### 1.3.6
````
- 函数抽象：
  概念：隐藏实现方式（被抽象掉）仅体现功能性
  三个方面：函数的域：接受参数的范围（类比定义域）
           范围：可以返回值的集合（值域）
           意图：输入和输出之间发生了什么->作用效果(及其他各类副作用eg：存在输出语句)
````
## 1.4
### 1.4.1
````
- 文档：
文档字符串（docstring）
1.基本要求：它必须在函数体中缩进。文档字符串通常使用三个引号，第一行描述函数的任务，随后的几行可以描述参数并解释函数的意图
eg：>>> def pressure(v, t, n):
        """计算理想气体的压力，单位为帕斯卡

        使用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

        v -- 气体体积，单位为立方米
        t -- 绝对温度，单位为开尔文
        n -- 气体粒子
        """
        k = 1.38e-23  # 玻尔兹曼常数
        return n * k * t / v
  2.调出方式：当你使用函数名称作为参数调用 help 时，你会看到它的文档字符串（键入 q 以退出 Python   help）
````
### 1.4.2
````
参数默认值：
将默认值绑定到形参a上，当未给出形参a的实参时则带入默认值进行计算
````
### 1.5.6
**测试：**
- 1.断言（Assertions）:assert fib(8)==13(该表达式存在于布尔上下文中)，（当表达式计算结果为假输出->）"the 8th number in fib should be 13"
当表达式计算值为真时：断言语句执行无效
..............假..：assert语句导致错误，程序不再执行

- 2.文档测试（doctests）:
````python
>>> from doctest import run_docstring_examples
>>> run_docstring_examples(sum_naturals, globals(), True)
Finding tests in NoName
Trying:
    sum_naturals(10)
Expecting:
    55
ok
Trying:
    sum_naturals(100)
Expecting:
    5050
ok
````
## 1.6
### 1.6.1
作为参数的函数，体现函数作为一个方法的思想
eg：
````python
>>> def summation(n, term):
        total, k = 0, 1
        while k <= n:
            total, k = total + term(k), k + 1
        return total
>>> def identity(x):
        return x
>>> def sum_naturals(n):
        return summation(n, identity)
>>> sum_naturals(10)
55
````
可以用完全相同的summation函数来对数列求和，只需调整形参位置的函数即可
### 1.6.2  
info：
作为通用方法的函数  
原本："用户定义函数"-->数值运算的抽象模式与**涉及的特定数字**无关  
拥有高阶函数之后：用函数表达**计算的通用方法**与其所**调用的特定函数**无关
1.通用表达式  
定义：不会指定要解决的具体问题，而是会将这些细节留给作为参数传入的函数。
eg：
````python
>>> def improve(update, close, guess=1):
        while not close(guess):
            guess = update(guess)
        return guess

>>> def golden_update(guess):
        return 1/guess + 1

>>> def square_close_to_successor(guess):
        return approx_eq(guess * guess, guess + 1)

>>> def approx_eq(x, y, tolerance=1e-15):
        return abs(x - y) < tolerance

>>> improve(golden_update, square_close_to_successor)
1.6180339887498951
````
在上例中的improve函数就是一个通用表达式  

### 1.6.3  
1.嵌套定义  
将函数定义放在另一个函数定义内  
2.词法作用域  
局部定义的函数可以访问整个定义作用域的名称绑定，嵌套定义之间共享名称  
**其中，内部函数可以访问定义它们的环境中的名称**





     





       
    
