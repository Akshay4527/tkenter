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
g=Button(s,text='Submit',bg='grey',fg='white')
g.place(x=100,y=90)



mainloop()