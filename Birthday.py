import tkinter as tk
import time

# 创建主窗口
root = tk.Tk()
root.title("等待一秒后关闭窗口")

# 等待一秒
time.sleep(1)

# 关闭窗口
root.destroy()

# 进入主循环
root.mainloop()
