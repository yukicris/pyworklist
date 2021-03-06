# 数据类型

# 1 整型,长度不受限制,只限于计算机虚拟内存总数
a = 100

# 2 浮点型,可以使用科学计数法(E计法)
b = 0.0000000015
# 等效于1.5e-9

# 3 布尔类型,true等于1,false等于0,可以用于运算,不过false不能做分母;int()把浮点数转换为整数,直接截断处理
True+True
int(0.005)

# 4 获取数据类型 用type(),判断两个数据是否为同一类型 用isinstance(a,b)
type(0.01)

# 5 运算,除法有个双除法,作用是取整数
3/2
3//2

# 6 幂运算3**2=9=3*3,幂运算优先级比左侧一元操作符高,比右侧一元操作符低;-3**2=-9   3**-2=0.111111111
3**2

# 6 3<4<5 合法,被解释为3<4 and 4<5