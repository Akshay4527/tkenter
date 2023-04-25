from tkinter import *
s=Tk()
s.geometry('400x500')
s.title('Login')
s.configure(bg='black')

l=Label(s,text='LOGIN FORM',bg='black',fg='white')
l.pack(side=TOP)
r=Label(s,text='Name: ',bg='black',fg='white',borderwidth=2)
r.place(x=10,y=30)
d=Entry(s,width=30)
d.place(x=70,y=30)

e=Label(s,text='Password: ',bg='black',fg='white')
e.place(x=10,y=60)
f=Entry(s,width=30)
f.place(x=70,y=60)

def submit():
    aks=Label(s,text=d.get(),bg='black',fg='white')
    ak=Label(s,text=f.get(),bg='black',fg='white')
    aks.place(x=90,y=130)
    ak.place(x=105,y=160)

g=Button(s,text='Submit',bg='grey',fg='white',command=submit)
g.place(x=100,y=90)

s.mainloop()