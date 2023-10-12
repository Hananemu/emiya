#coding.utf-8
from win10toast import ToastNotifier as TN
from libs.event.qqevent import oncommand
tn=TN()
@oncommand(promat=["~"],cmd=["n","notice","提醒"])
def handle(n):
  tn_show_toast(title="提醒",msg=n.arg,icon_puth=None,duration=5,threaded=True)
