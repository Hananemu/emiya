#coding:utf-8
from libs.event.qqvent import oncommand
import requests
BASEURL = "http://127.0.0.1:5700"
def sendGroupMessage(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    requests.post(f"{BASEURL}/send_group_msg", data=d)

@oncommand(promat=["","/"],cmd=["启动"])
def handle(n):
  try:
    sendGroupMsg(gid=n.group_id,text="Hello World!")
  except:
    pass
