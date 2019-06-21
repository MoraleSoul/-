# -*- coding: utf-8 -*-
"""
Created on Thu May 30 15:52:02 2019

@author: 18420
"""

import tkinter
from tkinter import Menu
from tkinter import scrolledtext
import tkinter.messagebox

import re
import os

from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
import matplotlib.pyplot as plt

#读取文本文件
f = open('英语作文.txt')
ff = f.read()
l1 = []
line = ff.replace('.',' ').replace('!',' ').replace(',',' ').replace('?',' ').replace('  ',' ').replace(';',' ').replace("’",' ').replace("“",' ').replace("”",' ')
w = line.split()
for i in w:
    l1.append(i.lower())#去掉字符后小写化放入列表

#读取英文停用词表
f1 = open('英文停用词表.txt')
stopword = f1.readlines()
l2 = []
for i in stopword:
    i = i.strip()
    l2.append(i)#将停用词表放入列表

#去掉停用词后的单词放入列表
l3 = []
for i in l1:
    if i not in l2:
        l3.append(i)
    else:
        continue

def full():
    #输出原文本
    print(line)	

def word():
    for i in l1:
        print(i,end='')

def Wordcount(lists):
    #检索重复单词计算瓷瓶
    wkey = {}
    wkey = wkey.fromkeys(lists)
    word = list(wkey.keys())
    for i in word:
        wkey[i] = lists.count(i)
    return wkey

def sort(wkey):
    #词频排序
	wkey1 = {}
	wkey1 = sorted(wkey.items(),key=lambda d:d[1],reverse=True)
	wkey1 = dict(wkey1)
	return wkey1

def main(word):
    global l4
    l4 = []
    for x,y in word.items():
            c = format(x),format(y)
            l4.append(c)
            continue

