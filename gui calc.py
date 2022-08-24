from tkinter import *
root=Tk()
root.title("90's calculater")
e=Entry(root,width=45,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#e.insert(0, "entr your name")
def but_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
def but_clear():
    e.delete(0,END)
def but_add():
    global fnum
    global opr
    fnum=int(e.get())
    opr="add"
    e.delete(0,END)
def but_sub():
    global fnum
    global opr
    fnum=int(e.get())
    opr="sub"
    e.delete(0,END)
def but_mul():
    global fnum
    global opr
    opr="mul"
    fnum = int(e.get())
    e.delete(0, END)
def but_div():
    global fnum
    global opr
    opr="div"
    fnum = int(e.get())
    e.delete(0, END)
def but_equal():
    #secnum=e.get()
    snum=int(e.get())
    e.delete(0,END)
    if opr=="add":
        e.insert(0,fnum+snum)
    elif opr=="sub":
        e.insert(0,fnum-snum)
    elif opr=="mul":
        e.insert(0,fnum*snum)
    else :
        e.insert(0,fnum/snum)
but1=Button(root,text="1",padx=40,pady=20,command=lambda: but_click(1))
but2=Button(root,text="2",padx=40,pady=20,command=lambda: but_click(2))
but3=Button(root,text="3",padx=40,pady=20,command=lambda: but_click(3))
but4=Button(root,text="4",padx=40,pady=20,command=lambda: but_click(4))
but5=Button(root,text="5",padx=40,pady=20,command=lambda: but_click(5))
but6=Button(root,text="6",padx=40,pady=20,command=lambda: but_click(6))
but7=Button(root,text="7",padx=40,pady=20,command=lambda: but_click(7))
but8=Button(root,text="8",padx=40,pady=20,command=lambda: but_click(8))
but9=Button(root,text="9",padx=40,pady=20,command=lambda: but_click(9))
but0=Button(root,text="0",padx=40,pady=20,command=lambda: but_click(0))
butadd=Button(root,text="+",padx=39,pady=20,command=but_add)
butsub=Button(root,text="-",padx=41,pady=20,command=but_sub)
butmul=Button(root,text="*",padx=40,pady=20,command=but_mul)
butdiv=Button(root,text="%",padx=38,pady=20,command=but_div)

butclr=Button(root,text="clear",padx=81,pady=20,command=but_clear)
butequal=Button(root,text="=",padx=89,pady=20,command=but_equal)

but1.grid(row=1,column=0)
but2.grid(row=1,column=1)
but3.grid(row=1,column=2)

but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)

but7.grid(row=3,column=0)
but8.grid(row=3,column=1)
but9.grid(row=3,column=2)
but0.grid(row=4,column=0)
butadd.grid(row=6,column=0)
butsub.grid(row=5,column=0)
butmul.grid(row=4,column=1)
butdiv.grid(row=4,column=2)

butclr.grid(row=5,column=1,columnspan=2)
butequal.grid(row=6,column=1,columnspan=2)
'''
def myclick():
    hello="Hello"+e.get()
    lab=Label(root,text=hello)
    lab.pack()
but=Button(root,text="enter ur stock",command=myclick)
#but.pack()
'''
root.mainloop()