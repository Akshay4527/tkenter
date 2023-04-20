from tkinter import *
s=Tk()
s.geometry('350x450')
s.resizable(False,True)
s.title('Tkinter')
s.configure(bg='black')

def add():
    l=Label(s,text='Hello World',bg='black',fg='white')
    l.pack()

b=Button(s,text='Click Here!!',command=add)
b.pack()

mainloop()