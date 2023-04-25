from tkinter import *
s=Tk()
s.geometry('800x800')
s.resizable(False,False)
s.title('Students Mark Sheet')
s.configure(bg='white')

l=Label(s,text='STUDENT MARK SHEET',bg='white',font=("bold",24))
l.place(x=5,y=0)

l1=Label(s,text='NAME', bg="white",fg='black')
l1.place(x=5,y=60)
l2=Entry(s,width=20,border=2)
l2.place(x=55,y=60)


l3=Label(s,text='Roll No:', bg="white",fg='black')
l3.place(x=200,y=60)
l4=Entry(s,width=20,border=2)
l4.place(x=250,y=60)

l5=Label(s,text='SUBJECTS', bg="black",fg='white',font='bold',width=20, borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='white')
l5.place(x=5,y=150)
l6=Label(s,text='MARKS', bg="black",fg='white',font='bold',width=20, borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='white')
l6.place(x=185,y=150)
l7=Label(s,text='GRADE', bg="black",fg='white',font='bold',width=20, borderwidth=1,relief='solid',highlightthickness=1,highlightcolor='white')
l7.place(x=365,y=150)

l8=Label(s,text='ENGLISH', bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l8.place(x=5,y=174)
l9=Entry(bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l9.place(x=185,y=174)
l10=Entry(bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l10.place(x=365,y=174)

l11=Label(s,text='HINDI', bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l11.place(x=5,y=198)
l12=Entry(bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l12.place(x=185,y=198)
l13=Entry(bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l13.place(x=365,y=198)

l14=Label(s,text='SCIENCE', bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l14.place(x=5,y=222)
l15=Entry(bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l15.place(x=185,y=222)
l16=Entry(bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l16.place(x=365,y=222)

l17=Label(s,text='MATHS', bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l17.place(x=5,y=246)
l18=Entry(bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l18.place(x=185,y=246)
l19=Entry(bg="grey",fg='black',font='bold',width=20, borderwidth=1,relief='solid')
l19.place(x=365,y=246)

submit=Button(s,text='SUBMIT',bg='light blue',fg='white')
submit.place(x=450,y=280)

s.mainloop()
