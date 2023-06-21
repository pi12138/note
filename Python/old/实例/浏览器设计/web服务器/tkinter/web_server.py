'''编写服务器简单界面'''

import tkinter

class WebServerGUI():

    def __init__(self, master):

        self.base = tkinter.Tk()
        self.base.title('Web Server')
        self.base.geometry('500x500')


    label1 = tkinter.Label(base, text='IP:')
    label1.pack()
    entry1 = tkinter.Entry(base, show=None, bg='gray')
    entry1.pack()

    label2 = tkinter.Label(base, text='Port:')
    label2.pack()
    entry2 = tkinter.Entry(base, show=None, bg='gray')
    entry2.pack()

    def start():
        ip = entry1.get()
        port = entry2.get()
        print(ip, port)

    button1 = tkinter.Button(base, text='开启', command=start)
    button1.pack()

    label3 = tkinter.Label(base, bg='gray', width=50, height=30)
    label3.pack()





    base.mainloop()