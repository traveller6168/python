#!/usr/bin/env python3

from functools import partial
import tkinter

root = tkinter.Tk()  #生成root主窗口
MyButton = partial(tkinter.Button,root,fg='white',bg = 'blue')
b1 = MyButton(text = 'Button 1')
b2 = MyButton(text = 'Button 2')
qb = MyButton(text = 'QUIT',bg = 'red',command = root.quit())

b1.pack()
b2.pack()
qb.pack(fill = x,expand = True)
root.title('PFAs!')
root.mainloop()
