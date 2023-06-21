'''tkinter label, button使用'''


import tkinter

base = tkinter.Tk()
# 设置窗口名
base.title('My window')
# 设置窗口大小
base.geometry('500x500')

var = tkinter.StringVar()

lab = tkinter.Label(base, textvariable=var, bg='green', width=15, height=2)
lab.pack()

hit = False


def hit_me():
    global hit

    if hit == True:
        var.set('')
        hit = False
    else:
        var.set('you hit me')
        hit = True


but = tkinter.Button(base, text='hit me', command=hit_me)
but.pack()

base.mainloop()
