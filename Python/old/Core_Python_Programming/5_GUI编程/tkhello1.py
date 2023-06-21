import tkinter


def resize(ev=None):
    label.config(font='Helvetica -{} bold'.format(scale.get()))


top = tkinter.Tk()
top.geometry('250x150')

label = tkinter.Label(top, text='hello world!', font='Helvetica -12 bold')
label.pack(fill=tkinter.Y, expand=1)

scale = tkinter.Scale(top, from_=10, to=40, orient=tkinter.HORIZONTAL, command=resize)
scale.set(12)
scale.pack(fill=tkinter.X, expand=1)

quit = tkinter.Button(top, text='QUIT!', command=top.quit, bg='red', fg='white')
quit.pack(fill=tkinter.X, expand=1)

tkinter.mainloop()