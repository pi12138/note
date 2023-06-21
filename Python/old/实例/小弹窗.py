import tkinter

base = tkinter.Tk()
base.geometry('200x200')


def func1():
	label2 = tkinter.Label(base, text='干的漂亮')
	label2.pack()

def func2():
	label2 = tkinter.Label(base, text='谁让你点我的')
	label2.pack()

label1 = tkinter.Label(base, text='别看了快点按钮')
label1.pack()

button1 = tkinter.Button(base, text='点我', command=func1)
button1.pack()
button2 = tkinter.Button(base, text='快点我', command=func2)
button2.pack()

base.mainloop()