#unit test
import tkinter as tk

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

#------------------------------------------------------------------------------
    
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

#------------------------------------------------------------------------------
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

#------------------------------------------------------------------------------
        
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
        
#------------------------------------------------------------------------------
        
        def reset1():
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
#------------------------------------------------------------------------------
#defining function to generate report card
        def gen1():
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
            

#------------------------------------------------------------------------------
            
            #putting in org name, test name and student details
            
            if clsss in ["11-PCM","11-PCB","11-COMMERCE","11-ARTS"]:
                itsi="11"
            elif clsss in ["12-PCM","12-PCB","12-COMMERCE","12-ARTS"]:
                itsi="12"
            else:
                itsi=str(clsss)
            mhmk=tk.Frame(f,width=215,height=85,bg="white")
            mhmk.grid(row=0,column=1,columnspan=4)
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
#------------------------------------------------------------------------------
            
        # button to display completed report card 
        bn1=tk.Button(ut, text="Generate", bg="green", command=gen1) 
        bn1.grid(row=22, column=0)

        # button to reset
        bn2=tk.Button(ut, text="Reset", bg="red", command=reset1) 
        bn2.grid(row=22, column=3)

        # button to go back to main menu
        bn2=tk.Button(ut, text="Back", bg="blue",fg="white", command=ut.destroy) 
        bn2.grid(row=22, column=5)
        ut.mainloop()
