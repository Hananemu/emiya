#coding:gbk
from libs.event.qqvent import oncommand
import random
import requests
BASEURL = "http://127.0.0.1:5700"
def send(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    requests.post(f"{BASEURL}/send_group_msg", data=d)
    
sum=random.randint(-100,100)#随机生成一个负一百到一百的整数
@oncommand(promat=["@","/"],cmd=["猜",“c”])
def handle(n):
    send(text="开始游戏啦",gid=n.group_id)
    
    num=n.arg
    try:
        num=int(n.arg.replace(" ",""))
    except Exception as e:
        send(n.group_id,e)
        return
        
    
    if num>sum:
      send(n.groud_id,text="你猜大了!")
    elif num<sum:
      send(n.groud_id,text="你猜小了!")
    else if num==sum:
      send(n.groud_id,text="你猜对了！")
      sum=random.randint(-100,100)
