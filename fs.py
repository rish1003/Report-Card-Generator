#FINALS
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

#------------------------------------------------------------------------------
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
#------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------

        def reset3():
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
#------------------------------------------------------------------------------
#defining function to generate report card
        def gen3():
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
            mhmkm=tk.Frame(leo,width=170,height=80,bg="white")
            mhmkm.grid(row=0,column=1,columnspan=8)
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

#------------------------------------------------------------------------------

        # button to display completed report card 
        bn1=tk.Button(root, text="Generate", bg="green", command=gen3) 
        bn1.grid(row=22, column=0)
        # button to reset
        bn2=tk.Button(root, text="Reset", bg="red", command=reset3) 
        bn2.grid(row=22, column=3)

        # button to go back to main menu
        bn2=tk.Button(root, text="Back", bg="blue",fg="white", command=root.destroy) 
        bn2.grid(row=22, column=5)
        root.mainloop()
