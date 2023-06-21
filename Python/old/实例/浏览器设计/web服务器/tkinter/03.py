'''tkinter  Entry 和 Text'''

import tkinter


base = tkinter.Tk()
base.title('My Window')
base.geometry('500x500')

def func():
    print(entry.get())

entry = tkinter.Entry(base, show=None, bg='green')
entry.pack()

but1 = tkinter.Button(base, text='点击', command=func)
but1.pack()


base.mainloop()