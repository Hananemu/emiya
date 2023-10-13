from libs.event.qqvent import oncommand
import random
random_sum=random.randint(-100,100)#随机生成一个负一百到一百的整数
@oncommand(promat=["","/"],cmd=["猜",“c”])
def handle(n)
    num=n.arg
    num=int(n.arg)
    if num>sum:
      send(n.groud_id,text=("你猜大了!"))
    elif num<sum:
      send(n.groud_id,text=("你猜小了!"))
    else if num==sum:
      send(n.groud_id,text=("你猜对了！"))
    random_sum=random.randint(-100,100)
