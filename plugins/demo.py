from libs.event.qqvent import oncommond
import os
import ping
@oncommond (promat=[""],cmd=["生日"]
def handle(n):
    os.system("python.Birthday.py")
    sendGroupMessage("启动成功",n.groupID)