#由于tkinter中没有ToolTip功能，所以定义这个功能如下
class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
 
    def showtip(self, text):
        #显示tooltip
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tkinter.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tkinter.Label(tw, text=self.text, justify=tkinter.LEFT,
                              background="#ffffe0", relief=tkinter.SOLID,
                              borderwidth=1,font=("黑体", "10", "normal"))
        label.pack(ipadx=1)
 
    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def createToolTip( widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

#创建一层主界面窗口
top = tkinter.Tk()
top.title('文本编辑器')
top.geometry('635x600') 

def B1():
    #在主窗口输出所有字母
    t1 = tkinter.Tk()
    t1.title('所有字母查看框')
    t1.geometry('500x400') 
    scrt1 = scrolledtext.ScrolledText(t1)
    scrt1.place(x=10,y=10,width=500,height=380)

    for i in l1:
        scrt1.insert(tkinter.INSERT, i) 

def B2():
    #在主窗口输出单词总数
    scr3.insert(tkinter.INSERT, len(l1))

def B3():
    #在主窗口输出所有单词词频
    t2 = tkinter.Tk()
    t2.title('单词词频查看框')
    t2.geometry('400x600') 
    scrt2 = scrolledtext.ScrolledText(t2)
    scrt2.place(x=10,y=10,width=390,height=580)
    
    main(sort(Wordcount(l1)))
    for i in l4:
        var = i[0] + ' ' + i[-1] + '次' + '\n'
        scrt2.insert(tkinter.INSERT, var)

def B4():
    #在主窗口输出关键词及其词频以及二者构成的柱状图（柱状图直接输出）
    la = []
    lb = []
    main(sort(Wordcount(l3)))
    for i in range(6):
        la.append(l4[i][0])
        lb.append(int(l4[i][1]))
    
    scr4.insert(tkinter.INSERT, '关键词：' + '\n')
    for j in la:
        scr4.insert(tkinter.INSERT, j + '\n')
    
    fig, ax = plt.subplots()  
    ax.bar(la,lb,label=u'关键词词频')
    plt.title('数据分析表')
    plt.ylabel('词频')
    plt.xlabel('关键词')
    plt.legend()
    plt.show()

#清除文本框文本函数
def cancel():
    scr.delete('0.0', 'end')
    
#def cancel2():
    #scr2.delete('0.0', 'end')
    
def cancel3():
    scr3.delete('0.0', 'end')
    
def cancel4():
    scr4.delete('0.0', 'end')

#创建文本框
scr = scrolledtext.ScrolledText(top)
scr.place(x=130,y=40,width=500,height=530)

#scr2 = scrolledtext.ScrolledText(top)
#scr2.place(x=640,y=30,width=500,height=540)

scr3 = scrolledtext.ScrolledText(top)
scr3.place(x=130,y=1,width=500,height=30)

scr4 = scrolledtext.ScrolledText(top)
scr4.place(x=10,y=222,width=115,height=200)

#设置查看按钮
button1 = tkinter.Button(top,text='查看所有字母',bd = 2,activebackground='DarkGray',
                         font=('黑体',10),command = B1)
button2 = tkinter.Button(top,text='查看单词个数',bd = 2,activebackground='DarkGray',
                         font=('黑体',10),command = B2)
button3 = tkinter.Button(top,text='查看单词词频',bd = 2,activebackground='DarkGray',
                         font=('黑体',10),command = B3)
button4 = tkinter.Button(top,text='查看关键词',bd = 2,activebackground='DarkGray',
                         font=('黑体',10),command = B4)

#设置清除文本框文字按钮
cancel1 = tkinter.Button(top,text='清除编辑文本框',bd = 2,activebackground='DarkGray',
                         font=('微软雅黑',10),command = cancel)
#cancel2 = tkinter.Button(top,text='清除词频文本框',bd = 2,activebackground='DarkGray',
                         #font=('微软雅黑',10),command = cancel2)
cancel3 = tkinter.Button(top,text='清除单词数文本框',bd = 2,activebackground='DarkGray',
                         font=('微软雅黑',10),command = cancel3)
cancel4 = tkinter.Button(top,text='清除关键词文本框',bd = 2,activebackground='DarkGray',
                         font=('微软雅黑',10),command = cancel4)

#将按钮固定
button1.place(x=10, y=80, width=100, height=30)
button2.place(x=10, y=40, width=100, height=30)
button3.place(x=10, y=120, width=100, height=30)
button4.place(x=10, y=160, width=100, height=30)
cancel1.place(x=10, y=460, width=110, height=30)
#cancel2.place(x=10, y=460, width=110, height=30)
cancel3.place(x=10, y=500, width=110, height=30)
cancel4.place(x=10, y=540, width=110, height=30)

#设置菜单栏相关函数
def _open():
    #打开原文本
    scr.insert(tkinter.INSERT, ff)

def _quit():
    #关闭文本编辑器
    top.quit()
    top.destroy()

def _seek():
    #查找工具
    SK = tkinter.Tk()
    SK.title('查找工具')
    SK.geometry('300x200')
    
    label_a = tkinter.Label(SK,text = '请输入需要查找的内容',font=('微软雅黑',10))
    textbox_a = tkinter.StringVar(SK,value='')
    Seekword = tkinter.Entry(SK,width = 20,bd=1,textvariable = textbox_a)
    label_a.place(x=80,y=10,width=140,height=25)
    Seekword.place(x=20,y=50,width=260,height=25)
    
    def SKok():
        #开始查找按钮函数
        Afword = scr.get('0.0', 'end')
        Bfword = scr.get('0.0', 'end')
        if Bfword == '\n':
            #编辑文本框尚未输入文本出现操作
            tkinter.messagebox.showerror(title = '查找失败',
                                         message = '尚未输入文本无法进行替换\n\n提示：在 “文件” 处调出文本')
            SK.destroy()
        else:
            SKword = Seekword.get()
            s = str(SKword)
            countSK = list(re.subn( SKword,'*'*len(s),Bfword))#计算符合的内容存在的个数
            if int(countSK[-1]) > 0:
                l5 = ()
                
                #记录所有符合的内容所在的区间
                for i in range(countSK[-1]):
                    searchSK = re.search( SKword, Bfword, re.M|re.I)
                    l5 += searchSK.span()
                    Neword = re.sub(searchSK.group(0),'*'*len(s),Bfword,count = 1)
                    scr.delete('0.0', 'end')
                    scr.insert(tkinter.INSERT, Neword)
                    Bfword = scr.get('0.0', 'end')
                scr.delete('0.0', 'end')
                scr.insert(tkinter.INSERT, Afword)
                
                #将所得区间高亮
                for i in range(0,len(l5)-1,2):
                    a = str(1) + '.' + str(l5[i]) 
                    b = str(1) + '.' + str(l5[i+1])
                    scr.tag_add('tag1', a, b)
                    scr.tag_config('tag1', background='yellow', foreground='red')
                tkinter.messagebox.showinfo(title = '查找成功',
                                            message = '已经将所有的'+'“'+SKword+'”'+'查找出')
                SK.destroy()
            else:
                tkinter.messagebox.showerror(title = '查找失败',
                                             message = '未能找到需要查找的内容')
    def cancelSK():
        #取消查找，关闭查找工具
        SK.destroy()
    
    #创建按钮并固定
    ok = tkinter.Button(SK,text='查找',bd = 1,activebackground='DarkGray',
                         font=('黑体',12),command = SKok)
    cancelok = tkinter.Button(SK,text='取消',bd = 1,activebackground='DarkGray',
                               font=('黑体',12),command = cancelSK)
    ok.place(x=20, y=150, width=80, height=30)
    cancelok.place(x=200, y=150, width=80, height=30)
    
    #启动消息循环
    SK.mainloop()

def _replace():
    #替换工具
    RE = tkinter.Tk()
    RE.title('替换工具')
    RE.geometry('300x200')
    
    #创建标签组件并固定
    label_b = tkinter.Label(RE,text = '请输入需要替换的内容',font=('微软雅黑',10))
    textbox_b = tkinter.StringVar(RE,value='')
    Seekword2 = tkinter.Entry(RE,width = 20,bd=1,textvariable = textbox_b)
    label_c = tkinter.Label(RE,text = '请输入替换之后的内容',font=('微软雅黑',10))
    textbox_c = tkinter.StringVar(RE,value='')
    Reword = tkinter.Entry(RE,width = 20,bd=1,textvariable = textbox_c)
    
    label_b.place(x=80,y=10,width=140,height=25)
    Seekword2.place(x=20,y=40,width=260,height=25)
    label_c.place(x=80,y=80,width=140,height=25)
    Reword.place(x=20,y=110,width=260,height=25)
    
    def REok():
        #开始替换函数
        Orword = scr.get('0.0', 'end')
        if Orword == '\n':
            #编辑文本框尚未输入文本出现操作
            tkinter.messagebox.showerror(title = '替换失败',
                                         message = '尚未输入文本无法进行替换\n\n提示：在 “文件” 处调出文本')
            RE.destroy()
        else:
            Aword = str(Seekword2.get())#需要替换的内容
            Bword = str(Reword.get())#替换之后的内容
            searchRE = re.search( Aword, Orword, re.M|re.I)#查找需要替换的内容出现次数
            if searchRE:
                #需要查找内容存在，进行替换
                Moword = re.sub(Aword,Bword,Orword)
                scr.delete('0.0', 'end')
                scr.insert(tkinter.INSERT, Moword)
                tkinter.messagebox.showinfo(title = '替换成功',
                                            message = '已经将所有的'+'“'+Aword+'”'+'替换为'+'“'+Bword+'”')
                RE.destroy()
            else:
                tkinter.messagebox.showerror(title = '替换失败',
                                             message = '未能找到需要替换的内容')
    def cancelRE():
        #取消替换，关闭替换工具
        RE.destroy()
    
    #创建按钮并固定
    ok2 = tkinter.Button(RE,text='替换',bd = 1,activebackground='DarkGray',
                         font=('黑体',12),command = REok)
    cancelok2 = tkinter.Button(RE,text='取消',bd = 1,activebackground='DarkGray',
                               font=('黑体',12),command = cancelRE)
    ok2.place(x=20, y=150, width=80, height=30)
    cancelok2.place(x=200, y=150, width=80, height=30)
    
    #启动消息循环
    RE.mainloop()

#撤销与恢复
def callback(event):
    #每当有字符插入的时候，就自动插入一个分割符，主要是防止每次撤销的时候会全部撤销
    scr.edit_separator()
scr.bind("<Key>", callback)
 
def show1():
    x = scr.get('0.0', 'end')
    if len(x) == 1: #如果还剩余一个字符的话，不能撤销
        return
    scr.edit_undo()
 
maxx = scr.get('0.0', 'end')
def show2():
    if len(maxx) == len(scr.get('0.0', 'end')):
        return
    scr.edit_redo()

#创建撤销恢复按钮并固定
buttonc = tkinter.Button(top, text = "撤销", command = show1)
buttons = tkinter.Button(top, text = "恢复", command = show2)
buttonc.place(x=10, y=1, width=50, height=30)
buttons.place(x=60, y=1, width=50, height=30)

def _http():
    #打开超链接
    os.system('"C:/Program Files/Internet Explorer/iexplore.exe" https://ipaperclip.net/doku.php')

def _KFC():
    #开发者选项函数设置
    top2 = tkinter.Tk()
    top2.title('开发者系统登录界面')
    top2.geometry('300x150') 
    
    #在登录界面窗口创建‘用户名’和‘密码’标签组件
    label_a = tkinter.Label(top2,text='用户名',font=('微软雅黑',10))
    label_b = tkinter.Label(top2,text='密码',font=('微软雅黑',10))
    label_a.place(x=10,y=15,width=120,height=25)
    label_b.place(x=10,y=40,width=120,height=25)
    textbox_a = tkinter.StringVar(top,value='')
    textbox_b = tkinter.StringVar(top,value='')
    #创建密码文本框
    entryName = tkinter.Entry(top2,width = 15,bd = 1,textvariable = textbox_a)
    entryPwd = tkinter.Entry(top2,show = '*',width = 15,bd = 1,textvariable = textbox_b)
    entryName.place(x=100, y=15, width=120, height=25)
    entryPwd.place(x=100, y=40, width=120, height=25)
    
    #加入ToolTip
    createToolTip(entryName,'用户名不为空')
    createToolTip(entryPwd,'密码不为空')
    
    def login():
        #登录函数
        name = entryName.get()          #获取用户名
        pwd = entryPwd.get()            #获取密码
        #只要二者其中一个为空就不能登录
        if name == '' or pwd == '':
            tkinter.messagebox.showerror('登录失败',message = '用户名或密码错误')
            top2.destroy()
        else:
            tkinter.messagebox.showinfo(title = '登录成功',message = '欢迎来到开发者模式')
            top2.destroy()#将登录窗口关闭
            
            #开发者模式窗口设置
            top3 = tkinter.Toplevel()
            top3.title('开放人员模式')
            top3.geometry('1000x500')
            
            #插入图片
            img01 = tkinter.PhotoImage(file = 'image01.png')
            image01 = tkinter.Label(top3, text="abc", image=img01)
            img02 = tkinter.PhotoImage(file = 'image02.png')
            image02 = tkinter.Label(top3, text="abc", image=img02)
            image01.place(x=10, y=10)
            image02.place(x=500, y=10)
            
            #启动消息循环
            top3.mainloop()
    
    def cancelK():
        #关闭登录界面窗口
        top2.destroy()
    
    #设置按钮并固定
    button_a = tkinter.Button(top2,text='Login',bd = 1,activebackground='DarkGray',
                              font=('微软雅黑',10),command = login)
    button_b = tkinter.Button(top2,text='退出',bd = 1,activebackground='DarkGray',
                              font=('微软雅黑',10),command = cancelK)
    button_a.place(x=90, y=80, width=50, height=30)
    button_b.place(x=150, y=80, width=50, height=30)
    
    #启动消息循环
    top2.mainloop()

#def _light():
    #scr.tag_add(self)   

#创建菜单栏
menuBar = Menu(top)
top.config(menu=menuBar)
 
#添加菜单栏组件
#文件菜单栏
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="打开文本文件", command=_open)
fileMenu.add_separator()
fileMenu.add_command(label="退出文本编辑", command=_quit)
menuBar.add_cascade(label="文件", menu=fileMenu)

