from tkinter import Listbox, Tk, ttk, Label, Entry, Scrollbar, END
from tkinter.filedialog import asksaveasfile, askopenfilename

class ToDo:
    def __init__(self):
        self.win = Tk()
        self.win.title('TO DO')
        self.win.resizable(False,False)
        self.putComponents()
        self.win.mainloop()

    def putComponents(self):
        self.bsave = ttk.Button(self.win, text="SAVE")
        self.bload = ttk.Button(self.win, text="LOAD")
        self.bclear = ttk.Button(self.win, text="CLEAR")
        
        self.lname = Label(self.win, text="TO DO")

        self.badd = ttk.Button(self.win, text="+")
        self.bsub = ttk.Button(self.win, text="-")

        self.etext = Entry(self.win,text="write here .....")
        
        
        self.lb = Listbox(self.win)

        self.scroll_list = Scrollbar(self.win, command=self.lb.yview)

        self.bsave.grid(row=0,column=0,sticky="news")
        self.bclear.grid(row=0,column=1,sticky="news")
        self.lname.grid(row=3,column=0,rowspan=1,columnspan=3,sticky="news")
        self.bload.grid(row=0,column=2,sticky="news")
        self.lb.grid(row=1,column=0,rowspan=1,columnspan=2,sticky="news")
        self.scroll_list.grid(row=1,column=2,rowspan=1,columnspan=1,sticky="news")
        self.badd.grid(row=2,column=0,sticky="news")
        self.etext.grid(row=2,column=1,sticky="news")
        self.bsub.grid(row=2,column=2,sticky="news")

        self.badd.bind("<Button 1>", self.add)
        self.bsub.bind("<Button 1>", self.remove)
        self.bsave.bind("<Button 1>", self.save)
        self.bload.bind("<Button 1>", self.load)
        self.bclear.bind("<Button 1>", self.clear)

    def add(self,event):
        s=self.etext.get()
        self.lb.insert(self.lb.size(),s)

    def remove(self,event):
        item = self.lb.curselection()
        if item!=():
            self.lb.delete(item)

    def clear(self,event):
        self.lb.delete(0,END)

    def save(self,event):
        fp = asksaveasfile(initialfile = 'Untitled.todo',defaultextension=".todo",filetypes=[("ToDo","*.todo")])
        v = list(self.lb.get(0,END))
        for i in range(len(v)):
            v[i]=v[i]+"\n"
        fp.writelines(v)
        fp.close()
        
    def load(self,event):
        name=askopenfilename()
        self.lname.configure(text=name.split('/')[-1])
        self.lb.delete(0,END)
        fp=open(name,'r')
        v = fp.readlines()
        fp.close()
        for i in range(len(v)):
            v[i] = ((v[i]).split("\n"))[0]
            self.lb.insert(i,v[i])
        
if __name__=="__main__":
    ToDo()
