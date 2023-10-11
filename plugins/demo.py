#coding:utf-8
from libs.event.qqvent import oncommand
import os
BASEURL = "http://127.0.0.1:5700"
def sendGroupMessage(gid: int, text: str):
    d = {"message": text, "group_id": gid}
    requests.post(f"{BASEURL}/send_group_msg", data=d)


@oncommand (promat=["","/"],cmd=["xk","下课"])
def handle(n):
    os.system("python.Birthday.py")
    sendGroupMessage(text="启动成功",gid=n.group_id)
