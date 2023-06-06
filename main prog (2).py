import tkinter as tk

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

    

def unittest():
    def des():
        m.destroy()
        uts()
    import tkinter as tk
    from tkinter import ttk
    m=tk.Tk()
    m.geometry("800x200")
    f5=open("disclaimer.txt","r")
    disclaim=f5.read()
    f5.close()
    msg=tk.Message(m,text=disclaim)
    msg.configure(font=("Poor Richard",21),aspect=1000,relief="sunken")
    msg.pack(fill=tk.X)
    btn=tk.Button(m,text="Dismiss",command=des)
    btn.pack()

    
    def uts():
        global cnt
        cnt=0
        ut=tk.Tk()
        ut.title("Values")
        ut.geometry("1100x800")
        
        #entry widgets for various values
        u1=tk.Entry(ut)
        u2=tk.Entry(ut)
        u3=tk.Entry(ut)
        u4=tk.Entry(ut)
        u5=tk.Entry(ut)
        u6=tk.Entry(ut)
        u7=tk.Entry(ut)
        u8=tk.Entry(ut)
        u9=tk.Entry(ut)
        u10=tk.Entry(ut)
        u11=tk.Entry(ut)
        u12=tk.Entry(ut)
        u13=tk.Entry(ut)
        u14=tk.Entry(ut)
        u15=tk.Entry(ut)
        u16=tk.Entry(ut)
        u17=tk.Entry(ut)
        u18=tk.Entry(ut)
        u19=tk.Entry(ut)
        u20=tk.Entry(ut)
        u21=tk.Entry(ut)
        u22=tk.Entry(ut)
        u23=tk.Entry(ut)
        u24=tk.Entry(ut)

        #entry for name of organisation
        tk.Label(ut,text="Name of organisation").grid(row=0,column=0)
        u1.grid(row=0,column=1)

        #entry of name
        tk.Label(ut,text="Name of Student").grid(row=1,column=0)
        u2.grid(row=1,column=1)

        #entry of adm no
        tk.Label(ut,text="Admission No.").grid(row=1,column=2)
        u3.grid(row=1,column=3)

        #entry of class
        tk.Label(ut,text="Class").grid(row=1,column=4)
        OPTIONS = [1,2,3,4,5,6,7,8,9,10,"11-PCM","11-PCB","11-COMMERCE","11-ARTS","12-PCM","12-PCB","12-COMMERCE","12-ARTS"]
        variable = tk.StringVar(ut)
        variable.set("select class")
        w = tk.OptionMenu(ut, variable, *OPTIONS)
        w.grid(row=1,column=5)
        global cks

        # entry of subject names
        tk.Label(ut, text="Subject").grid(row=4, column=3)  
        u7.grid(row=10, column=3)
        
        def confirm():
            global cnt
            cnt=cnt+1
            global clsss
            
            clsss=(variable.get())
            global aa1,aa2,aa3,aa4,aa5
            if cnt>1:
                    aa1.destroy()
                    aa2.destroy()
                    aa3.destroy()
                    aa4.destroy()
                    try:
                        aa5.destroy()
                    except:
                        pass
            
            try:
                
                
                if int(clsss)>=1 and int(clsss)<=5:
                    
                    aa1=tk.Label(ut, text="English")
                    aa2=tk.Label(ut, text="Maths")
                    aa3=tk.Label(ut, text="EVS")
                    aa4=tk.Label(ut, text="Computers")
                    aa5=tk.Label(ut, text="\t    Hindi   \t")
                elif int(clsss)>=6 and int(clsss)<=10:
                    aa1=tk.Label(ut, text="English")
                    aa2=tk.Label(ut, text="Maths")
                    aa3=tk.Label(ut, text="Science")
                    aa4=tk.Label(ut, text="Social Science")
                    aa5=tk.Label(ut, text="\t    Hindi   \t")
                aa1.grid(row=5, column=3)
                aa2.grid(row=6, column=3)
                aa3.grid(row=7, column=3)
                aa4.grid(row=8, column=3)
                aa5.grid(row=9, column=3)
            except:
                
                if clsss=="11-PCM" or clsss=="12-PCM":
                    aa1=tk.Label(ut, text="English")
                    aa2=tk.Label(ut, text="Maths")
                    aa3=tk.Label(ut, text="Chemistry")
                    aa4=tk.Label(ut, text="Physics")
                    
                elif clsss=="11-PCB" or clsss=="12-PCB":
                    aa1=tk.Label(ut, text="English")
                    aa2=tk.Label(ut, text="Biology")
                    aa3=tk.Label(ut, text="Chemistry")
                    aa4=tk.Label(ut, text="Physics")
                    
                elif clsss=="11-COMMERCE" or clsss=="12-COMMERCE":
                    aa1=tk.Label(ut, text="English")
                    aa2=tk.Label(ut, text="Accountancy")
                    aa3=tk.Label(ut, text="Business Studies")
                    aa4=tk.Label(ut, text="Economics")
                    
                elif clsss=="11-ARTS" or clsss=="12-ARTS":
                    aa1=tk.Label(ut, text="English")
                    aa2=tk.Label(ut, text="History")
                    aa3=tk.Label(ut, text="Political Science")
                    aa4=tk.Label(ut, text="Geography")
                    
                aa1.grid(row=5, column=3)
                aa2.grid(row=6, column=3)
                aa3.grid(row=7, column=3)
                aa4.grid(row=8, column=3)
                u10.grid(row=9, column=3)
                
        
        BTN=tk.Button(ut,text="Confirm Class",command=confirm)
        BTN.grid(row=1,column=6)
        

        

        #entry of section
        tk.Label(ut,text="Section").grid(row=2,column=0)
        u4.grid(row=2,column=1)

        #entry of roll no.
        tk.Label(ut,text="Roll Number").grid(row=2,column=3)
        def sel():
            selection = "Roll Number = " + str(scale.get())
            label.config(text = selection)
        var = tk.DoubleVar()
        scale = tk.Scale(ut,from_=1,to=100,variable=var )
        scale.grid(row=2,column=4)
        button = tk.Button(ut, text="Confirm Roll No.", command=sel)
        button.grid(row=2,column=6)
        label = tk.Label(ut)
        label.grid(row=2,column=5)
        
        #entry of FATHERS NAME
        tk.Label(ut, text="Father's Name").grid(row=3, column=0)
        u5.grid(row=3,column=1)
        
        #entry of mothers name
        tk.Label(ut, text="Mother's Name").grid(row=3, column=3)
        u6.grid(row=3,column=4)

        # entry of serial numbers
        tk.Label(ut, text="Srl.No").grid(row=4, column=1)
        tk.Label(ut, text="1").grid(row=5, column=1)
        tk.Label(ut, text="2").grid(row=6, column=1)
        tk.Label(ut, text="3").grid(row=7, column=1)
        tk.Label(ut, text="4").grid(row=8, column=1)
        tk.Label(ut, text="5").grid(row=9, column=1)
        tk.Label(ut, text="6").grid(row=10, column=1)

     
            

        # entry of marks scored
        tk.Label(ut, text="Marks Obtained").grid(row=4, column=4)  
        u12.grid(row=5, column=4) 
        u13.grid(row=6, column=4) 
        u14.grid(row=7, column=4) 
        u15.grid(row=8, column=4) 
        u16.grid(row=9, column=4)
        u8.grid(row=10, column=4)

        # entry of Total marks
        tk.Label(ut, text="Total Marks").grid(row=4, column=5)
        u17.grid(row=5, column=5)
        u18.grid(row=6, column=5)
        u19.grid(row=7, column=5)
        u20.grid(row=8, column=5)
        u21.grid(row=9, column=5)
        u9.grid(row=10, column=5)

        # entry of teachers remarks
        tk.Label(ut, text="Teacher's Remarks").grid(row=11, column=0)
        u22.grid(row=11,column=1)

        # entry of teachers name
        tk.Label(ut, text="Teacher's Name").grid(row=12, column=0)
        u23.grid(row=12,column=1)

        # entry of date
        tk.Label(ut, text="Date").grid(row=13, column=0)
        u24.grid(row=13,column=1)

        #\colours
        
        #header
        header=tk.Label(ut,text="choose header colour:").grid(row=16,column=0)
        global ii
        global jj
        global kk
        ii=tk.IntVar(ut)
        r1=tk.Radiobutton(ut,text="white",value=1,variable=ii).grid(row=17,column=0)
        r2=tk.Radiobutton(ut,text="purple",value=2,variable=ii).grid(row=17,column=1)
        r3=tk.Radiobutton(ut,text="blue",value=3,variable=ii).grid(row=17,column=2)
        r4=tk.Radiobutton(ut,text="green",value=4,variable=ii).grid(row=17,column=3)
        r5=tk.Radiobutton(ut,text="orange",value=5,variable=ii).grid(row=17,column=4)
        r6=tk.Radiobutton(ut,text="yellow",value=6,variable=ii).grid(row=17,column=5)

        #background
        backg=tk.Label(ut,text="choose background colour:").grid(row=18,column=0)
        jj=tk.IntVar(ut)
        r11=tk.Radiobutton(ut,text="white",value=1,variable=jj).grid(row=19,column=0)
        r22=tk.Radiobutton(ut,text="purple",value=2,variable=jj).grid(row=19,column=1)
        r33=tk.Radiobutton(ut,text="blue",value=3,variable=jj).grid(row=19,column=2)
        r44=tk.Radiobutton(ut,text="green",value=4,variable=jj).grid(row=19,column=3)
        r55=tk.Radiobutton(ut,text="orange",value=5,variable=jj).grid(row=19,column=4)
        r66=tk.Radiobutton(ut,text="yellow",value=6,variable=jj).grid(row=19,column=5)

        #foreground
        backg=tk.Label(ut,text="choose details colour:").grid(row=20,column=0)
        kk=tk.IntVar(ut)
        r22=tk.Radiobutton(ut,text="white",value=2,variable=kk).grid(row=21,column=1)
        r22=tk.Radiobutton(ut,text="grey",value=3,variable=kk).grid(row=21,column=2)
        

        def reset():
            u1.delete(0,tk.END)
            u2.delete(0,tk.END)
            u3.delete(0,tk.END)
            u4.delete(0,tk.END)
            u5.delete(0,tk.END)
            u6.delete(0,tk.END)
            u7.delete(0,tk.END)
            u8.delete(0,tk.END)
            u9.delete(0,tk.END)
            u10.delete(0,tk.END)
            u11.delete(0,tk.END)
            u12.delete(0,tk.END)
            u13.delete(0,tk.END)
            u14.delete(0,tk.END)
            u15.delete(0,tk.END)
            u16.delete(0,tk.END)
            u17.delete(0,tk.END)
            u18.delete(0,tk.END)
            u19.delete(0,tk.END)
            u20.delete(0,tk.END)
            u21.delete(0,tk.END)
            u22.delete(0,tk.END)
            u23.delete(0,tk.END)
            u24.delete(0,tk.END)
            aa1.destroy()
            aa2.destroy()
            aa3.destroy()
            aa4.destroy()
            try:
                aa5.destroy()
            except:
                pass

        def heh():
            opt=1
            clsss=variable.get()
            if u7.get()=="":
                opt=0
            if ii.get()==1:
                head="white"
            elif ii.get()==2:
                head="mediumpurple"
            elif ii.get()==3:
                head="cornflowerblue"
            elif ii.get()==4:
                head="limegreen"
            elif ii.get()==5:
                head="darkorange"
            else:
                head="goldenrod"
            if jj.get()==1:
                back="white"
            elif jj.get()==2:
                back="thistle"
            elif jj.get()==3:
                back="powderblue"
            elif jj.get()==4:
                back="limegreen"
            elif jj.get()==5:
                back="sandybrown"
            else:
                back="khaki"
            if kk.get()==2:
                fore="white"
            else:
                fore="grey"

            f=tk.Tk()
            f.title("Report Card")
            f.geometry("1000x800")
            f.config(bg=back)
            sc=tk.Scrollbar(f)
            sc.configure(command=f)

            #putting in org name, test name and student details
            
            if clsss in ["11-PCM","11-PCB","11-COMMERCE","11-ARTS"]:
                itsi="11"
            elif clsss in ["12-PCM","12-PCB","12-COMMERCE","12-ARTS"]:
                itsi="12"
            else:
                itsi=str(clsss)
            mhmk=tk.Frame(f,width=215,height=85,bg="white")
            mhmk.grid(row=0,column=2,columnspan=2)
            l=u1.get()+"\n"+"UNIT TEST"
            m=tk.Message(mhmk,text=l)
            m.configure(font=("times",22,"bold"),bg=head,justify="center",aspect=1000,relief="groove")
            m.place(x=0,y=0)
            lol=tk.Frame(f,width=1000,height=200,bg=fore)
            lol.grid(row=2,columnspan=6)
            h="Name:"+u2.get()+"\n"+"Class-Sec:"+itsi+" "+u4.get()+"\n"+"Father's Name:"+u5.get()
            k="Admission No.:"+u3.get()+"\n"+"Roll No.:"+str(scale.get())+"\n"+"Mother's Name:"+u6.get()
            mg=tk.Message(lol,text=h)
            mg.configure(font=("times",23),bg=fore,aspect=1000,relief="raised")
            mg.place(x=0,y=20)
            mh=tk.Message(lol,text=k)
            mh.configure(font=("times",23),bg=fore,aspect=1000,relief="raised")
            mh.place(x=500,y=20)

            #serial num
            tk.Label(f, text="Srl.No",font=("times",15),justify="left",relief="sunken",bg=head).grid(row=4, column=0)
            tk.Label(f, text="1",font=("times",15)).grid(row=5, column=0)
            tk.Label(f, text="2",font=("times",15)).grid(row=6, column=0)
            tk.Label(f, text="3",font=("times",15)).grid(row=7, column=0)
            tk.Label(f, text="4",font=("times",15)).grid(row=8, column=0)
            tk.Label(f, text="5",font=("times",15)).grid(row=9, column=0)
            if opt!=0:
                tk.Label(f, text="6",font=("times",15)).grid(row=10, column=0)


            #subj
            tk.Label(f, text="Subject",font=("times",15),relief="sunken",bg=head).grid(row=4, column=1)
            try:
                if int(clsss)>=1 and int(clsss)<=5:
                    tk.Label(f, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(f, text="Maths",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(f, text="EVS",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(f, text="Computers",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(f, text="Hindi",font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif int(clsss)>=6 and int(clsss)<=10:
                    tk.Label(f, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(f, text="Maths",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(f, text="Science",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(f, text="Social Science",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(f, text="Hindi",font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
            except:
                if clsss=="11-PCM" or clsss=="12-PCM":
                    tk.Label(f, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(f, text="Maths",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(f, text="Chemistry",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(f, text="Physics",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(f, text=u10.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif clsss=="11-PCB" or clsss=="12-PCB":
                    tk.Label(f, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(f, text="Biology",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(f, text="Chemistry",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(f, text="Physics",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(f, text=u10.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif clsss=="11-COMMERCE" or clsss=="12-COMMERCE":
                    tk.Label(f, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(f, text="Accountancy",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(f, text="Business Studies",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(f, text="Economics",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(f, text=u10.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif clsss=="11-ARTS" or clsss=="12-ARTS" :
                    tk.Label(f, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(f, text="History",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(f, text="Political Science",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(f, text="Geography",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(f, text=u10.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
            if opt!=0:
                tk.Label(f, text=u7.get(),font=("times",15),relief="sunken",bg=head).grid(row=10, column=1)
                                                        

            #marks scored
            tk.Label(f, text="Marks Obtained",font=("times",15),relief="sunken",bg=head).grid(row=4, column=2)
            tk.Label(f, text=u12.get(),font=("times",15)).grid(row=5, column=2)
            tk.Label(f, text=u13.get(),font=("times",15)).grid(row=6, column=2)
            tk.Label(f, text=u14.get(),font=("times",15)).grid(row=7, column=2)
            tk.Label(f, text=u15.get(),font=("times",15)).grid(row=8, column=2)
            tk.Label(f, text=u16.get(),font=("times",15)).grid(row=9, column=2)
            if opt!=0:
                tk.Label(f, text=u8.get(),font=("times",15)).grid(row=10, column=2)
            
            #total marks
            tk.Label(f, text="Total Marks",font=("times",15),relief="sunken",bg=head).grid(row=4, column=3)
            tk.Label(f, text=u17.get(),font=("times",15)).grid(row=5, column=3)
            tk.Label(f, text=u18.get(),font=("times",15)).grid(row=6, column=3)
            tk.Label(f, text=u19.get(),font=("times",15)).grid(row=7, column=3)
            tk.Label(f, text=u20.get(),font=("times",15)).grid(row=8, column=3)
            tk.Label(f, text=u21.get(),font=("times",15)).grid(row=9, column=3)
            if opt!=0:
                tk.Label(f, text=u9.get(),font=("times",15)).grid(row=10, column=3)

            #grades
            tk.Label(f, text="Grade",font=("times",15),relief="sunken",bg=head).grid(row=4, column=4)

            #status
            tk.Label(f, text="Status",font=("times",15),relief="sunken",bg=head).grid(row=4, column=5)
    
            b=int(u17.get())
            if int(u12.get())>=0.9*b:
                tk.Label(f, text ="A",font=("times",15)).grid(row=5, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=5, column=5)
            elif int(u12.get()) >= 0.7 *b:
                tk.Label(f, text ="B",font=("times",15)).grid(row=5, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=5, column=5)
            elif int(u12.get()) >= 0.5* b:
                tk.Label(f, text ="C",font=("times",15)).grid(row=5, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=5, column=5)
            elif int(u12.get()) >= 0.4*b:
                tk.Label(f, text ="D",font=("times",15)).grid(row=5, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=5, column=5)
            elif int(u12.get()) >= 0.33*b:
                tk.Label(f, text ="E",font=("times",15)).grid(row=5, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=5, column=5)
            else:
                tk.Label(f, text ="F",font=("times",15)).grid(row=5, column=4)
                tk.Label(f, text ="FAIL",font=("times",15),fg="red").grid(row=5, column=5)


            c=int(u18.get())
            if int(u13.get())>=0.9*c:
                tk.Label(f, text ="A",font=("times",15)).grid(row=6, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=6, column=5)
            elif int(u13.get()) >= 0.7 *c:
                tk.Label(f, text ="B",font=("times",15)).grid(row=6, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=6, column=5)
            elif int(u13.get()) >= 0.5* c:
                tk.Label(f, text ="C",font=("times",15)).grid(row=6, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=6, column=5)
            elif int(u13.get()) >= 0.4*c:
                tk.Label(f, text ="D",font=("times",15)).grid(row=6, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=6, column=5)
            elif int(u13.get()) >= 0.33*c:
                tk.Label(f, text ="E",font=("times",15)).grid(row=6, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=6, column=5)
            else:
                tk.Label(f, text ="F",font=("times",15)).grid(row=6, column=4)
                tk.Label(f, text ="FAIL",font=("times",15),fg="red").grid(row=6, column=5)

            d=int(u19.get())
            if int(u14.get())>=0.9*d:
                tk.Label(f, text ="A",font=("times",15)).grid(row=7, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=7, column=5)
            elif int(u14.get()) >= 0.7 *d:
                tk.Label(f, text ="B",font=("times",15)).grid(row=7, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=7, column=5)
            elif int(u14.get()) >= 0.5* d:
                tk.Label(f, text ="C",font=("times",15)).grid(row=7, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=7, column=5)
            elif int(u14.get()) >= 0.4*d:
                tk.Label(f, text ="D",font=("times",15)).grid(row=7, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=7, column=5)
            elif int(u14.get()) >= 0.33*d:
                tk.Label(f, text ="E",font=("times",15)).grid(row=7, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=7, column=5)
            else:
                tk.Label(f, text ="F",font=("times",15)).grid(row=7, column=4)
                tk.Label(f, text ="FAIL",font=("times",15),fg="red").grid(row=7, column=5)

            e=int(u20.get())
            if int(u15.get())>=0.9*e:
                tk.Label(f, text ="A",font=("times",15)).grid(row=8, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=8, column=5)
            elif int(u15.get()) >= 0.7 *e:
                tk.Label(f, text ="B",font=("times",15)).grid(row=8, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=8, column=5)
            elif int(u15.get()) >= 0.5* e:
                tk.Label(f, text ="C",font=("times",15)).grid(row=8, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=8, column=5)
            elif int(u15.get()) >= 0.4*e:
                tk.Label(f, text ="D",font=("times",15)).grid(row=8, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=8, column=5)
            elif int(u15.get()) >= 0.33*e:
                tk.Label(f, text ="E",font=("times",15)).grid(row=8, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=8, column=5)
            else:
                tk.Label(f, text ="F",font=("times",15)).grid(row=8, column=4)
                tk.Label(f, text ="FAIL",font=("times",15),fg="red").grid(row=8, column=5)
                


            f1=int(u21.get())
            if int(u16.get())>=0.9*f1:
                tk.Label(f, text ="A",font=("times",15)).grid(row=9, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=9, column=5)
            elif int(u16.get()) >= 0.7 *f1:
                tk.Label(f, text ="B",font=("times",15)).grid(row=9, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=9, column=5)
            elif int(u16.get()) >= 0.5* f1:
                tk.Label(f, text ="C",font=("times",15)).grid(row=9, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=9, column=5)
            elif int(u16.get()) >= 0.4*f1:
                tk.Label(f, text ="D",font=("times",15)).grid(row=9, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=9, column=5)
            elif int(u16.get()) >= 0.33*f1:
                tk.Label(f, text ="E",font=("times",15)).grid(row=9, column=4)
                tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=9, column=5)
            else:
                tk.Label(f, text ="F",font=("times",15)).grid(row=9, column=4)
                tk.Label(f, text ="FAIL",font=("times",15),fg="red").grid(row=9, column=5)

            if opt!=0:
                g1=int(u9.get())
                if int(u8.get())>=0.9*g1:
                    tk.Label(f, text ="A",font=("times",15)).grid(row=10, column=4)
                    tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=10, column=5)
                elif int(u8.get()) >= 0.7 *g1:
                    tk.Label(f, text ="B",font=("times",15)).grid(row=10, column=4)
                    tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=10, column=5)
                elif int(u8.get()) >= 0.5* g1:
                    tk.Label(f, text ="C",font=("times",15)).grid(row=10, column=4)
                    tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=10, column=5)
                elif int(u8.get()) >= 0.4*g1:
                    tk.Label(f, text ="D",font=("times",15)).grid(row=10, column=4)
                    tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=10, column=5)
                elif int(u8.get()) >= 0.33*g1:
                    tk.Label(f, text ="E",font=("times",15)).grid(row=10, column=4)
                    tk.Label(f, text ="PASS",font=("times",15),fg="green").grid(row=10, column=5)
                else:
                    tk.Label(f, text ="F",font=("times",15)).grid(row=10, column=4)
                    tk.Label(f, text ="FAIL",font=("times",15),fg="red").grid(row=10, column=5)
            
            #to display total marks obtsained
            if opt==0:
                tot=int(u12.get())+int(u13.get())+int(u14.get())+int(u15.get())+int(u16.get())
            else:
                tot=int(u12.get())+int(u13.get())+int(u14.get())+int(u15.get())+int(u16.get())+int(u8.get())
                
            tk.Label(f, text=(tot),font=("times",15),relief="flat",bg=head).grid(row=11, column=2)

            # to display total scored
            if opt==0:
                tot1=int(u17.get())+int(u18.get())+int(u19.get())+int(u20.get())+int(u21.get())
            else:
                tot1=int(u17.get())+int(u18.get())+int(u19.get())+int(u20.get())+int(u21.get())+int(u9.get())
            tk.Label(f, text=(tot1),font=("times",15),relief="flat",bg=head).grid(row=11, column=3)

            #to display percentage
            per=(tot/tot1)*100
            tk.Label(f, text=str(per),font=("times",15),bg=head,relief="flat").grid(row=12, column=2)
            tk.Label(f, text="Total:",font=("times",15),relief="flat",bg=head).grid(row=11, column=1)
            tk.Label(f, text="Percentage",font=("times",15),bg=head,relief="flat").grid(row=12, column=1)

            #teachers remarks
            tk.Label(f, text="Teacher's Remarks",font=("times",15),bg=head).grid(row=14, column=0)
            tk.Label(f, text=u22.get(),font=("times",15)).grid(row=16, column=0)

            #teachers name
            tk.Label(f, text="Teacher's Name",font=("times",15),bg=head).grid(row=14, column=2)
            tk.Label(f, text=u23.get(),font=("times",15)).grid(row=16, column=2)

            #date
            tk.Label(f, text="Date",font=("times",15),bg=head).grid(row=14, column=5)
            tk.Label(f, text=u24.get(),font=("times",15)).grid(row=16, column=5)

            #button to go back
            n2=tk.Button(f, text="Back",font=("times",15), bg="blue",fg="white", command=f.destroy) 
            n2.grid(row=18, column=3)

        # button to display completed report card 
        bn1=tk.Button(ut, text="Generate", bg="green", command=heh) 
        bn1.grid(row=22, column=0)

        # button to reset
        bn2=tk.Button(ut, text="Reset", bg="red", command=reset) 
        bn2.grid(row=22, column=3)

        # button to go back to main menu
        bn2=tk.Button(ut, text="Back", bg="blue",fg="white", command=ut.destroy) 
        bn2.grid(row=22, column=5)
        ut.mainloop()
        
def halfyearly():
    
    def des():
        m.destroy()
        hys()
        
    m=tk.Tk()
    m.geometry("800x200")
    f5=open("disclaimer.txt","r")
    disclaim=f5.read()
    f5.close()
    msg=tk.Message(m,text=disclaim)
    msg.configure(font=("Poor Richard",21),aspect=1000,relief="sunken")
    msg.pack(fill=tk.X)
    btn=tk.Button(m,text="Dismiss",command=des)
    btn.pack()
    
    def hys():
        global cnt
        cnt=0
        ok=tk.Tk()
        ok.title("HALF YEARLY")
        ok.geometry("1300x700")
        f1=tk.Entry(ok)
        f2=tk.Entry(ok)
        f3=tk.Entry(ok)
        f4=tk.Entry(ok)
        f5=tk.Entry(ok)
        f6=tk.Entry(ok)
        f7=tk.Entry(ok)
        f8=tk.Entry(ok)
        f9=tk.Entry(ok)
        f10=tk.Entry(ok)
        f11=tk.Entry(ok)
        f12=tk.Entry(ok)
        f13=tk.Entry(ok)
        f14=tk.Entry(ok)
        f15=tk.Entry(ok)
        f16=tk.Entry(ok)
        f17=tk.Entry(ok)
        f18=tk.Entry(ok)
        f19=tk.Entry(ok)
        f20=tk.Entry(ok)
        f21=tk.Entry(ok)
        f22=tk.Entry(ok)
        f23=tk.Entry(ok)
        f24=tk.Entry(ok)
        f25=tk.Entry(ok)
        f26=tk.Entry(ok)
        f27=tk.Entry(ok)
        f28=tk.Entry(ok)
        f29=tk.Entry(ok)
        f30=tk.Entry(ok)
        f31=tk.Entry(ok)
        f32=tk.Entry(ok)
        f33=tk.Entry(ok)
        f34=tk.Entry(ok)
        f35=tk.Entry(ok)
        f36=tk.Entry(ok)
        f37=tk.Entry(ok)
        f38=tk.Entry(ok)
        f39=tk.Entry(ok)
        f40=tk.Entry(ok)
        f41=tk.Entry(ok)
        f42=tk.Entry(ok)
        f43=tk.Entry(ok)
        f44=tk.Entry(ok)
        f45=tk.Entry(ok)
        f46=tk.Entry(ok)

        #entry for name of organisation
        tk.Label(ok,text="Name of organisation").grid(row=0,column=0)
        f1.grid(row=0,column=1)

        #entry of name
        tk.Label(ok,text="Name of Student").grid(row=1,column=0)
        f2.grid(row=1,column=1)

        #entry of adm no
        tk.Label(ok,text="Admission Number").grid(row=1,column=2)
        f3.grid(row=1,column=3)

        #entry of class
        tk.Label(ok,text="Class").grid(row=1,column=4)
        OPTIONS = [1,2,3,4,5,6,7,8,9,10,"11-PCM","11-PCB","11-COMMERCE","11-ARTS","12-PCM","12-PCB","12-COMMERCE","12-ARTS"]
        variable1 = tk.StringVar(ok)
        variable1.set("select class")
        w = tk.OptionMenu(ok, variable1, *OPTIONS)
        w.grid(row=1,column=5)

        # entry of subject names
        tk.Label(ok, text="Subject").grid(row=4, column=3)  
        f42.grid(row=10, column=3)
        
        def confirm():
            global cnt
            cnt=cnt+1
            global clsss
            
            clsss=(variable1.get())
            global aa1,aa2,aa3,aa4,aa5
            if cnt>1:
                    aa1.destroy()
                    aa2.destroy()
                    aa3.destroy()
                    aa4.destroy()
                    try:
                        aa5.destroy()
                    except:
                        pass
            
            try:
                
                
                if int(clsss)>=1 and int(clsss)<=5:
                    
                    aa1=tk.Label(ok, text="English")
                    aa2=tk.Label(ok, text="Maths")
                    aa3=tk.Label(ok, text="EVS")
                    aa4=tk.Label(ok, text="Computers")
                    aa5=tk.Label(ok, text="\t    Hindi   \t")
                elif int(clsss)>=6 and int(clsss)<=10:
                    aa1=tk.Label(ok, text="English")
                    aa2=tk.Label(ok, text="Maths")
                    aa3=tk.Label(ok, text="Science")
                    aa4=tk.Label(ok, text="Social Science")
                    aa5=tk.Label(ok, text="\t    Hindi   \t")
                aa1.grid(row=5, column=1)
                aa2.grid(row=6, column=1)
                aa3.grid(row=7, column=1)
                aa4.grid(row=8, column=1)
                aa5.grid(row=9, column=1)
            except:
                
                if clsss=="11-PCM" or clsss=="12-PCM":
                    aa1=tk.Label(ok, text="English")
                    aa2=tk.Label(ok, text="Maths")
                    aa3=tk.Label(ok, text="Chemistry")
                    aa4=tk.Label(ok, text="Physics")
                    
                elif clsss=="11-PCB" or clsss=="12-PCB":
                    aa1=tk.Label(ok, text="English")
                    aa2=tk.Label(ok, text="Biology")
                    aa3=tk.Label(ok, text="Chemistry")
                    aa4=tk.Label(ok, text="Physics")
                    
                elif clsss=="11-COMMERCE" or clsss=="12-COMMERCE":
                    aa1=tk.Label(ok, text="English")
                    aa2=tk.Label(ok, text="Accountancy")
                    aa3=tk.Label(ok, text="Business Studies")
                    aa4=tk.Label(ok, text="Economics")

                elif clsss=="11-ARTS" or clsss=="12-ARTS":
                    aa1=tk.Label(ok, text="English")
                    aa2=tk.Label(ok, text="History")
                    aa3=tk.Label(ok, text="Political Science")
                    aa4=tk.Label(ok, text="Geography")
                aa1.grid(row=5, column=1)
                aa2.grid(row=6, column=1)
                aa3.grid(row=7, column=1)
                aa4.grid(row=8, column=1)
                f7.grid(row=9, column=1)
                
        
        BTN=tk.Button(ok,text="Confirm Class",command=confirm)
        BTN.grid(row=1,column=6)
        

        #entry of sec
        tk.Label(ok,text="Section").grid(row=2,column=0)
        f4.grid(row=2,column=1)

        #entry of roll no.
        tk.Label(ok,text="Roll Number").grid(row=2,column=3)
        def sel1():
            sel2 = "Roll Number = " + str(scale.get())
            label.config(text = sel2)
        var1 = tk.DoubleVar()
        scale = tk.Scale(ok,from_=1,to=100,variable=var1 )
        scale.grid(row=2,column=4)
        button = tk.Button(ok, text="Get Scale Value", command=sel1)
        button.grid(row=2,column=6)
        label = tk.Label(ok)
        label.grid(row=2,column=5)
        
        #entry of FATHERS NAME
        tk.Label(ok, text="Father's Name").grid(row=3, column=0)
        f5.grid(row=3,column=1)
        
        #entry of mothers name
        tk.Label(ok, text="Mother's Name").grid(row=3, column=3)
        f6.grid(row=3,column=4)

        # entry of serial numbers
        tk.Label(ok, text="Srl.No").grid(row=4, column=0)
        tk.Label(ok, text="1").grid(row=5, column=0)
        tk.Label(ok, text="2").grid(row=6, column=0)
        tk.Label(ok, text="3").grid(row=7, column=0)
        tk.Label(ok, text="4").grid(row=8, column=0)
        tk.Label(ok, text="5").grid(row=9, column=0)
        tk.Label(ok, text="6").grid(row=10, column=0)

        # entry of subject names
        tk.Label(ok, text="Subject").grid(row=4, column=1)
        f42.grid(row=10,column=1)
        

        #labels and entries for Ut
        tk.Label(ok, text="Marks Scored in UT-1").grid(row=4, column=2)
        f13.grid(row=5,column=2)
        f14.grid(row=6,column=2)
        f15.grid(row=7,column=2)
        f16.grid(row=8,column=2)
        f17.grid(row=9,column=2)
        f8.grid(row=10,column=2)

        tk.Label(ok, text="Total Marks in UT-1").grid(row=4, column=3)
        f18.grid(row=5,column=3)
        f19.grid(row=6,column=3)
        f20.grid(row=7,column=3)
        f21.grid(row=8,column=3)
        f22.grid(row=9,column=3)
        f9.grid(row=10,column=3)

        #labels and entries for Half Yearly
        tk.Label(ok, text="Marks Scored in HY").grid(row=4, column=4)
        f23.grid(row=5,column=4)
        f24.grid(row=6,column=4)
        f25.grid(row=7,column=4)
        f26.grid(row=8,column=4)
        f27.grid(row=9,column=4)
        f10.grid(row=10,column=4)

        tk.Label(ok, text="Total Marks in HY").grid(row=4, column=5)
        f28.grid(row=5,column=5)
        f29.grid(row=6,column=5)
        f30.grid(row=7,column=5)
        f31.grid(row=8,column=5)
        f32.grid(row=9,column=5)
        f11.grid(row=10,column=5)

        # entry of teachers remarks
        tk.Label(ok, text="Teacher's Remarks").grid(row=11, column=0)
        f33.grid(row=11,column=1)

        # entry of teachers name
        tk.Label(ok, text="Teacher's Name").grid(row=12, column=0)
        f34.grid(row=12,column=1)

        # entry of date
        tk.Label(ok, text="Date").grid(row=13, column=0)
        f35.grid(row=13,column=1)

        #\colours
        
        #header
        hea=tk.Label(ok,text="choose header colour:").grid(row=14,column=0)
        global ii
        global jj
        global kk
        iii=tk.IntVar(ok)
        ri1=tk.Radiobutton(ok,text="white",value=1,variable=iii).grid(row=15,column=0)
        ri2=tk.Radiobutton(ok,text="purple",value=2,variable=iii).grid(row=15,column=1)
        ri3=tk.Radiobutton(ok,text="blue",value=3,variable=iii).grid(row=15,column=2)
        ri4=tk.Radiobutton(ok,text="green",value=4,variable=iii).grid(row=15,column=3)
        ri5=tk.Radiobutton(ok,text="orange",value=5,variable=iii).grid(row=15,column=4)
        ri6=tk.Radiobutton(ok,text="yellow",value=6,variable=iii).grid(row=15,column=5)

        #background
        bac=tk.Label(ok,text="choose background colour:").grid(row=16,column=0)
        jjj=tk.IntVar(ok)
        ri11=tk.Radiobutton(ok,text="white",value=1,variable=jjj).grid(row=17,column=0)
        ri22=tk.Radiobutton(ok,text="purple",value=2,variable=jjj).grid(row=17,column=1)
        ri33=tk.Radiobutton(ok,text="blue",value=3,variable=jjj).grid(row=17,column=2)
        ri44=tk.Radiobutton(ok,text="green",value=4,variable=jjj).grid(row=17,column=3)
        ri55=tk.Radiobutton(ok,text="orange",value=5,variable=jjj).grid(row=17,column=4)
        ri66=tk.Radiobutton(ok,text="yellow",value=6,variable=jjj).grid(row=17,column=5)

        #foreground
        fo=tk.Label(ok,text="choose details colour:").grid(row=18,column=0)
        kkk=tk.IntVar(ok)
        rii11=tk.Radiobutton(ok,text="white",value=2,variable=kkk).grid(row=19,column=1)
        rii22=tk.Radiobutton(ok,text="grey",value=3,variable=kkk).grid(row=19,column=2)

        def reset():
            f1.delete(0,tk.END)
            f2.delete(0,tk.END)
            f3.delete(0,tk.END)
            f4.delete(0,tk.END)
            f5.delete(0,tk.END)
            f6.delete(0,tk.END)
            f7.delete(0,tk.END)
            f8.delete(0,tk.END)
            f9.delete(0,tk.END)
            f10.delete(0,tk.END)
            f11.delete(0,tk.END)
            f12.delete(0,tk.END)
            f13.delete(0,tk.END)
            f14.delete(0,tk.END)
            f15.delete(0,tk.END)
            f16.delete(0,tk.END)
            f17.delete(0,tk.END)
            f18.delete(0,tk.END)
            f19.delete(0,tk.END)
            f20.delete(0,tk.END)
            f21.delete(0,tk.END)
            f22.delete(0,tk.END)
            f23.delete(0,tk.END)
            f24.delete(0,tk.END)
            f25.delete(0,tk.END)
            f26.delete(0,tk.END)
            f27.delete(0,tk.END)
            f28.delete(0,tk.END)
            f29.delete(0,tk.END)
            f30.delete(0,tk.END)
            f31.delete(0,tk.END)
            f32.delete(0,tk.END)
            f33.delete(0,tk.END)
            f34.delete(0,tk.END)
            f35.delete(0,tk.END)
            f42.delete(0,tk.END)
            aa1.destroy()
            aa2.destroy()
            aa3.destroy()
            aa4.destroy()
            try:
                aa5.destroy()
            except:
                pass

        def heh():
            opt=1
            clsss=variable1.get()
            if f42.get()=="":
                opt=0
            if iii.get()==1:
                head="white"
            elif iii.get()==2:
                head="mediumpurple"
            elif iii.get()==3:
                head="cornflowerblue"
            elif iii.get()==4:
                head="limegreen"
            elif iii.get()==5:
                head="darkorange"
            else:
                head="goldenrod"
            if jjj.get()==1:
                back="white"
            elif jjj.get()==2:
                back="thistle"
            elif jjj.get()==3:
                back="powderblue"
            elif jjj.get()==4:
                back="limegreen"
            elif jjj.get()==5:
                back="sandybrown"
            else:
                back="khaki"
            if kkk.get()==2:
                fore="white"
            else:
                fore="grey"

            fg=tk.Tk()
            fg.title("Report Card")
            fg.geometry("1250x800")
            fg.config(bg=back)
            
            #putting in org name, test name and student details
            if clsss in ["11-PCM","11-PCB","11-COMMERCE","11-ARTS"]:
                itsi="11"
            elif clsss in ["12-PCM","12-PCB","12-COMMERCE","12-ARTS"]:
                itsi="12"
            else:
                itsi=str(clsss)
            mhmkm=tk.Frame(fg,width=200,height=65,bg="white")
            mhmkm.grid(row=0,column=3,columnspan=2)
            l=f1.get()+"\n"+"HALF YEARLY"
            m1=tk.Message(mhmkm,text=l)
            m1.configure(font=("times",15,"bold"),bg=head,justify="center",aspect=1000,relief="groove")
            m1.place(x=0,y=0)
            lool=tk.Frame(fg,width=1000,height=200,bg=fore)
            lool.grid(row=2,columnspan=8)
            hf="Name:"+f2.get()+"\n"+"Class-Sec:"+itsi+" "+f4.get()+"\n"+"Father's Name:"+f5.get()
            kf="Admission No.:"+f3.get()+"\n"+"Roll No.:"+str(scale.get())+"\n"+"Mother's Name:"+f6.get()
            mg=tk.Message(lool,text=hf)
            mg.configure(font=("times",23),bg=fore,aspect=1000,relief="raised")
            mg.place(x=0,y=20)
            mh=tk.Message(lool,text=kf)
            mh.configure(font=("times",23),bg=fore,aspect=1000,relief="raised")
            mh.place(x=500,y=20)

            #serial num
            tk.Label(fg, text="Srl.No",font=("times",15),justify="left",relief="sunken",bg=head).grid(row=4, column=0)
            tk.Label(fg, text="1",font=("times",15)).grid(row=5, column=0)
            tk.Label(fg, text="2",font=("times",15)).grid(row=6, column=0)
            tk.Label(fg, text="3",font=("times",15)).grid(row=7, column=0)
            tk.Label(fg, text="4",font=("times",15)).grid(row=8, column=0)
            tk.Label(fg, text="5",font=("times",15)).grid(row=9, column=0)
            if opt!=0:
                tk.Label(fg, text="6",font=("times",15)).grid(row=10, column=0)

            #subj
            tk.Label(fg, text="Subject",font=("times",15),relief="sunken",bg=head).grid(row=4, column=1)
            
            try:
                if int(clsss)>=1 and int(clsss)<=5:
                    tk.Label(fg, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(fg, text="Maths",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(fg, text="EVS",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(fg, text="Computers",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(fg, text="Hindi",font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif int(clsss)>=6 and int(clsss)<=10:
                    tk.Label(fg, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(fg, text="Maths",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(fg, text="Science",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(fg, text="Social Science",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(fg, text="Hindi",font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
            except:
                if clsss=="11-PCM" or clsss=="12-PCM":
                    tk.Label(fg, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(fg, text="Maths",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(fg, text="Chemistry",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(fg, text="Physics",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(fg, text=f7.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif clsss=="11-PCB" or clsss=="12-PCB":
                    tk.Label(fg, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(fg, text="Biology",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(fg, text="Chemistry",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(fg, text="Physics",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(fg, text=f7.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif clsss=="11-COMMERCE" or clsss=="12-COMMERCE":
                    tk.Label(fg, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(fg, text="Accountancy",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(fg, text="Business Studies",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(fg, text="Economics",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(fg, text=f7.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif clsss=="11-ARTS" or clsss=="12-ARTS" :
                    tk.Label(fg, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(fg, text="History",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(fg, text="Political Science",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(fg, text="Geography",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(fg, text=f7.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
            if opt!=0:
                tk.Label(fg, text=f42.get(),font=("times",15),relief="sunken",bg=head).grid(row=10, column=1)

            #marks scored in ut
            tk.Label(fg, text="Marks Scored in UT-1",font=("times",15),relief="sunken",bg=head).grid(row=4, column=2)
            tk.Label(fg, text=f13.get(),font=("times",15)).grid(row=5, column=2)
            tk.Label(fg, text=f14.get(),font=("times",15)).grid(row=6, column=2)
            tk.Label(fg, text=f15.get(),font=("times",15)).grid(row=7, column=2)
            tk.Label(fg, text=f16.get(),font=("times",15)).grid(row=8, column=2)
            tk.Label(fg, text=f17.get(),font=("times",15)).grid(row=9, column=2)
            if opt!=0:
                tk.Label(fg, text=f8.get(),font=("times",15)).grid(row=10, column=2)
 
            #total marks in ut
            tk.Label(fg, text="Total Marks in UT-1",font=("times",15),relief="sunken",bg=head).grid(row=4, column=3)
            tk.Label(fg, text=f18.get(),font=("times",15)).grid(row=5, column=3)
            tk.Label(fg, text=f19.get(),font=("times",15)).grid(row=6, column=3)
            tk.Label(fg, text=f20.get(),font=("times",15)).grid(row=7, column=3)
            tk.Label(fg, text=f21.get(),font=("times",15)).grid(row=8, column=3)
            tk.Label(fg, text=f22.get(),font=("times",15)).grid(row=9, column=3)
            if opt!=0:
                tk.Label(fg, text=f9.get(),font=("times",15)).grid(row=10, column=3)

            #marks in half yearly
            tk.Label(fg, text="Marks Scored in HY",font=("times",15),relief="sunken",bg=head).grid(row=4, column=4)
            tk.Label(fg, text=f23.get(),font=("times",15)).grid(row=5, column=4)
            tk.Label(fg, text=f24.get(),font=("times",15)).grid(row=6, column=4)
            tk.Label(fg, text=f25.get(),font=("times",15)).grid(row=7, column=4)
            tk.Label(fg, text=f26.get(),font=("times",15)).grid(row=8, column=4)
            tk.Label(fg, text=f27.get(),font=("times",15)).grid(row=9, column=4)
            if opt!=0:
                tk.Label(fg, text=f10.get(),font=("times",15)).grid(row=10, column=4)

            #totsl marks in half yearly
            tk.Label(fg, text="Total Marks in HY",font=("times",15),relief="sunken",bg=head).grid(row=4, column=5)
            tk.Label(fg, text=f28.get(),font=("times",15)).grid(row=5, column=5)
            tk.Label(fg, text=f29.get(),font=("times",15)).grid(row=6, column=5)
            tk.Label(fg, text=f30.get(),font=("times",15)).grid(row=7, column=5)
            tk.Label(fg, text=f31.get(),font=("times",15)).grid(row=8, column=5)
            tk.Label(fg, text=f32.get(),font=("times",15)).grid(row=9, column=5)
            if opt!=0:
                tk.Label(fg, text=f11.get(),font=("times",15)).grid(row=10, column=5)

            #grades
            tk.Label(fg, text="Grade",font=("times",15),relief="sunken",bg=head).grid(row=4, column=6)

            #status
            tk.Label(fg, text="Status",font=("times",15),relief="sunken",bg=head).grid(row=4, column=7)

            #labels for total and percentage
            tk.Label(fg, text="Total ").grid(row=11, column=1)
            tk.Label(fg , text="Total Marks in UT AND HY").grid(row=13, column=2)
            tk.Label(fg , text="Marks Scored in UT AND HY").grid(row=14, column=2)
            tk.Label(fg , text="percentage").grid(row=15, column=2)
            if opt!=0:
                tot1=int(f18.get())+int(f19.get())+int(f20.get())+int(f21.get())+int(f22.get())+int(f9.get())
                tot2=int(f28.get())+int(f29.get())+int(f30.get())+int(f31.get())+int(f32.get())+int(f11.get())
                tot3=int(f23.get())+int(f24.get())+int(f25.get())+int(f26.get())+int(f27.get())+int(f10.get())
                tot4=int(f13.get())+int(f14.get())+int(f15.get())+int(f16.get())+int(f17.get())+int(f8.get())
            else:
                tot1=int(f18.get())+int(f19.get())+int(f20.get())+int(f21.get())+int(f22.get())
                tot2=int(f28.get())+int(f29.get())+int(f30.get())+int(f31.get())+int(f32.get())
                tot3=int(f23.get())+int(f24.get())+int(f25.get())+int(f26.get())+int(f27.get())
                tot4=int(f13.get())+int(f14.get())+int(f15.get())+int(f16.get())+int(f17.get())
            tmarks=(30/100)*tot1+(70/100)*tot2
            tmarks1=tot1+tot2
            omarks=(30/100)*tot4+(70/100)*tot3
            omarks1=tot4+tot3

            tk.Label(fg, text=tot1).grid(row=11, column=3)
            tk.Label(fg, text=tot4).grid(row=11, column=2)
            tk.Label(fg, text=tot2).grid(row=11, column=5)
            tk.Label(fg, text=tot3).grid(row=11, column=4)
            tk.Label(fg, text=tmarks1).grid(row=13, column=3)
            tk.Label(fg, text=omarks1).grid(row=14, column=3)
            l=(omarks/tmarks)*100
            
            tk.Label(fg, text=l).grid(row=15, column=3)

            a=(0.3*int(f13.get()))+(0.7*int(f23.get()))
            b=(0.3*int(f18.get()))+(0.7*int(f28.get()))
            if a>=0.9*b:
                tk.Label(fg, text ="A").grid(row=5, column=6)
                tk.Label(fg, text ="PASS").grid(row=5, column=7)
            elif a >= 0.7 *b:
                tk.Label(fg, text ="B").grid(row=5, column=6)
                tk.Label(fg, text ="PASS").grid(row=5, column=7)
            elif a >= 0.5* b:
                tk.Label(fg, text ="C").grid(row=5, column=6)
                tk.Label(fg, text ="PASS").grid(row=5, column=7)
            elif a >= 0.4*b:
                tk.Label(fg, text ="D").grid(row=5, column=6)
                tk.Label(fg, text ="PASS").grid(row=5, column=7)
            elif a >= 0.33*b:
                tk.Label(fg, text ="E").grid(row=5, column=6)
                tk.Label(fg, text ="PASS").grid(row=5, column=7)
            else:
                tk.Label(fg, text ="F").grid(row=5, column=6)
                tk.Label(fg, text ="FAIL").grid(row=5, column=7)

            c=(0.3*int(f14.get()))+(0.7*int(f24.get()))
            d=(0.3*int(f19.get()))+(0.7*int(f29.get()))
            if c>=0.9*d:
                tk.Label(fg, text ="A").grid(row=6, column=6)
                tk.Label(fg, text ="PASS").grid(row=6, column=7)
            elif c >= 0.7 *d:
                tk.Label(fg, text ="B").grid(row=6, column=6)
                tk.Label(fg, text ="PASS").grid(row=6, column=7)
            elif c >= 0.5* d:
                tk.Label(fg, text ="C").grid(row=6, column=6)
                tk.Label(fg, text ="PASS").grid(row=6, column=7)
            elif c >= 0.4*d:
                tk.Label(fg, text ="D").grid(row=6, column=6)
                tk.Label(fg, text ="PASS").grid(row=6, column=7)
            elif c >= 0.33*d:
                tk.Label(fg, text ="E").grid(row=6, column=6)
                tk.Label(fg, text ="PASS").grid(row=6, column=7)
            else:
                tk.Label(fg, text ="F").grid(row=6, column=6)
                tk.Label(fg, text ="FAIL").grid(row=6, column=7)

            e=(0.3*int(f15.get()))+(0.7*int(f25.get()))
            f=(0.3*int(f20.get()))+(0.7*int(f30.get()))
            if e>=0.9*f:
                tk.Label(fg, text ="A").grid(row=7, column=6)
                tk.Label(fg, text ="PASS").grid(row=7, column=7)
            elif e >= 0.7 *f:
                tk.Label(fg, text ="B").grid(row=7, column=6)
                tk.Label(fg, text ="PASS").grid(row=7, column=7)
            elif e >= 0.5*f:
                tk.Label(fg, text ="C").grid(row=7, column=6)
                tk.Label(fg, text ="PASS").grid(row=7, column=7)
            elif e >= 0.4*f:
                tk.Label(fg, text ="D").grid(row=7, column=6)
                tk.Label(fg, text ="PASS").grid(row=7, column=7)
            elif e >= 0.33*f:
                tk.Label(fg, text ="E").grid(row=7, column=6)
                tk.Label(fg, text ="PASS").grid(row=7, column=7)
            else:
                tk.Label(fg, text ="F").grid(row=7, column=6)
                tk.Label(fg, text ="FAIL").grid(row=7, column=7)

            g=(0.3*int(f16.get()))+(0.7*int(f26.get()))
            h=(0.3*int(f21.get()))+(0.7*int(f31.get()))
            if g>=0.9*h:
                tk.Label(fg, text ="A").grid(row=8, column=6)
                tk.Label(fg, text ="PASS").grid(row=8, column=7)
            elif g >= 0.7 *h:
                tk.Label(fg, text ="B").grid(row=8, column=6)
                tk.Label(fg, text ="PASS").grid(row=8, column=7)
            elif g >= 0.5*h:
                tk.Label(fg, text ="C").grid(row=8, column=6)
                tk.Label(fg, text ="PASS").grid(row=8, column=7)
            elif g >= 0.4*h:
                tk.Label(fg, text ="D").grid(row=8, column=6)
                tk.Label(fg, text ="PASS").grid(row=8, column=7)
            elif g >= 0.33*h:
                tk.Label(fg, text ="E").grid(row=8, column=6)
                tk.Label(fg, text ="PASS").grid(row=8, column=7)
            else:
                tk.Label(fg, text ="F").grid(row=8, column=6)
                tk.Label(fg, text ="FAIL").grid(row=8, column=7)

            i=(0.3*int(f17.get()))+(0.7*int(f27.get()))
            j=(0.3*int(f22.get()))+(0.7*int(f32.get()))
            if i>=0.9*j:
                tk.Label(fg, text ="A").grid(row=9, column=6)
                tk.Label(fg, text ="PASS").grid(row=9, column=7)
            elif i >= 0.7 *j:
                tk.Label(fg, text ="B").grid(row=9, column=6)
                tk.Label(fg, text ="PASS").grid(row=9, column=7)
            elif i >= 0.5*j:
                tk.Label(fg, text ="C").grid(row=9, column=6)
                tk.Label(fg, text ="PASS").grid(row=9, column=7)
            elif i >= 0.4*j:
                tk.Label(fg, text ="D").grid(row=9, column=6)
                tk.Label(fg, text ="PASS").grid(row=9, column=7)
            elif i >= 0.33*j:
                tk.Label(fg, text ="E").grid(row=9, column=6)
                tk.Label(fg, text ="PASS").grid(row=9, column=7)
            else:
                tk.Label(fg, text ="F").grid(row=9, column=6)
                tk.Label(fg, text ="FAIL").grid(row=9, column=7)

            if opt!=0:
                ik=(0.3*int(f8.get()))+(0.7*int(f10.get()))
                jk=(0.3*int(f9.get()))+(0.7*int(f11.get()))
                if ik>=0.9*jk:
                    tk.Label(fg, text ="A").grid(row=9, column=6)
                    tk.Label(fg, text ="PASS").grid(row=9, column=7)
                elif ik >= 0.7 *jk:
                    tk.Label(fg, text ="B").grid(row=9, column=6)
                    tk.Label(fg, text ="PASS").grid(row=9, column=7)
                elif ik >= 0.5*jk:
                    tk.Label(fg, text ="C").grid(row=9, column=6)
                    tk.Label(fg, text ="PASS").grid(row=9, column=7)
                elif ik >= 0.4*jk:
                    tk.Label(fg, text ="D").grid(row=9, column=6)
                    tk.Label(fg, text ="PASS").grid(row=9, column=7)
                elif ik >= 0.33*jk:
                    tk.Label(fg, text ="E").grid(row=9, column=6)
                    tk.Label(fg, text ="PASS").grid(row=9, column=7)
                else:
                    tk.Label(fg, text ="F").grid(row=9, column=6)
                    tk.Label(fg, text ="FAIL").grid(row=9, column=7)
    
            

            #teachers remarks
            tk.Label(fg, text="Teacher's Remarks",font=("times",15),bg=head).grid(row=16, column=0)
            tk.Label(fg, text=f33.get(),font=("times",15)).grid(row=18, column=0)

            #teachers name
            tk.Label(fg, text="Teacher's Name",font=("times",15),bg=head).grid(row=16, column=3)
            tk.Label(fg, text=f34.get(),font=("times",15)).grid(row=18, column=3)

            #date
            tk.Label(fg, text="Date",font=("times",15),bg=head).grid(row=16, column=5)
            tk.Label(fg, text=f35.get(),font=("times",15)).grid(row=18, column=5)

            #button to go back
            n2=tk.Button(fg, text="Back",font=("times",15), bg="blue",fg="white", command=fg.destroy) 
            n2.grid(row=20, column=3)

        # button to display completed report card 
        bn1=tk.Button(ok, text="Generate", bg="green", command=heh) 
        bn1.grid(row=22, column=0)
        
        # button to reset
        bn2=tk.Button(ok, text="Reset", bg="red", command=reset) 
        bn2.grid(row=22, column=3)

        # button to go back to main menu
        bn2=tk.Button(ok, text="Back", bg="blue",fg="white", command=ok.destroy) 
        bn2.grid(row=22, column=5)
        ok.mainloop() 


import tkinter as tk
def finals():
    
    def des():
        m.destroy()
        fs()

    m=tk.Tk()
    m.geometry("800x200")
    f5=open("disclaimer.txt","r")
    disclaim=f5.read()
    f5.close()
    msg=tk.Message(m,text=disclaim)
    msg.configure(font=("Poor Richard",21),aspect=1000,relief="sunken")
    msg.pack(fill=tk.X)
    btn=tk.Button(m,text="Dismiss",command=des)
    btn.pack()
    def fs():
        global cnt
        cnt=0
        root=tk.Tk()
        root.title("Finals")
        root.geometry("1700x700")
        g1=tk.Entry(root)
        g2=tk.Entry(root)
        g3=tk.Entry(root)
        g4=tk.Entry(root)
        g5=tk.Entry(root)
        g6=tk.Entry(root)
        g7=tk.Entry(root)
        g8=tk.Entry(root)
        g9=tk.Entry(root)
        g10=tk.Entry(root)
        g11=tk.Entry(root)
        g12=tk.Entry(root)
        g13=tk.Entry(root)
        g14=tk.Entry(root)
        g15=tk.Entry(root)
        g16=tk.Entry(root)
        g17=tk.Entry(root)
        g18=tk.Entry(root)
        g19=tk.Entry(root)
        g20=tk.Entry(root)
        g21=tk.Entry(root)
        g22=tk.Entry(root)
        g23=tk.Entry(root)
        g24=tk.Entry(root)
        g25=tk.Entry(root)
        g26=tk.Entry(root)
        g27=tk.Entry(root)
        g28=tk.Entry(root)
        g29=tk.Entry(root)
        g30=tk.Entry(root)
        g31=tk.Entry(root)
        g32=tk.Entry(root)
        g33=tk.Entry(root)
        g34=tk.Entry(root)
        g35=tk.Entry(root)
        g36=tk.Entry(root)
        g37=tk.Entry(root)
        g38=tk.Entry(root)
        g39=tk.Entry(root)
        g40=tk.Entry(root)
        g41=tk.Entry(root)
        g42=tk.Entry(root)
        g43=tk.Entry(root)
        g44=tk.Entry(root)
        g45=tk.Entry(root)
        g46=tk.Entry(root)
        g47=tk.Entry(root)
        g48=tk.Entry(root)
        g49=tk.Entry(root)
        g50=tk.Entry(root)
        g51=tk.Entry(root)
        g52=tk.Entry(root)
        g53=tk.Entry(root)
        g54=tk.Entry(root)
        g55=tk.Entry(root)
        g56=tk.Entry(root)
        g57=tk.Entry(root)
        g58=tk.Entry(root)
        g59=tk.Entry(root)
        g60=tk.Entry(root)
        g61=tk.Entry(root)
        g62=tk.Entry(root)
        g63=tk.Entry(root)

        #entry for name of organisation
        tk.Label(root,text="Name of organisation").grid(row=0,column=0)
        g1.grid(row=0,column=1)

        #entry of name
        tk.Label(root,text="Name of Student").grid(row=1,column=0)
        g2.grid(row=1,column=1)

        #entry of adm no
        tk.Label(root,text="Admission Number").grid(row=1,column=2)
        g3.grid(row=1,column=3)

        #entry of class
        tk.Label(root,text="Class").grid(row=1,column=4)
        OPTIONS = [1,2,3,4,5,6,7,8,9,10,"11-PCM","11-PCB","11-COMMERCE","11-ARTS","12-PCM","12-PCB","12-COMMERCE","12-ARTS"]
        variable2 = tk.StringVar(root)
        variable2.set("select class")
        w = tk.OptionMenu(root, variable2, *OPTIONS)
        w.grid(row=1,column=5)
        
        # entry of subject names
        tk.Label(root, text="Subject").grid(row=4, column=1)  
        g11.grid(row=10, column=1)
        
        def confirm():
            global cnt
            cnt=cnt+1
            global clsss
            
            clsss=(variable2.get())
            global aa1,aa2,aa3,aa4,aa5
            if cnt>1:
                    aa1.destroy()
                    aa2.destroy()
                    aa3.destroy()
                    aa4.destroy()
                    try:
                        aa5.destroy()
                    except:
                        pass
            
            try:
                
                
                if int(clsss)>=1 and int(clsss)<=5:
                    
                    aa1=tk.Label(root, text="English")
                    aa2=tk.Label(root, text="Maths")
                    aa3=tk.Label(root, text="EVS")
                    aa4=tk.Label(root, text="Computers")
                    aa5=tk.Label(root, text="\t    Hindi   \t")
                elif int(clsss)>=6 and int(clsss)<=10:
                    aa1=tk.Label(root, text="English")
                    aa2=tk.Label(root, text="Maths")
                    aa3=tk.Label(root, text="Science")
                    aa4=tk.Label(root, text="Social Science")
                    aa5=tk.Label(root, text="\t    Hindi   \t")
                aa1.grid(row=5, column=1)
                aa2.grid(row=6, column=1)
                aa3.grid(row=7, column=1)
                aa4.grid(row=8, column=1)
                aa5.grid(row=9, column=1)
            except:
                
                if clsss=="11-PCM" or clsss=="12-PCM":
                    aa1=tk.Label(root, text="English")
                    aa2=tk.Label(root, text="Maths")
                    aa3=tk.Label(root, text="Chemistry")
                    aa4=tk.Label(root, text="Physics")
                    
                elif clsss=="11-PCB" or clsss=="12-PCB":
                    aa1=tk.Label(root, text="English")
                    aa2=tk.Label(root, text="Biology")
                    aa3=tk.Label(root, text="Chemistry")
                    aa4=tk.Label(root, text="Physics")
                    
                elif clsss=="11-COMMERCE" or clsss=="12-COMMERCE":
                    aa1=tk.Label(root, text="English")
                    aa2=tk.Label(root, text="Accountancy")
                    aa3=tk.Label(root, text="Business Studies")
                    aa4=tk.Label(root, text="Economics")

                elif clsss=="11-ARTS" or clsss=="12-ARTS":
                    aa1=tk.Label(root, text="English")
                    aa2=tk.Label(root, text="History")
                    aa3=tk.Label(root, text="Political Science")
                    aa4=tk.Label(root, text="Geography")
                aa1.grid(row=5, column=1)
                aa2.grid(row=6, column=1)
                aa3.grid(row=7, column=1)
                aa4.grid(row=8, column=1)
                g7.grid(row=9, column=1)
                
        
        BTN=tk.Button(root,text="Confirm Class",command=confirm)
        BTN.grid(row=1,column=6)


        #entry of sec
        tk.Label(root,text="Section").grid(row=2,column=0)
        g4.grid(row=2,column=1)

        #entry of roll no.
        tk.Label(root,text="Roll Number").grid(row=2,column=3)
        def sel1():
            sel2 = "Roll Number = " + str(scale.get())
            label.config(text = sel2)
        var1 = tk.DoubleVar()
        scale = tk.Scale(root,from_=1,to=100,variable=var1 )
        scale.grid(row=2,column=4)
        button = tk.Button(root, text="Get Scale Value", command=sel1)
        button.grid(row=2,column=6)
        label = tk.Label(root)
        label.grid(row=2,column=5)
        #entry of FATHERS NAME
        tk.Label(root, text="Father's Name").grid(row=3, column=0)
        g5.grid(row=3,column=1)
        #entry of mothers name
        tk.Label(root, text="Mother's Name").grid(row=3, column=3)
        g6.grid(row=3,column=4)

        # entry of serial numbers
        tk.Label(root, text="Srl.No").grid(row=4, column=0)
        tk.Label(root, text="1").grid(row=5, column=0)
        tk.Label(root, text="2").grid(row=6, column=0)
        tk.Label(root, text="3").grid(row=7, column=0)
        tk.Label(root, text="4").grid(row=8, column=0)
        tk.Label(root, text="5").grid(row=9, column=0)
        tk.Label(root, text="6").grid(row=10, column=0)


        #labels and entries for Ut
        tk.Label(root, text="Marks Scored in UT-1").grid(row=4, column=2)
        g13.grid(row=5,column=2)
        g14.grid(row=6,column=2)
        g15.grid(row=7,column=2)
        g16.grid(row=8,column=2)
        g17.grid(row=9,column=2)
        g56.grid(row=10,column=2)


        tk.Label(root, text="Total Marks in UT-1").grid(row=4, column=3)
        g18.grid(row=5,column=3)
        g19.grid(row=6,column=3)
        g20.grid(row=7,column=3)
        g21.grid(row=8,column=3)
        g22.grid(row=9,column=3)
        g57.grid(row=10,column=3)


        #labels and entries for Half Yearly
        tk.Label(root, text="Marks Scored in HY").grid(row=4, column=4)
        g23.grid(row=5,column=4)
        g24.grid(row=6,column=4)
        g25.grid(row=7,column=4)
        g26.grid(row=8,column=4)
        g27.grid(row=9,column=4)
        g58.grid(row=10,column=4)

        tk.Label(root, text="Total Marks in HY").grid(row=4, column=5)
        g28.grid(row=5,column=5)
        g29.grid(row=6,column=5)
        g30.grid(row=7,column=5)
        g31.grid(row=8,column=5)
        g32.grid(row=9,column=5)
        g59.grid(row=10,column=5)

        #labels and entries for Ut-2
        tk.Label(root, text="Marks Scored in UT-2").grid(row=4, column=6)
        g33.grid(row=5,column=6)
        g34.grid(row=6,column=6)
        g35.grid(row=7,column=6)
        g36.grid(row=8,column=6)
        g37.grid(row=9,column=6)
        g60.grid(row=10,column=6)

        tk.Label(root, text="Total Marks in UT-2").grid(row=4, column=7)
        g38.grid(row=5,column=7)
        g39.grid(row=6,column=7)
        g40.grid(row=7,column=7)
        g41.grid(row=8,column=7)
        g42.grid(row=9,column=7)
        g61.grid(row=10,column=7)

        #labels and entries for Finals

        tk.Label(root, text="Marks Scored in Finals").grid(row=4, column=8)
        g43.grid(row=5,column=8)
        g44.grid(row=6,column=8)
        g45.grid(row=7,column=8)
        g46.grid(row=8,column=8)
        g47.grid(row=9,column=8)
        g62.grid(row=10,column=8)

        tk.Label(root, text="Total Marks in Finals").grid(row=4, column=9)
        g48.grid(row=5,column=9)
        g49.grid(row=6,column=9)
        g50.grid(row=7,column=9)
        g51.grid(row=8,column=9)
        g52.grid(row=9,column=9)
        g63.grid(row=10,column=9)

        # entry of teachers remarks
        tk.Label(root, text="Teacher's Remarks").grid(row=11, column=0)
        g53.grid(row=11,column=1)

        # entry of teachers name
        tk.Label(root, text="Teacher's Name").grid(row=12, column=0)
        g54.grid(row=12,column=1)

        # entry of date
        tk.Label(root, text="Date").grid(row=13, column=0)
        g55.grid(row=13,column=1)

        #\colours
        
        #header
        hea=tk.Label(root,text="choose header colour:").grid(row=14,column=0)
        global ii
        global jj
        global kk
        iii=tk.IntVar(root)
        ri1=tk.Radiobutton(root,text="white",value=1,variable=iii).grid(row=15,column=0)
        ri2=tk.Radiobutton(root,text="purple",value=2,variable=iii).grid(row=15,column=2)
        ri3=tk.Radiobutton(root,text="blue",value=3,variable=iii).grid(row=15,column=4)
        ri4=tk.Radiobutton(root,text="green",value=4,variable=iii).grid(row=15,column=6)
        ri5=tk.Radiobutton(root,text="orange",value=5,variable=iii).grid(row=15,column=8)
        ri6=tk.Radiobutton(root,text="yellow",value=6,variable=iii).grid(row=15,column=10)

        #background
        bac=tk.Label(root,text="choose background colour:").grid(row=16,column=0)
        jjj=tk.IntVar(root)
        ri11=tk.Radiobutton(root,text="white",value=1,variable=jjj).grid(row=17,column=0)
        ri22=tk.Radiobutton(root,text="purple",value=2,variable=jjj).grid(row=17,column=2)
        ri33=tk.Radiobutton(root,text="blue",value=3,variable=jjj).grid(row=17,column=4)
        ri44=tk.Radiobutton(root,text="green",value=4,variable=jjj).grid(row=17,column=6)
        ri55=tk.Radiobutton(root,text="orange",value=5,variable=jjj).grid(row=17,column=8)
        ri66=tk.Radiobutton(root,text="yellow",value=6,variable=jjj).grid(row=17,column=10)

        #foreground
        fo=tk.Label(root,text="choose details colour:").grid(row=18,column=0)
        kkk=tk.IntVar(root)
        rii11=tk.Radiobutton(root,text="white",value=2,variable=kkk).grid(row=19,column=0)
        rii22=tk.Radiobutton(root,text="grey",value=3,variable=kkk).grid(row=19,column=2)

        def reset():
            g1.delete(0,tk.END)
            g2.delete(0,tk.END)
            g3.delete(0,tk.END)
            g4.delete(0,tk.END)
            g5.delete(0,tk.END)
            g6.delete(0,tk.END)
            g7.delete(0,tk.END)
            g8.delete(0,tk.END)
            g9.delete(0,tk.END)
            g10.delete(0,tk.END)
            g11.delete(0,tk.END)
            g12.delete(0,tk.END)
            g13.delete(0,tk.END)
            g14.delete(0,tk.END)
            g15.delete(0,tk.END)
            g16.delete(0,tk.END)
            g17.delete(0,tk.END)
            g18.delete(0,tk.END)
            g19.delete(0,tk.END)
            g20.delete(0,tk.END)
            g21.delete(0,tk.END)
            g22.delete(0,tk.END)
            g23.delete(0,tk.END)
            g24.delete(0,tk.END)
            g25.delete(0,tk.END)
            g26.delete(0,tk.END)
            g27.delete(0,tk.END)
            g28.delete(0,tk.END)
            g29.delete(0,tk.END)
            g30.delete(0,tk.END)
            g31.delete(0,tk.END)
            g32.delete(0,tk.END)
            g33.delete(0,tk.END)
            g34.delete(0,tk.END)
            g35.delete(0,tk.END)
            g36.delete(0,tk.END)
            g37.delete(0,tk.END)
            g38.delete(0,tk.END)
            g39.delete(0,tk.END)
            g40.delete(0,tk.END)
            g41.delete(0,tk.END)
            g42.delete(0,tk.END)
            g43.delete(0,tk.END)
            g44.delete(0,tk.END)
            g45.delete(0,tk.END)
            g46.delete(0,tk.END)
            g47.delete(0,tk.END)
            g48.delete(0,tk.END)
            g49.delete(0,tk.END)
            g50.delete(0,tk.END)
            g51.delete(0,tk.END)
            g52.delete(0,tk.END)
            g53.delete(0,tk.END)
            g54.delete(0,tk.END)
            g55.delete(0,tk.END)
            g56.delete(0,tk.END)
            g57.delete(0,tk.END)
            g58.delete(0,tk.END)
            g59.delete(0,tk.END)
            g60.delete(0,tk.END)
            g61.delete(0,tk.END)
            g62.delete(0,tk.END)
            g63.delete(0,tk.END)
            aa1.destroy()
            aa2.destroy()
            aa3.destroy()
            aa4.destroy()
            try:
                aa5.destroy()
            except:
                pass

        def heh():
            opt=1
            clsss=variable2.get()
            if g11.get()=="":
                opt=0
            if iii.get()==1:
                head="white"
            elif iii.get()==2:
                head="mediumpurple"
            elif iii.get()==3:
                head="cornflowerblue"
            elif iii.get()==4:
                head="limegreen"
            elif iii.get()==5:
                head="darkorange"
            else:
                head="goldenrod"
            if jjj.get()==1:
                back="white"
            elif jjj.get()==2:
                back="thistle"
            elif jjj.get()==3:
                back="powderblue"
            elif jjj.get()==4:
                back="limegreen"
            elif jjj.get()==5:
                back="sandybrown"
            else:
                back="khaki"
            if kkk.get()==2:
                fore="white"
            else:
                fore="grey"

            leo=tk.Tk()
            leo.title("Report Card")
            leo.geometry("1420x800")
            leo.config(bg=back)

        
            #putting in org name, test name and student details
            if clsss in ["11-PCM","11-PCB","11-COMMERCE","11-ARTS"]:
                itsi="11"
            elif clsss in ["12-PCM","12-PCB","12-COMMERCE","12-ARTS"]:
                itsi="12"
            else:
                itsi=str(clsss)
            mhmkm=tk.Frame(leo,width=170,height=85,bg="white")
            mhmkm.grid(row=0,column=3,columnspan=5)
            l=" "+g1.get()+" "+"\n"+" FINALS "
            m1=tk.Message(mhmkm,text=l)
            m1.configure(font=("times",22,"bold"),bg=head,justify="center",aspect=1000,relief="groove")
            m1.place(x=0,y=0)
            lool=tk.Frame(leo,width=1000,height=200,bg=fore)
            lool.grid(row=2,columnspan=11)
            hf="Name:"+g2.get()+"\n"+"Class-Sec:"+itsi+" "+g4.get()+"\n"+"Father's Name:"+g5.get()
            kf="Admission No.:"+g3.get()+"\n"+"Roll No.:"+str(scale.get())+"\n"+"Mother's Name:"+g6.get()
            mg=tk.Message(lool,text=hf)
            mg.configure(font=("times",23),bg=fore,aspect=1000,relief="raised")
            mg.place(x=0,y=20)
            mh=tk.Message(lool,text=kf)
            mh.configure(font=("times",23),bg=fore,aspect=1000,relief="raised")
            mh.place(x=500,y=20)

            #serial num
            tk.Label(leo, text="Srl.No",font=("times",10),justify="left",relief="sunken",bg=head).grid(row=4, column=0)
            tk.Label(leo, text="1",font=("times",10)).grid(row=5, column=0)
            tk.Label(leo, text="2",font=("times",10)).grid(row=6, column=0)
            tk.Label(leo, text="3",font=("times",10)).grid(row=7, column=0)
            tk.Label(leo, text="4",font=("times",10)).grid(row=8, column=0)
            tk.Label(leo, text="5",font=("times",10)).grid(row=9, column=0)
            if opt!=0:
                tk.Label(leo, text="6",font=("times",10)).grid(row=10, column=0)

            #subj
            tk.Label(leo, text="Subject",font=("times",10),relief="sunken",bg=head).grid(row=4, column=1)
            try:
                if int(clsss)>=1 and int(clsss)<=5:
                    tk.Label(leo, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(leo, text="Maths",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(leo, text="EVS",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(leo, text="Computers",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(leo, text="Hindi",font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif int(clsss)>=6 and int(clsss)<=10:
                    tk.Label(leo, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(leo, text="Maths",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(leo, text="Science",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(leo, text="Social Science",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(leo, text="Hindi",font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
            except:
                if clsss=="11-PCM" or clsss=="12-PCM":
                    tk.Label(leo, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(leo, text="Maths",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(leo, text="Chemistry",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(leo, text="Physics",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(leo, text=g7.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif clsss=="11-PCB" or clsss=="12-PCB":
                    tk.Label(leo, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(leo, text="Biology",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(leo, text="Chemistry",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(leo, text="Physics",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(leo, text=g7.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif clsss=="11-COMMERCE" or clsss=="12-COMMERCE":
                    tk.Label(leo, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(leo, text="Accountancy",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(leo, text="Business Studies",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(leo, text="Economics",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(leo, text=g7.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
                elif clsss=="11-ARTS" or clsss=="12-ARTS" :
                    tk.Label(leo, text="English",font=("times",15),relief="sunken",bg=head).grid(row=5, column=1)
                    tk.Label(leo, text="History",font=("times",15),relief="sunken",bg=head).grid(row=6, column=1)
                    tk.Label(leo, text="Political Science",font=("times",15),relief="sunken",bg=head).grid(row=7, column=1)
                    tk.Label(leo, text="Geography",font=("times",15),relief="sunken",bg=head).grid(row=8, column=1)
                    tk.Label(leo, text=g7.get(),font=("times",15),relief="sunken",bg=head).grid(row=9, column=1)
            if opt!=0:
                tk.Label(leo, text=g11.get(),font=("times",15),relief="sunken",bg=head).grid(row=10, column=1)


            #marks scored in ut
            tk.Label(leo, text="Marks Scored in UT-1",font=("times",10),relief="sunken",bg=head).grid(row=4, column=2)
            tk.Label(leo, text=g13.get(),font=("times",10)).grid(row=5, column=2)
            tk.Label(leo, text=g14.get(),font=("times",10)).grid(row=6, column=2)
            tk.Label(leo, text=g15.get(),font=("times",10)).grid(row=7, column=2)
            tk.Label(leo, text=g16.get(),font=("times",10)).grid(row=8, column=2)
            tk.Label(leo, text=g17.get(),font=("times",10)).grid(row=9, column=2)
            if opt!=0:
                tk.Label(leo, text=g56.get(),font=("times",10)).grid(row=10, column=2)
 
            #total marks in ut
            tk.Label(leo, text="Total Marks in UT-1",font=("times",10),relief="sunken",bg=head).grid(row=4, column=3)
            tk.Label(leo, text=g18.get(),font=("times",10)).grid(row=5, column=3)
            tk.Label(leo, text=g19.get(),font=("times",10)).grid(row=6, column=3)
            tk.Label(leo, text=g20.get(),font=("times",10)).grid(row=7, column=3)
            tk.Label(leo, text=g21.get(),font=("times",10)).grid(row=8, column=3)
            tk.Label(leo, text=g22.get(),font=("times",10)).grid(row=9, column=3)
            if opt!=0:
                tk.Label(leo, text=g57.get(),font=("times",10)).grid(row=10, column=3)

            #marks in half yearly
            tk.Label(leo, text="Marks Scored in HY",font=("times",10),relief="sunken",bg=head).grid(row=4, column=4)
            tk.Label(leo, text=g23.get(),font=("times",10)).grid(row=5, column=4)
            tk.Label(leo, text=g24.get(),font=("times",10)).grid(row=6, column=4)
            tk.Label(leo, text=g25.get(),font=("times",10)).grid(row=7, column=4)
            tk.Label(leo, text=g26.get(),font=("times",10)).grid(row=8, column=4)
            tk.Label(leo, text=g27.get(),font=("times",10)).grid(row=9, column=4)
            if opt!=0:
                tk.Label(leo, text=g58.get(),font=("times",10)).grid(row=10, column=4)

            #totsl marks in half yearly
            tk.Label(leo, text="Total Marks in HY",font=("times",10),relief="sunken",bg=head).grid(row=4, column=5)
            tk.Label(leo, text=g28.get(),font=("times",10)).grid(row=5, column=5)
            tk.Label(leo, text=g29.get(),font=("times",10)).grid(row=6, column=5)
            tk.Label(leo, text=g30.get(),font=("times",10)).grid(row=7, column=5)
            tk.Label(leo, text=g31.get(),font=("times",10)).grid(row=8, column=5)
            tk.Label(leo, text=g32.get(),font=("times",10)).grid(row=9, column=5)
            if opt!=0:
                tk.Label(leo, text=g59.get(),font=("times",10)).grid(row=10, column=5)

            #marks in ut2
            tk.Label(leo, text="Marks Scored in UT-2",font=("times",10),relief="sunken",bg=head).grid(row=4, column=6)
            tk.Label(leo, text=g33.get(),font=("times",10)).grid(row=5, column=6)
            tk.Label(leo, text=g34.get(),font=("times",10)).grid(row=6, column=6)
            tk.Label(leo, text=g35.get(),font=("times",10)).grid(row=7, column=6)
            tk.Label(leo, text=g36.get(),font=("times",10)).grid(row=8, column=6)
            tk.Label(leo, text=g37.get(),font=("times",10)).grid(row=9, column=6)
            if opt!=0:
                tk.Label(leo, text=g60.get(),font=("times",10)).grid(row=10, column=6)

            #totsl marks in ut2
            tk.Label(leo, text="Total Marks in UT-2",font=("times",10),relief="sunken",bg=head).grid(row=4, column=7)
            tk.Label(leo, text=g38.get(),font=("times",10)).grid(row=5, column=7)
            tk.Label(leo, text=g39.get(),font=("times",10)).grid(row=6, column=7)
            tk.Label(leo, text=g40.get(),font=("times",10)).grid(row=7, column=7)
            tk.Label(leo, text=g41.get(),font=("times",10)).grid(row=8, column=7)
            tk.Label(leo, text=g42.get(),font=("times",10)).grid(row=9, column=7)
            if opt!=0:
                tk.Label(leo, text=g61.get(),font=("times",10)).grid(row=10, column=7)

            #marks in FINALS
            tk.Label(leo, text="Marks Scored in UT-2",font=("times",10),relief="sunken",bg=head).grid(row=4, column=8)
            tk.Label(leo, text=g43.get(),font=("times",10)).grid(row=5, column=8)
            tk.Label(leo, text=g44.get(),font=("times",10)).grid(row=6, column=8)
            tk.Label(leo, text=g45.get(),font=("times",10)).grid(row=7, column=8)
            tk.Label(leo, text=g46.get(),font=("times",10)).grid(row=8, column=8)
            tk.Label(leo, text=g47.get(),font=("times",10)).grid(row=9, column=8)
            if opt!=0:
                tk.Label(leo, text=g62.get(),font=("times",10)).grid(row=10, column=8)

            #totsl marks in finals
            tk.Label(leo, text="Total Marks in UT-2",font=("times",10),relief="sunken",bg=head).grid(row=4, column=9)
            tk.Label(leo, text=g48.get(),font=("times",10)).grid(row=5, column=9)
            tk.Label(leo, text=g49.get(),font=("times",10)).grid(row=6, column=9)
            tk.Label(leo, text=g50.get(),font=("times",10)).grid(row=7, column=9)
            tk.Label(leo, text=g51.get(),font=("times",10)).grid(row=8, column=9)
            tk.Label(leo, text=g52.get(),font=("times",10)).grid(row=9, column=9)
            if opt!=0:
                tk.Label(leo, text=g63.get(),font=("times",10)).grid(row=10, column=9)

            #grades
            tk.Label(leo, text="Grade",font=("times",10),relief="sunken",bg=head).grid(row=4, column=10)

            #status
            tk.Label(leo, text="Status",font=("times",10),relief="sunken",bg=head).grid(row=4, column=11)

            #labels for total and percentage
            tk.Label(leo, text="Total ").grid(row=11, column=1)
            tk.Label(leo , text="Total Marks in All Exams").grid(row=13, column=1)
            tk.Label(leo , text="Marks Scored in All Exams").grid(row=14, column=1)
            tk.Label(leo , text="Percentage").grid(row=15, column=1)
            if opt!=0:
                tot1=int(g18.get())+int(g19.get())+int(g20.get())+int(g21.get())+int(g22.get())+int(g57.get())
                tot2=int(g28.get())+int(g29.get())+int(g30.get())+int(g31.get())+int(g32.get())+int(g59.get())
                to1=int(g38.get())+int(g39.get())+int(g40.get())+int(g41.get())+int(g42.get())+int(g61.get())
                to2=int(g48.get())+int(g49.get())+int(g50.get())+int(g51.get())+int(g52.get())+int(g63.get())

                tot3=int(g23.get())+int(g24.get())+int(g25.get())+int(g26.get())+int(g27.get())+int(g58.get())
                tot4=int(g13.get())+int(g14.get())+int(g15.get())+int(g16.get())+int(g17.get())+int(g56.get())
                to3=int(g33.get())+int(g34.get())+int(g35.get())+int(g36.get())+int(g37.get())+int(g60.get())
                to4=int(g43.get())+int(g44.get())+int(g45.get())+int(g46.get())+int(g47.get())+int(g62.get())
            else:
                tot1=int(g18.get())+int(g19.get())+int(g20.get())+int(g21.get())+int(g22.get())
                tot2=int(g28.get())+int(g29.get())+int(g30.get())+int(g31.get())+int(g32.get())
                to1=int(g38.get())+int(g39.get())+int(g40.get())+int(g41.get())+int(g42.get())
                to2=int(g48.get())+int(g49.get())+int(g50.get())+int(g51.get())+int(g52.get())

                tot3=int(g23.get())+int(g24.get())+int(g25.get())+int(g26.get())+int(g27.get())
                tot4=int(g13.get())+int(g14.get())+int(g15.get())+int(g16.get())+int(g17.get())
                to3=int(g33.get())+int(g34.get())+int(g35.get())+int(g36.get())+int(g37.get())
                to4=int(g43.get())+int(g44.get())+int(g45.get())+int(g46.get())+int(g47.get())

            
            tmarks=(10/100)*tot1+(30/100)*tot2+(10/100)*to1+(50/100)*to2
            omarks=(10/100)*tot4+(30/100)*tot3+(50/100)*to4+(10/100)*to3
            tk.Label(leo, text=tot1).grid(row=11, column=3)
            
            tk.Label(leo, text=tot4).grid(row=11, column=2)
            tk.Label(leo, text=tot2).grid(row=11, column=5)
            tk.Label(leo, text=tot3).grid(row=11, column=4)
            tk.Label(leo, text=to3).grid(row=11, column=6)
            tk.Label(leo, text=to1).grid(row=11, column=7)
            tk.Label(leo, text=to4).grid(row=11, column=8)
            tk.Label(leo, text=to2).grid(row=11, column=9)
            tk.Label(leo, text=tot1+tot2+to1+to2).grid(row=13, column=2)
            tk.Label(leo, text=tot3+tot4+to3+to4).grid(row=14, column=2)
            
            l=(omarks/tmarks)*100
            tk.Label(leo, text=l).grid(row=15, column=2)
            
            a=(0.1*int(g13.get()))+(0.3*int(g23.get()))+ (0.1*int(g33.get()))+(0.5*int(g43.get()))
            b=(0.1*int(g18.get()))+(0.3*int(g28.get()))+(0.1*int(g38.get()))+(0.5*int(g48.get()))
            if a>=0.9*b:
                tk.Label(leo, text ="A").grid(row=5, column=10)
                tk.Label(leo, text ="PASS").grid(row=5, column=11)
            elif a >= 0.7 *b:
                tk.Label(leo, text ="B").grid(row=5, column=10)
                tk.Label(leo, text ="PASS").grid(row=5, column=11)
            elif a >= 0.5* b:
                tk.Label(leo, text ="C").grid(row=5, column=10)
                tk.Label(leo, text ="PASS").grid(row=5, column=11)
            elif a >= 0.4*b:
                tk.Label(leo, text ="D").grid(row=5, column=10)
                tk.Label(leo, text ="PASS").grid(row=5, column=11)
            elif a >= 0.33*b:
                tk.Label(leo, text ="E").grid(row=5, column=10)
                tk.Label(leo, text ="PASS").grid(row=5, column=11)
            else:
                tk.Label(leo, text ="F").grid(row=5, column=10)
                tk.Label(leo, text ="FAIL").grid(row=5, column=11)

            c=(0.1*int(g14.get()))+(0.3*int(g24.get()))+ (0.1*int(g34.get()))+(0.5*int(g44.get()))
            d=(0.1*int(g19.get()))+(0.3*int(g29.get()))+(0.1*int(g39.get()))+(0.5*int(g49.get()))
            if c>=0.9*d:
                tk.Label(leo, text ="A").grid(row=6, column=10)
                tk.Label(leo, text ="PASS").grid(row=6, column=11)
            elif c >= 0.7 *d:
                tk.Label(leo, text ="B").grid(row=6, column=10)
                tk.Label(leo, text ="PASS").grid(row=6, column=11)
            elif c >= 0.5* d:
                tk.Label(leo, text ="C").grid(row=6, column=10)
                tk.Label(leo, text ="PASS").grid(row=6, column=11)
            elif c >= 0.4*d:
                tk.Label(leo, text ="D").grid(row=6, column=10)
                tk.Label(leo, text ="PASS").grid(row=6, column=11)
            elif c >= 0.33*d:
                tk.Label(leo, text ="E").grid(row=6, column=10)
                tk.Label(leo, text ="PASS").grid(row=6, column=11)
            else:
                tk.Label(leo, text ="F").grid(row=6, column=10)
                tk.Label(leo, text ="FAIL").grid(row=6, column=11)

            e=(0.1*int(g15.get()))+(0.3*int(g25.get()))+ (0.1*int(g35.get()))+(0.5*int(g45.get()))
            f=(0.1*int(g20.get()))+(0.3*int(g30.get()))+(0.1*int(g40.get()))+(0.5*int(g50.get()))
            if e>=0.9*f:
                tk.Label(leo, text ="A").grid(row=7, column=10)
                tk.Label(leo, text ="PASS").grid(row=7, column=11)
            elif e >= 0.7 *f:
                tk.Label(leo, text ="B").grid(row=7, column=10)
                tk.Label(leo, text ="PASS").grid(row=7, column=11)
            elif e >= 0.5* f:
                tk.Label(leo, text ="C").grid(row=7, column=10)
                tk.Label(leo, text ="PASS").grid(row=7, column=11)
            elif e >= 0.4*f:
                tk.Label(leo, text ="D").grid(row=7, column=10)
                tk.Label(leo, text ="PASS").grid(row=7, column=11)
            elif e >= 0.33*f:
                tk.Label(leo, text ="E").grid(row=7, column=10)
                tk.Label(leo, text ="PASS").grid(row=7, column=11)
            else:
                tk.Label(leo, text ="F").grid(row=7, column=10)
                tk.Label(leo, text ="FAIL").grid(row=7, column=11)

            g=(0.1*int(g16.get()))+(0.3*int(g26.get()))+ (0.1*int(g36.get()))+(0.5*int(g46.get()))
            h=(0.1*int(g21.get()))+(0.3*int(g31.get()))+(0.1*int(g41.get()))+(0.5*int(g51.get()))
            if g>=0.9*f:
                tk.Label(leo, text ="A").grid(row=8, column=10)
                tk.Label(leo, text ="PASS").grid(row=8, column=11)
            elif g >= 0.7 *h:
                tk.Label(leo, text ="B").grid(row=8, column=10)
                tk.Label(leo, text ="PASS").grid(row=8, column=11)
            elif g >= 0.5* h:
                tk.Label(leo, text ="C").grid(row=8, column=10)
                tk.Label(leo, text ="PASS").grid(row=8, column=11)
            elif g >= 0.4*h:
                tk.Label(leo, text ="D").grid(row=8, column=10)
                tk.Label(leo, text ="PASS").grid(row=8, column=11)
            elif g >= 0.33*h:
                tk.Label(leo, text ="E").grid(row=8, column=10)
                tk.Label(leo, text ="PASS").grid(row=8, column=11)
            else:
                tk.Label(leo, text ="F").grid(row=8, column=10)
                tk.Label(leo, text ="FAIL").grid(row=8, column=11)

            i=(0.1*int(g17.get()))+(0.3*int(g27.get()))+ (0.1*int(g37.get()))+(0.5*int(g47.get()))
            j=(0.1*int(g22.get()))+(0.3*int(g32.get()))+(0.1*int(g42.get()))+(0.5*int(g52.get()))
            if i>=0.9*j:
                tk.Label(leo, text ="A").grid(row=9, column=10)
                tk.Label(leo, text ="PASS").grid(row=9, column=11)
            elif i >= 0.7 *j:
                tk.Label(leo, text ="B").grid(row=9, column=10)
                tk.Label(leo, text ="PASS").grid(row=9, column=11)
            elif i >= 0.5* j:
                tk.Label(leo, text ="C").grid(row=9, column=10)
                tk.Label(leo, text ="PASS").grid(row=9, column=11)
            elif i >= 0.4*j:
                tk.Label(leo, text ="D").grid(row=9, column=10)
                tk.Label(leo, text ="PASS").grid(row=9 , column=11)
            elif i >= 0.33*j:
                tk.Label(leo, text ="E").grid(row=9, column=10)
                tk.Label(leo, text ="PASS").grid(row=9, column=11)
            else:
                tk.Label(leo, text ="F").grid(row=9, column=10)
                tk.Label(leo, text ="FAIL").grid(row=9, column=11)


            if opt!=0:
                ik=(0.1*int(g56.get()))+(0.3*int(g58.get()))+ (0.1*int(g60.get()))+(0.5*int(g61.get()))
                jk=(0.1*int(g57.get()))+(0.3*int(g59.get()))+(0.1*int(g61.get()))+(0.5*int(g63.get()))
                if ik>=0.9*jk:
                    tk.Label(leo, text ="A").grid(row=9, column=10)
                    tk.Label(leo, text ="PASS").grid(row=9, column=11)
                elif ik >= 0.7 *jk:
                    tk.Label(leo, text ="B").grid(row=9, column=10)
                    tk.Label(leo, text ="PASS").grid(row=9, column=11)
                elif ik >= 0.5* jk:
                    tk.Label(leo, text ="C").grid(row=9, column=10)
                    tk.Label(leo, text ="PASS").grid(row=9, column=11)
                elif ik >= 0.4*jk:
                    tk.Label(leo, text ="D").grid(row=9, column=10)
                    tk.Label(leo, text ="PASS").grid(row=9 , column=11)
                elif ik >= 0.33*jk:
                    tk.Label(leo, text ="E").grid(row=9, column=10)
                    tk.Label(leo, text ="PASS").grid(row=9, column=11)
                else:
                    tk.Label(leo, text ="F").grid(row=9, column=10)
                    tk.Label(leo, text ="FAIL").grid(row=9, column=11)


            #teachers remarks
            tk.Label(leo, text="Teacher's Remarks",font=("times",15),bg=head).grid(row=16, column=0)
            tk.Label(leo, text=g53.get(),font=("times",15)).grid(row=17, column=0)

            #teachers name
            tk.Label(leo, text="Teacher's Name",font=("times",15),bg=head).grid(row=16, column=3)
            tk.Label(leo, text=g54.get(),font=("times",15)).grid(row=17, column=3)

            #date
            tk.Label(leo, text="Date",font=("times",15),bg=head).grid(row=16, column=5)
            tk.Label(leo, text=g55.get(),font=("times",15)).grid(row=17, column=5)

            #button to go back
            n2=tk.Button(leo, text="Back",font=("times",15), bg="blue",fg="white", command=leo.destroy) 
            n2.grid(row=18, column=3)

        # button to display completed report card 
        bn1=tk.Button(root, text="Generate", bg="green", command=heh) 
        bn1.grid(row=22, column=0)
        # button to reset
        bn2=tk.Button(root, text="Reset", bg="red", command=reset) 
        bn2.grid(row=22, column=3)

        # button to go back to main menu
        bn2=tk.Button(root, text="Back", bg="blue",fg="white", command=root.destroy) 
        bn2.grid(row=22, column=5)

#MAIN PROGRAM

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



#tkinter setup

lvl=tk.Tk()
lvl.title("WELCOME")
lvl.geometry("815x611")
ph=tk.PhotoImage(file="Capture.png")
l=tk.Label(lvl,image=ph)
l.place(x=0,y=0)


#retrieving data from text files
f2=open("welcome.txt","r")
welcome1=f2.read()
f2.close()
f3=open("text.txt","r")
welcome2=f3.read()
f3.close()

#putting data in place

fr=tk.Frame(lvl,width=495,height=35)
fr.place(x=140,y=100)
l1=tk.Label(fr,text=welcome1)
l1.configure(bg="grey",fg="white",justify="center",font=("Poor Richard",21), height=0,width=0)
l1.place(x=0,y=0)

fr2=tk.Frame(lvl,width=430,height=118)
fr2.place(x=165,y=150)
l2=tk.Label(fr2,text=welcome2)
l2.configure(bg="silver",fg="black",justify="center",font=("Poor Richard",18))
l2.place(x=0,y=0)

#start/exit commands
fr3=tk.Frame(lvl,width=200,height=220)
fr3.place(x=300,y=300)
butt1=tk.Button(fr3,text="Start",command=start)
butt1.configure(height=5,width=22,bg="gainsboro",font=("times",10))
butt1.place(x=20,y=10)
butt2=tk.Button(fr3,text="Exit",command=lvl.destroy)
butt2.configure(height=5,width=22,bg="whitesmoke",font=("times",10))
butt2.place(x=20,y=110)


