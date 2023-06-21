import os
import tkinter
from time import sleep


class DirList(object):
    def __init__(self, initdir=None):
        self.top = tkinter.Tk()
        self.label = tkinter.Label(self.top, text='Directory Lister v1.1')
        self.label.pack()

        self.cwd = tkinter.StringVar(self.top)

        self.dirl = tkinter.Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dirl.pack()

        self.dirfm = tkinter.Frame(self.top)
        self.dirsb = tkinter.Scrollbar(self.dirfm)
        self.dirsb.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.dirs = tkinter.Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.dirfm.pack()

        self.dirn = tkinter.Entry(self.top, width=50, textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        self.bfm = tkinter.Frame(self.top)
        self.clr = tkinter.Button(self.bfm, text='Clear', command=self.clrDir, activeforeground='white', activebackground='green')
        self.ls = tkinter.Button(self.bfm, text='List Directory', command=self.doLS, activeforeground='white', activebackground='green')
        self.quit = tkinter.Button(self.bfm, text='Quit', command=self.top.quit, activeforeground='white', activebackground='red')
        self.clr.pack(side=tkinter.LEFT)
        self.ls.pack(side=tkinter.LEFT)
        self.quit.pack(side=tkinter.LEFT)
        self.bfm.pack()

        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    def clrDir(self, ev=None):
        self.cwd.set('')

    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())

        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir: tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ': not a directory'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()

            return 
        
        self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)

        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, tkinter.END)
        self.dirs.insert(tkinter.END, os.curdir)
        self.dirs.insert(tkinter.END, os.pardir)

        for eachFile in dirlist:
            self.dirs.insert(tkinter.END, eachFile)
        
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')


def main():
    d = DirList(os.curdir)
    tkinter.mainloop()


if __name__ == "__main__":
    main()