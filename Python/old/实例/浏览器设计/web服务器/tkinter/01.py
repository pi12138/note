
import tkinter

def func():
    file = open('../html/index.html', 'r')
    content = file.read()
    file.close()

    lab = tkinter.Label(base, text=content)
    lab.pack()


base = tkinter.Tk()
# 设置窗口名
base.title('My window')
# 设置窗口大小
base.geometry('500x500')


but = tkinter.Button(base, text='开启', command=func)
but.pack()

base.mainloop()
