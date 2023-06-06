#HALF YEARLY
import tkinter as tk

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
#------------------------------------------------------------------------------    
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
#------------------------------------------------------------------------------        
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
#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------
        def reset2():
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
#------------------------------------------------------------------------------
#defining function to generate report card
        def gen2():
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
            mhmkm=tk.Frame(fg,width=190,height=65,bg="white")
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
#------------------------------------------------------------------------------
        # button to display completed report card 
        bn1=tk.Button(ok, text="Generate", bg="green", command=gen2) 
        bn1.grid(row=22, column=0)
        
        # button to reset
        bn2=tk.Button(ok, text="Reset", bg="red", command=reset2) 
        bn2.grid(row=22, column=3)

        # button to go back to main menu
        bn2=tk.Button(ok, text="Back", bg="blue",fg="white", command=ok.destroy) 
        bn2.grid(row=22, column=5)
        ok.mainloop() 

