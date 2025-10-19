def pressure(v, t, n=6.022e23):
    """计算理想气体的压力，单位为帕斯卡

    使用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- 气体体积，单位为立方米
    t -- 绝对温度，单位为开尔文
    n -- 气体粒子，默认为一摩尔
    """
    k = 1.38e-23  # 玻尔兹曼常数
    return n * k * t / v
#学到的：在有些时候可以通过设置默认值使函数更易懂易于操作