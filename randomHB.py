#_*_ coding:utf-8 _*_
import random

def redPocket(people,money):
    result=[]
    remain=people
    max_money=money/people*2
    for i in range(people):
        remain-=1
        if remain>0:
            m=random.randint(1,min(money-remain,max_money))
        else:
            m=money
        money-=m
        result.append(m/100)
    return result

people=int(input('红包个数:\n'))
money=int(input('总金额:\n')*100)
print(redPocket(people,money))
