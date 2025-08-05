from tkinter import *
import time
from tkinter import ttk, messagebox

root=Tk()
root.title("Timer")
root.geometry("400x700")
root.config(bg="black")

#set resizable false 
root.resizable(False,False)

# "Timer"label at top
heading=Label(root,text="Timer",font="ariel 30 bold",bg="#000",fg="#ea3548")
heading.pack(pady=10)

#clock label
Label(root,font=("arial",15,"bold"),text="current time:",bg="papaya whip").place(x=30,y=70)


#function to get current time
def clock():
    clock_time=time.strftime('%H:%M:%S %p  %d/%m/%Y')
    current_time.config(text=clock_time)
    current_time.after(1000,clock)
    
current_time=Label(root,font=("arial",15,"bold"),text="",fg="#000",bg="#fff")
current_time.place(x=155,y=70)
clock()



#timer
hrs=StringVar()
Entry(root,textvariable=hrs,width=2,font="arial 40",bd=0).place(x=30,y=155)
hrs.set("00")

mins=StringVar()
Entry(root,textvariable=mins,width=2,font="arial 40",bd=0).place(x=150,y=155)
mins.set("00")

sec=StringVar()
Entry(root,textvariable=sec,width=2,font="arial 40",bd=0).place(x=270,y=155)
sec.set("00")

Label(root,text="hours",font="airal 12",bg="#000",fg="#fff").place(x=95,y=200)
Label(root,text="min",font="airal 12",bg="#000",fg="#fff").place(x=215,y=200)
Label(root,text="sec",font="airal 12",bg="#000",fg="#fff").place(x=340,y=200)

def Timer():
    times=int(hrs.get())*3600+int(mins.get())*60+int(sec.get())
    while times > -1:
        minute ,second=(times//60, times %60)
        hour=0
        if minute>60:
            hour,minute=(minute//60,minute%60)

        sec.set(second)
        mins.set(minute)
        hrs.set(hour)

        root.update()
        time.sleep(1)

        if(times==0):
            messagebox.showinfo('REMAINDER','Time is up!!!')
          
        times -= 1

#functions to directly set time after clicking image

def study():
    hrs.set("02")
    mins.set("00")
    sec.set("00")
    
def breaktime():
    hrs.set("00")
    mins.set("20")
    sec.set("00")

def revision():
    hrs.set("00")
    mins.set("05")
    sec.set("00")

#Start button at the bottom
button=Button(root,text="Start",bg="#ea3548",bd=0,fg="#fff",width=20,height=2,font="arial 10 bold",command=Timer)
button.pack(padx=5,pady=80,side=BOTTOM)

#add image buttons

Image1=PhotoImage(file="study.png")
Image1=Image1.subsample(50,50)
button1=Button(root,image=Image1,bg="#000",bd=0,command=study)
button1.place(x=45,y=300)

Image2=PhotoImage(file="break_time.png")
Image2=Image2.subsample(45,45)
button2=Button(root,image=Image2,bg="#000",bd=0,command=breaktime)
button2.place(x=160,y=300)

Image3=PhotoImage(file="revision.png")
Image3=Image3.subsample(50,50)
button3=Button(root,image=Image3,bg="#000",bd=0,command=revision)
button3.place(x=280,y=300)

#add timetable image
Image4=PhotoImage(file="timetable.png")
Image4=Image4.subsample(2,3)
button4=Button(root,image=Image4,bg="#000",bd=0,command=breaktime)
button4.place(x=80,y=400)


root.mainloop()

