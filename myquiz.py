import tkinter as tk
from tkinter import messagebox
import os
file_path = "quiz_questions.txt"
def w1():
    main=tk.Tk()
    main.title("QUIZ APP.")

    main.geometry("500x500")

    l1=tk.LabelFrame(main,text="QUIZ",bg="green")
    l1.place(x=100,y=50)

    l2=tk.Label(l1,bg="blue",text="HELLO WLCOME TO THE ELECTRONICS AND \nCOMMUNICATION QUIZ.")
    l2.pack()


    l3=tk.Label(text="NAME :").place(x=100 ,y=150)

    name=tk.Entry(justify="left")   
    name.place(x=150,y=150)
    def question():
        main.destroy()
        count=[1,0]
        quest=[]
        opt=[]
        key=[]
        def question_count():
            
            def save_quest():
                if q3.get() and q7.get() and q8.get()!="":
                    count[0]=count[0]+1
                    q2.config(text=f"ENTER YOUR {count[0]} QUESTION .")
                    quest.append(f"{count[0]-1}.{q3.get()}")
                    opt.append(f"1.{q4.get()},2.{q5.get()},3.{q6.get()},4.{q7.get()}")
                    key.append(q8.get())
                    print(quest,opt,key)
                    q3.delete(0,len(q3.get()))
                    q4.delete(0,len(q4.get()))
                    q5.delete(0,len(q5.get()))
                    q6.delete(0,len(q6.get()))
                    q7.delete(0,len(q7.get()))
                    q8.delete(0,len(q8.get()))               
                else:
                    messagebox.showwarning("BLANK ERROR","FILL ALL THE BLANKS & ADD ")   
            def save():
                if os.path.exists(file_path):
                    messagebox.showinfo("CONFIRM",f"THE {count[0]-1} QUESTIONS YOU ENTERED ARE ADDED TO QUIZ")
                    with open(file_path, 'w') as f:
                        for i in range(count[0]-1):
                            f.write(f"{quest[i]}||{opt[i]}||{key[i]}\n")
                    side.destroy()        
            def myexit():
                if count[1]==0:
                    messagebox.showwarning("EXIT THE CHANNEL","YOU DIDN'T CHANGED ANY QUESTIONS DEFAULT ONES ARE CARRIED")
                    count[1]+=1
                else:
                    exit()                  
            side=tk.Tk()
            side.title("QUESTION CHANGING PANEL.")
            side.geometry("500x500")
            q1=tk.LabelFrame(side,bg="green",text="YOU CAN CHANGE QUESTIONS IN QUIZ HERE")
            q1.place(x=50,y=50)
            q2=tk.Label(q1,bg="RED",text=f"ENTER YOUR {count[0]} QUESTION .")
            q2.pack_configure(padx=10,pady=10)
            q3=tk.Entry(q1)
            q3.pack_configure(padx=10,pady=5)
            q9=tk.Label(q1,bg="RED",text=f"ENTER YOUR OPTIONS HERE.")
            q9.pack_configure(padx=10,pady=10)
            q4=tk.Entry(q1)
            q4.pack_configure(padx=10,pady=5)
            q5=tk.Entry(q1)
            q5.pack_configure(padx=10,pady=5)
            q6=tk.Entry(q1)
            q6.pack_configure(padx=10,pady=5)
            q7=tk.Entry(q1)
            q7.pack_configure(padx=10,pady=5)
            q10=tk.Label(q1,bg="RED",text=f"ENTER THE KEY HERE FROM OPTIONS WITH NUMBER LIKE 1 OR 2...")
            q10.pack_configure(padx=10,pady=10)
            q8=tk.Entry(q1)
            q8.pack_configure(padx=10,pady=5)
            q11=tk.Button(text="ADD QUESTION",command=save_quest,pady="3",border="5",bg="silver",fg="black")
            q11.place(x=350,y=400)
            q12=tk.Button(text="SAVE",command=save,pady="3",border="5",bg="silver",fg="black")
            q12.place(x=200,y=400)
            q13=tk.Button(text="EXIT",command=myexit,pady="3",border="5",bg="silver",fg="black")
            q13.place(x=50,y=400)
            side.mainloop()
        question_count()  
    def load_question_from_file():
        ques=[]
        ans=[]
        key=[]   
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                for line in f:
                    l1,l2 ,l3 = line.strip().split('||')
                    ques.append(l1)
                    ans.append(l2.split(",")) 
                    key.append(int(l3))
        w2(ques,ans,key)                         
    def verify_name():
        if name.get()=="":
            messagebox.showerror("NAME ERROR","ENTER YOUR NAME")
        elif name.get() in ["yateesh","YATEESH"]:
            question()    
        else:
            load_question_from_file()        
    def clear():
        for item in main.winfo_children():
            item.destroy()        
    def w2(ques,ans,key):
        name_1=name.get()
        clear()
        l4=tk.Label(text=f"HELLO {name_1.upper()},WELCOME TO THE QUIZ.\nREAD THE BELOW RULES CAREFULLY .")
        l4.place(x=150,y=100)

        l5=tk.LabelFrame(main,bg="red",text="RULES AND REGULATIONS:")
        l5.place(x=100,y=150)
    
        l6=tk.Label(l5,bg="green",text="1.ONE POINT AWARDED FOR CORRECT ANSWER.\n2.NO NEGATIVE MARKING.\n3.CLOSING THE WINDOW IS CONSIDERED AS FAIL.\n4.THERE ARE 5 QUESTIONS IN QUIZ.\n5.EACH CONTAIN 4 OPTIONS & CARRY EQUAL MARKS.\n6.ONLY ONE CHANCE IS ALLOWED TO ANSWER,\nFIRST RESPONSE WILL BE RECORDED.\n\n      ALL THE BEST!")
        l6.pack()

        var1=tk.IntVar()
        b1=tk.Checkbutton(main,variable=var1,onvalue=1,offvalue=0)
        b1.place(x=100,y=400)
    
        l7=tk.Label(main,text="I AGREE TERMS & CONDITIONS.")
        l7.place(x=130,y=400)
    
        def check():
            if var1.get()==0:
                messagebox.showerror("CHECKBOX ERROR","CLICK ON THE CHECK BOX.")
            else:
                i=0
                w3(name_1,i,ques,ans,key)    
        b2=tk.Button(main,text="CONTINUE",command=check,pady="3",border="5")
        b2.place(x=400,y=400)  
    go1=tk.Button(text="CONTINUE",bg="silver",fg="black",pady="3",border="5",command=verify_name)
    go1.place(x=400,y=400)
    sc=[0]   
    ver_que=[] 
    def w3(name,i,ques,ans,key):
        num=i
        name_2=name
        clear()
        try:
            l8=tk.Label(text=f"HELLO {name.upper()} HERE IS YOUR {num+1} QUESTION.").place(x=100,y=50)
            l9=tk.LabelFrame(main,text=f"{ques[num].upper()}")
            l9.place(x=100,y=100)
            var_2=tk.IntVar()
            l10=tk.Radiobutton(l9,text=f"{ans[num][0].upper()}",variable=var_2,value=1).pack(anchor="w")
            l11=tk.Radiobutton(l9,text=f"{ans[num][1].upper()}",variable=var_2,value=2).pack(anchor="w") 
            l12=tk.Radiobutton(l9,text=f"{ans[num][2].upper()}",variable=var_2,value=3).pack(anchor="w")
            l13=tk.Radiobutton(l9,text=f"{ans[num][3].upper()}",variable=var_2,value=4).pack(anchor="w") 
            l14=tk.Label(main,text=f" ")
            l14.place(x=100,y=300)
        except:
            clear()
            def last():
                main.after(1000,main.destroy())
            l15=tk.Label(main,text=f"{name.upper()} YOUR SCORE IS :{sum(sc)}").place(x=100,y=200)
            exit_button=tk.Button(main,text=f"EXIT",command=last,pady="3",border="5").place(x=400,y=400)
        def check_key():
                if(var_2.get()==key[num] and num+1 not in ver_que):
                    l14.config(text=f"CORRECT ANSWER.")
                    sc.append(1) 
                    ver_que.append(num+1)  
                elif(num+1 in ver_que):
                    l14.config(text="RESPONSE IS ALREADY RECORDED.")    
                elif var_2.get()==0 :
                    messagebox.showwarning("OPTION ERROR","SELECT ANY ONE OPTION.")
                else:
                    l14.config(text=f"WRONG ANSWER.CORRECT OPTION IS {ans[num][(key[num])-1].upper()}")         
                    ver_que.append(num+1)
        def next_call():
            if var_2.get()!=0 and num<len(ques):
                w3(name_2,num+1,ques,ans,key)
            else:
                messagebox.showwarning("QUESTION ERROR","CANT SKIP THE QUESTION")    
        if(num<len(ques)):
            b3=tk.Button(main,text="VERIFY",command=check_key,pady="3",border="5").place(x=300,y=400)
            b4=tk.Button(main,text="NEXT",command=next_call,pady="3",border="5").place(x=400,y=400)    
    
    main.mainloop()
w1()    