#编辑菜单栏
msgMenu = Menu(menuBar, tearoff=0)
msgMenu.add_command(label="查找", command=_seek)
msgMenu.add_separator()
msgMenu.add_command(label="替换", command=_replace)
menuBar.add_cascade(label="编辑", menu=msgMenu)

#帮助菜单栏
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="打开超链接", command=_http)
helpMenu.add_separator()
helpMenu.add_command(label="开发者选项", command=_KFC)
menuBar.add_cascade(label="帮助", menu=helpMenu)

#创建编辑框右键菜单
menubar = tkinter.Menu(top)
menubar.add_cascade(label="高亮文本")
 
def Menu1(event):
    menubar.post(event.x_root, event.y_root)   #将菜单条绑定上事件，坐标为x和y的root位置
 
#设定鼠标右键触发事件，调用xShowMenu方法
scr.bind("<Button-3>", Menu1)
#scr2.bind("<Button-3>", Menu1)
scr3.bind("<Button-3>", Menu1)
scr4.bind("<Button-3>", Menu1)

#加入ToolTip
createToolTip(scr,'这是文本编辑框\n右键调出更多选项')
#createToolTip(scr2,'这是词频文本框')
createToolTip(scr3,'这是单词数文本框')
createToolTip(scr4,'这是关键词文本框')
createToolTip(buttonc,'这是失效了的撤销按钮')
createToolTip(buttons,'这是失效了的恢复按钮')

#启动消息循环
top.mainloop()