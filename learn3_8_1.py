# 把2.1的程序优化一下
"""---第一个小程序---"""
import random
secret = random.randint(0,10)
temp = input("猜猜我想的什么数字:")
guess = int(temp)
while guess!=secret:
    temp = input("小树苗猜错啦,再给你一次机会:")
    guess = int(temp)
    if guess == secret:
        print("真是我可爱的小树苗")
    else:
        print("猜错啦")
print("不玩啦~~")