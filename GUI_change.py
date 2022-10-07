from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import * 

infos = [] # 用来装物品信息，创建一个列表

class StartPage:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个窗口
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('物品交换系统')
		self.window.geometry('300x410+500+100') # 这里的乘是小x，第一个参数表示窗口的长，第二个表示宽，第三个表示的距离屏幕左边界的距离，第三个为距离上边界的距离
 
		label = Label(self.window, text="物品交换系统", font=("Verdana", 20))
		label.pack(pady=100)  # pady=100 这个label距离窗口上边界的距离，这里设置为100刚好居中

		
 		# command=lambda:  可以带参数，注意带参数的类不要写括号，否者，这里调用会直接执行(class test:)
		Button(self.window, text="添加物品", font=tkFont.Font(size=16), command=lambda: Add(self.window), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()	# pack() 方法会使得组件在窗口中自动布局
		Button(self.window, text="删除物品", font=tkFont.Font(size=16), command=lambda: Del(self.window), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="查找物品", font=tkFont.Font(size=16), command=lambda: Find(self.window), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="所有物品", font=tkFont.Font(size=16), command=lambda: Show(self.window), width=30, height=1,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		Button(self.window, text="退出系统", height=1, font=tkFont.Font(size=16), width=30, command=self.window.destroy,
			   fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
		

		self.window.mainloop() # 主消息循环

#添加
class Add:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('添加物品')
		self.window.geometry('450x300+500+100')

		# 创建提示信息
		tk.Label(self.window, text='名称: ').place(x=80, y= 50)
		tk.Label(self.window, text='类别: ').place(x=80, y= 90)
		tk.Label(self.window, text='数量: ').place(x=80, y= 130)
		tk.Label(self.window, text='联系方式: ').place(x=80, y= 170)

		# 输入框
		self.name = tk.Entry(self.window)
		self.name.place(x=160, y=50)
		self.cla = tk.Entry(self.window)
		self.cla.place(x=160, y=90)
		self.qty = tk.Entry(self.window)
		self.qty.place(x=160, y=130)
		self.tel = tk.Entry(self.window)
		self.tel.place(x=160, y=170)

		# 按键
		btn_back = Button(self.window, text="添加物品", width=8, font=tkFont.Font(size=12), command=self.add)
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=250)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		StartPage(self.window) # 显示主窗口 销毁本窗口

	def add(self):
		info = {}   # 创建一个字典，来装商品信息
		info['name'] = self.name.get()
		info['cla'] = self.cla.get()
		info['qty'] = self.qty.get()
		info['tel'] = self.tel.get()
		infos.append(info)

		# 弹窗显示
		window_tip = tk.Tk()
		window_tip.geometry('100x50')
		tk.Label(window_tip, text='物品添加成功 ').place(x=30, y= 20)
		window_tip.mainloop()

# 删除
class Del:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('删除物品')
		self.window.geometry('450x300+500+100')

		# 创建提示信息
		tk.Label(self.window, text='名称: ').place(x=80, y= 90)
		tk.Label(self.window, text='联系方式: ').place(x=80, y= 120)
		
		self.name = tk.Entry(self.window)
		self.name.place(x=160, y=90)
		self.tel = tk.Entry(self.window)
		self.tel.place(x=160, y=120)
		

		btn_back = Button(self.window, text="删除物品", width=8, font=tkFont.Font(size=12), command=self.delete)
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=250)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		StartPage(self.window) # 显示主窗口 销毁本窗口

	def delete(self):
		flag = 0
		name = self.name.get()
		tel = self.tel.get()
		for i in infos:
			if i.get('name') == name and i.get('tel') == tel :
				infos.remove(i)#删除掉i的所有信息
				flag = 1
		if flag:	
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('100x50')
			tk.Label(window_tip, text='物品删除成功 ').place(x=30, y= 20)
			window_tip.mainloop()
		if not flag:
			# 弹窗显示
			window_tip = tk.Tk()
			window_tip.geometry('100x50')
			tk.Label(window_tip, text='未找到此物品').place(x=30, y= 20)
			window_tip.mainloop()

# 查找
class Find:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('查找物品')
		self.window.geometry('450x300+500+100')

		# 创建提示信息
		tk.Label(self.window, text='名称: ').place(x=80, y= 100)
		
		self.name = tk.Entry(self.window)
		self.name.place(x=160, y=100)
		

		btn_back = Button(self.window, text="查找物品", width=8, font=tkFont.Font(size=12), command=self.find)
		btn_back.place(x=200, y=210)
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=270)
		
		self.window.mainloop()

	# 返回首页
	def back(self):
		StartPage(self.window) # 显示主窗口 销毁本窗口

	def find(self):
		flag = 0
		name = self.name.get()
		
		# 滚条
		roll = tk.Scrollbar(self.window)
		roll.pack(side = tk.RIGHT,fill = tk.Y)
		# 文本
		text_input = tk.Text(self.window,width=100,height=20)
		for i in infos:
			if i.get('name') == name:
				flag = 1
				text_input.insert('insert',"名称：{}\t类别：{}\t数量：{}\t联系方式：{}\n".format(i.get('name'),
						i.get('cla'),i.get('qty'),i.get('tel')))
		if not flag:
			text_input.insert('insert','未找到此物品')
		text_input.pack()
		# 绑定
		text_input.config(yscrollcommand=roll.set) 
		roll.config(command=text_input.yview) 
							
		self.window.mainloop()


#列出所有物品
class Show:
	def __init__(self, parent_window):
		parent_window.destroy() # 销毁上一个界面
		self.window = tk.Tk()  # 初始框的声明
		self.window.title('所有物品')
		self.window.geometry('450x300+500+100')

		# 滚条
		roll = tk.Scrollbar(self.window)
		roll.pack(side = tk.RIGHT,fill = tk.Y)
		# 文本
		text_input = tk.Text(self.window,width=100,height=20)
		for i in infos:
			text_input.insert('insert',"名称：{}\t类别：{}\t数量：{}\t联系方式：{}\n".format(i.get('name'),
						i.get('cla'),i.get('qty'),i.get('tel')))
		text_input.pack()
		# 绑定
		text_input.config(yscrollcommand=roll.set) 
		roll.config(command=text_input.yview) 
					
		btn_back = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
		btn_back.place(x=200, y=270)
		
		self.window.mainloop()

	# 返回
	def back(self):
		StartPage(self.window) # 显示主窗口 销毁本窗口


if __name__ == '__main__':
	# 实例化Application
	window = tk.Tk()
	StartPage(window)