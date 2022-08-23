
'''
str='123456789'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str * 2)             # 输出字符串两次
print(str + '你好')         # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
from pydoc import importfile


x='a'
y='b'
z="2"
str=12345698
print( x, end=" " )
print( y, end=" " )
print()
'''
'''
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python文件 路径为',sys.path)

from re import A
from socket import NI_NOFQDN
import sys
print ('-----------------')
print('命令行参数是')
for i in sys.argv:
    print(i)
print('\n python文件 路径为',sys.path) 
# 实在是不知道怎么写了
print{NI_NOFQDN}
str=1023513

from tokenize import Number


Number1=1.5
Number2=3.2

sum=Number1+Number2

print(f"{sum}")
'''
'''
num11=25
print('我最喜欢的数字是'+str(num11))
import this

print("%.2f"%(3.99*54.3365))
'''
''''''
#print("%.2f"%(4.6694*33.2))

'''
huashi=eval(input("华氏摄氏度:"))
sheishidu=(5/9)*(huashi-32)
print("对应的摄氏度:",format(sheishidu))
'''
'''
zhengshu1=eval(input("输入整数1:"))
zhengshu2=eval(input("输入整数2:"))
a=zhengshu1+zhengshu2
b=zhengshu1-zhengshu2
c=zhengshu1*zhengshu2
d=zhengshu1/zhengshu2
print(a,b,c,d)
'''
'''
整数1=eval(input("输入整数1:"))
整数2=eval(input("输入整数2:"))
a=整数1+整数2
print("%.2f"%(a))
'''
'''
宽度=eval(input("矩形的宽度是："))
长度=eval(input("矩形的长度是: "))
面积=宽度*长度
print("%.3f"%(面积))
'''
#计算三角形周长
'''
a,b,c=eval(input("请输入以逗号分隔的三角形的三条边长："))
cl=a+b+c
print("三角形的周长是：%.3f"%(cl))
'''
#计算三角形周长
'''
a,b,c=eval(input("请输入以逗号为分隔的三角形的三条边长："))
cl=a+b+c
if a+b>c:
      print("三角形的周长是%.2f"%(cl))
else:
    print("你输入的边长无法构成三角形")
'''
#列表元素增减

'''
bycile=["a","b","c","d"]
print(bycile)

bycile.append("e")     #末尾添加元素
print(bycile)

bycile[0]='f'
print(bycile)
'''
'''
import random
counts = 3
answer=random.randint(1,10)
while counts > 0 :
    temp= input("不妨猜一下正确的是哪个数：")
    guss=int(temp)

    if guss == answer :
        print('很棒哦')
        break

    else :
        if guss < answer:
            print('小了')
        else:
             print("大了")
    counts = counts - 1

print("游戏结束了")
'''
'''
import time
start = time.time()
n = 1202121
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为:%d" %(n,sum))
end = time.time()
print(end-start)
'''
'''
def get_jiecheng(m):

   ji=1
   while m>=1 :
    ji=ji*m
    m=m-1
   return ji

print("6的阶乘是:",get_jiecheng(6))
'''

'''
def mianji(r):
    s=3.14*r**2
    return s
print(mianji(5))
'''
'''
# 消息轰炸
# 微信、QQ皆可用
import itchat
import time
print("请扫描弹出的扫二维码")
itchat.auto_login(hotReload=True)
boom_name = input("请输入想发送的人：")
message = input("请输入发送的内容：")
number = int(input("请输入发送的次数："))
boom_obj = itchat.search_friends(remarkName=boom_name)[0]['UserName']

for i in range(1,number+1):
    time.sleep(0.01)
    print("正在发送第%d遍" %i)
    itchat.send_msg(msg=message,toUserName=boom_obj)
'''
'''

year=int(input("请输入一个年份："))
if year%4==0:
    print(year,"是闰年")
else:
    print(year,"不是闰年")

'''
'''
import random #随机数模块
anwser=random.randint(1,10) #随机生成一个1到10中的整数
m=1 #循环开始
while m<=3:
    number=int(input("请输入1到10中一个数，猜猜这个数是否等于答案")) 
    if number==8:
        print("答案正确！很棒哦！")
        break
    elif number > 8:
        print("大了")
    else :
        print("小了")
    m=m+1
#循环结束
print("游戏结束")

'''
# 素数


for n in range(2,11):
    for i in range(2,n):
        if n % i==0:
            print(n,"=",i,"*",n//i)
            break   # 用于循环体
    else:
         print(n,"是一个素数")
         