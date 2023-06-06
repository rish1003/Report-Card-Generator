# MAIN PROGRAM
import tkinter as tk
from ut import *
from hy import *
from fs import *

#------------------------------------------------------------------------------

#storing text
f=open("welcome.txt","w")
f.write("     Welcome to the Report Card Generator!    ")
f.close()
f1=open("text.txt","w")
f1.writelines(["An easy tool to make the tedious task of","\n","making report cards troublefree.","\n",\
         "The report cards generated can be screenshotted","\n", \
         "and saved for future use."])
f1.close()
f4=open("disclaimer.txt","w")
f4.writelines(["General Instructions:","\n","1. Input the required values in the corresponding boxes","\n", \
              "2. 5 Subjects are compulsory, 6th is optional"])
f4.close()

#------------------------------------------------------------------------------

#tkinter setup
global lvl
lvl=tk.Tk()
lvl.title("WELCOME")
lvl.geometry("815x611")
global ph
ph=tk.PhotoImage(file="Capture.png")
l=tk.Label(lvl,image=ph)
l.place(x=0,y=0)

#------------------------------------------------------------------------------

#retrieving data from text files
f2=open("welcome.txt","r")
welcome1=f2.read()
f2.close()
f3=open("text.txt","r")
welcome2=f3.read()
f3.close()

#------------------------------------------------------------------------------

#putting data in place

fr=tk.Frame(lvl,width=450,height=35)
fr.place(x=160,y=100)
l1=tk.Label(fr,text=welcome1)
l1.configure(bg="grey",fg="white",justify="center",font=("Poor Richard",17), height=0,width=0)
l1.place(x=0,y=0)

fr2=tk.Frame(lvl,width=450,height=118)
fr2.place(x=165,y=150)
l2=tk.Label(fr2,text=welcome2)
l2.configure(bg="silver",fg="black",justify="center",font=("Poor Richard",15))
l2.place(x=0,y=0)

#------------------------------------------------------------------------------

#defining start
def start():
    
    lvl.destroy()
    top=tk.Tk()
    top.geometry("600x300")
    top.config(bg="silver")
    h="Choose the type of examination:"
    mss=tk.Message(top,text=h)
    mss.configure(bg="dimgrey",fg="white",justify="right",font=("Poor Richard",25),aspect=1000,relief="sunken")
    mss.pack(fill=tk.X)
    b1=tk.Button(top,text="Unit Test",command=unittest,bg="paleturquoise",font=("times",15),width=9,height=1)
    b2=tk.Button(top,text="Half Yearly",command=halfyearly,bg="lightcyan",font=("times",15),height=1)
    b3=tk.Button(top,text="Finals",command=finals,bg="azure",font=("times",15),height=1,width=9)
    b1.place(x=250,y=70)
    b2.place(x=250,y=140)
    b3.place(x=250,y=210)

#------------------------------------------------------------------------------
    
#start/exit commands
fr3=tk.Frame(lvl,width=200,height=220)
fr3.place(x=300,y=300)
butt1=tk.Button(fr3,text="Start",command=start)
butt1.configure(height=5,width=22,bg="gainsboro",font=("times",8))
butt1.place(x=20,y=10)
butt2=tk.Button(fr3,text="Exit",command=lvl.destroy)
butt2.configure(height=5,width=22,bg="whitesmoke",font=("times", 8))
butt2.place(x=20,y=110)


