from libs.event.qqvent import oncommand
import random
BASEURL = "http://127.0.0.1:5700"
def sendGroupMessage(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    requests.post(f"{BASEURL}/send_group_msg", data=d)
    
random_sum=random.randint(-100,100)#随机生成一个负一百到一百的整数
@oncommand(promat=["","/"],cmd=["猜",“c”])
def handle(n):
    sendGroupMessage(text="开始游戏啦",gid=n.group_id)
    
    num=n.arg
    num=int(n.arg)
    if num>sum:
      send(n.groud_id,text=("你猜大了!"))
    elif num<sum:
      send(n.groud_id,text=("你猜小了!"))
    else if num==sum:
      send(n.groud_id,text=("你猜对了！"))
    random_sum=random.randint(-100,100)
