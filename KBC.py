from tkinter import *
import pygame
from PIL import ImageTk, Image
import os
import time
from tkinter import messagebox

pygame.init()
root=Tk()
root.title("Kaun Banega Crorepati")
root.geometry('1600x800+0+0')
root.config(bg='black')

#=========================FRAME=======================================================
f=Frame(root,bg='black').grid()

f1=Frame(root,bg='black',width=900,height=600,bd=20,padx=70)
f1.grid(row=0,column=0)
f2=Frame(root,bg='black',width=452,height=600,bd=20)
f2.grid(row=0,column=1)

f11=Frame(f1,bg='black',width=1000,height=200,bd=20)
f11.grid(row=0,column=0)
f12=Frame(f1,bg='black',width=1000,height=200,bd=20)
f12.grid(row=1,column=0)
f13=Frame(f1,bg='black',width=1000,height=200,bd=20)
f13.grid(row=2,column=0)
#===========================IMAGES FUNCTION============================================

##def change50_50():
##    global index
##    canvas = Canvas(f11,bg='black',width=160,height=80)
##    canvas.grid(row=0, column=0)
##    canvas.delete('all')
##    Img50_50X=ImageTk.PhotoImage(Image.open('KBC/img50X.jpg'))
##    canvas.create_image(80,40,image = Img50_50X)
##    canvas.image=Img50_50X
##    #clear50_50()
##    
##    c=0
##    if A1.get()!=Answers[index] and c!=2:
##        A1.set=("")
##        c+=1
##    if A2.get()!=Answers[index] and c!=2:
##        A2.set=("")
##        c+=1
##    if A3.get()!=Answers[index] and c!=2:
##        A3.set=("")
##        c+=1
##    if A4.get()!=Answers[index] and c!=2:
##        A4.set=("")
##        c+=1
##    


def changeAudience():
    canvas = Canvas(f11,bg='black',width=160,height=80)
    canvas.grid(row=0, column=2)
    canvas.delete('all')
    ImgAudienceX=ImageTk.PhotoImage(Image.open('KBC/AudienceX.jpg'))
    canvas.create_image(80,40,image = ImgAudienceX)
    canvas.image=ImgAudienceX


def changePhone():
    canvas = Canvas(f11,bg='black',width=160,height=80)
    canvas.grid(row=0, column=4)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/PhoneX.jpg'))
    canvas.create_image(80,40,image = ImgPhoneX)
    canvas.image=ImgPhoneX


def MillionPicture0():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture01.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX


def MillionPicture1():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture1.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX


def MillionPicture2():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture2.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture3():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture3.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture4():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture4.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture5():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture5.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture6():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture6.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture7():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture7.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture8():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture8.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture9():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture9.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture10():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture10.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture11():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture11.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture12():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture12.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture13():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture13.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture14():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture14.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX

def MillionPicture15():
    canvas = Canvas(f2,bg='black',width=430,height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    ImgPhoneX=ImageTk.PhotoImage(Image.open('KBC/Picture15.png'))
    canvas.create_image(215,300,image = ImgPhoneX)
    canvas.image=ImgPhoneX




#============================IMAGES=====================================================
CentreImg=ImageTk.PhotoImage(Image.open('KBC/centre.jpg'))
LogoCentre = Button(f12, image= CentreImg ,bg='black',width=300,height=200)
LogoCentre.grid()

##Img50_50=ImageTk.PhotoImage(Image.open('KBC/img50.jpg'))
##Live50_50 = Button(f11, image=Img50_50 ,command=change50_50,bg='black',width=160,height=80,padx=10)
##Live50_50.grid(row=0,column=0)

space=Label(f11,bg='black',width=10)
space.grid(row=0,column=1)

ImgAudience=ImageTk.PhotoImage(Image.open('KBC/Audience.jpg'))
LiveAudience = Button(f11, image=ImgAudience ,command=changeAudience,bg='black',width=160,height=80,padx=10)
LiveAudience.grid(row=0,column=2)

space=Label(f11,bg='black',width=10)
space.grid(row=0,column=3)

ImgPhone=ImageTk.PhotoImage(Image.open('KBC/Phone.jpg'))
LivePhone = Button(f11, image=ImgPhone ,command=changePhone,bg='black',width=160,height=80,padx=10)
LivePhone.grid(row=0,column=4)

ImgScore=ImageTk.PhotoImage(Image.open('KBC/Picture01.png'))
Score=Button(f2,image=ImgScore,bg='black',height=600,width=430)
Score.grid(row=0,column=0)

#============================CLOCK==================================================
clock = Label(f12,bg='slateblue',fg='white',font=('arial',15,'bold'))
clock.grid(row=1,column=0)

count=30
def clockTime():
    global count
    
    count-=1
    if count!=0 and count>=0:
        clock.after(1000,clockTime)
        clock.config(text=count)
    elif count==-1:
        clock.config(text="No Time Limit")
    elif (count<0 or count==0):
        count='O'
        clock.config(text=count)
        msg=messagebox.showinfo("KBC","TIME OVER\n YOU LOOSE!!!")
        root.destroy()
    else:
        pass
    

#==============================Questions and Answers=====================================

Q=StringVar()
Q2=StringVar()
Q3=StringVar()
Q4=StringVar()

A1=StringVar()
A2=StringVar()
A3=StringVar()
A4=StringVar()

clockTime()

Q.set("Q1. Who is the Prime Minister of India in 2016")
A1.set('Manmohan Singh')
A2.set('Narendra Modi')
A3.set('Sonia Gandhi')
A4.set('Indira Ganhi')

Questions=[('Q1. Who is the Prime Minister of India in 2016'),('Q2: What is 2*3+10/5-2'),
           ('Q3. Who is the National Animal of India'),('Q4. What is 2+2 ?'),('Q5. Which Color has Highest wavelength ?'),
           ("Q6. How many Seconds are there in a Minute "),('Q7. _____ is the first woman to head a public sector bank.'),
           ("Q8. Where is Bose institute ?"),("Q.9 World Tourism Day is celebrated on- "),
           ('Q.10 When is the International Yoga Day celebrated ?'),("Q.11 The motif of 'Hampi with Chariot' is printed on the reverse of which currency note ? "),
           ("Q.12 'Line of Blood' is a book written by whom?"),("Q.13 The two-day festival 'North East Calling', is organized by which ministry ?"),
           ("Q.14 A major in-stream use of water is for -"),('Q.15  1+1 =__ ?')]

Options=[('Manmohan Singh','Narendra Modi','Sonia gandhi','indira gandhi'),
         ('1.5','1','6','0'),
         ('Peacock','Tiger','lion','Monkey'),
         ('4','22','2','2+2'),
         ('Blue','Violet','Yellow','Red'),
         ('60s','1s','120s','30s'),
         ('Shikha Sharma','Chanda Kochar','Usha Anan','Arundhati Bhattacharya'),
         ('Dispur','Kolkata','Mumbai','New Delhi'),
         ('September 12','September 25','September 27','September 29'),
         ('June 21 ','March 21 ','April 22 ','May 31'),
         (' One Rupee Note','Rs. 500 note',' Rs. 50 note','Rs. 1000 note'),
         ('Ursula Vernon','Amal EI-Mohtar','Diksha Basu','Bairaj Khanna'),
         ('Ministry of DoNER','Ministry of External Affairs','Ministry of Home Affairs','Ministry of Defence'),
         ('dissolving industrial wastes','agricultural irrigation','domestic use','producing hydroelectric power'),
         ('11','1','2','0')]

Answers = [('Narendra Modi'),('6'),('Tiger'),('4'),('Red'),('60s'),('Arundhati Bhattacharya'),
           ('Kolkata'),('September 27'),('June 21 '),(' Rs. 50 note'),('Bairaj Khanna'),
           ('Ministry of DoNER'),('producing hydroelectric power'),('2')]

index=0
fall=0

def select_img():
    global index
    global count
    global fall
        
    if index==0:
        MillionPicture1()
        count=30
    

    elif index==1:
        MillionPicture2()
        count=30
        clockTime()
    
    elif index==2:
        MillionPicture3()
        count=30
        clockTime()
    elif index==3:
        MillionPicture4()
        count=30
        clockTime()
    elif index==4:
        MillionPicture5()
        count=60
        fall=1
        clockTime()
    elif index==5:
        MillionPicture6()
        count=60
        clockTime()
    elif index==6:
        MillionPicture7()
        count=60
        clockTime()
    elif index==7:
        MillionPicture8()
        count=1000
        #clock.config(text="No Time Limit")
        
    elif index==8:
        MillionPicture9()
        #clock.config(text="No Time Limit")
        count=1000
    elif index==9:
        MillionPicture10()
        count=1000
        #clock.config(text="No Time Limit")
    elif index==10:
        MillionPicture11()
        #clock.config(text="No Time Limit")
        count=1000
    elif index==11:
        MillionPicture12()
        #clock.config(text="No Time Limit")
        count=1000
    elif index==12:
        MillionPicture13()
        #clocconfig(text="No Time Limit")
        count=1000
    elif index==13:
        MillionPicture14()
        #clock.config(text="No Time Limit")
        count=1000
    elif index==14:
        MillionPicture15()
        #clock.config(text="No Time Limit")
        count=1000
    else :
        pass
    index+=1

    if index==15:
        msg=messagebox.showinfo("KBC","Congo!!!\n\tYOU WON")
        if msg=='ok':
            root.destroy()
            

    



def checkA1():
    
    global index
    global fall
    Q.set(Questions[index])
    
    A1.set(Options[index][0])
    A2.set(Options[index][1])
    A3.set(Options[index][2])
    A4.set(Options[index][3])
    print(A1.get())
    if A1.get()==Answers[index]:
        select_img()
##    else:
##        if fall==0:
##            msg=messagebox.showinfo("KBC","Wrong Option\nYOU LOST")
##            if msg=='ok':
##                root.destroy()
##
##        elif fall==1:
##            msg=messagebox.showinfo("KBC","Wrong Option\nYOU Won 1000 Euro")
##            if msg=='ok':
##                root.destroy()
    

def checkA2():
    global fall
    Q.set(Questions[index])
    
    A1.set(Options[index][0])
    A2.set(Options[index][1])
    A3.set(Options[index][2])
    A4.set(Options[index][3])
    print(A2.get()," =",Answers[index])
    if A2.get()==Answers[index]:
        select_img()
        #count=30
##    else:
##        if fall==0:
##            msg=messagebox.showinfo("KBC","Wrong Option\nYOU LOST")
##            if msg=='ok':
##                root.destroy()
##
##        elif fall==1:
##            msg=messagebox.showinfo("KBC","Wrong Option\nYOU Won 1000 Euro")
##            if msg=='ok':
##                root.destroy()
    

        


def checkA3():
    global fall
    Q.set(Questions[index])
    
    A1.set(Options[index][0])
    A2.set(Options[index][1])
    A3.set(Options[index][2])
    A4.set(Options[index][3])

    if A3.get()==Answers[index]:
    
        select_img()
##    else:
##        if fall==0:
##            msg=messagebox.showinfo("KBC","Wrong Option\nYOU LOST")
##            if msg=='ok':
##                root.destroy()
##
##        elif fall==1:
##            msg=messagebox.showinfo("KBC","Wrong Option\nYOU Won 1000 Euro")
##            if msg=='ok':
##                root.destroy()
##    


def checkA4():
    global count
    global fall
    Q.set(Questions[index])

    A1.set(Options[index][0])
    A2.set(Options[index][1])
    A3.set(Options[index][2])
    A4.set(Options[index][3])

    if A4.get()==Answers[index]:
        select_img()
        #count=30
##    else:
##        if fall==0:
##            msg=messagebox.showinfo("KBC","Wrong Option\nYOU LOST")
##            if msg=='ok':
##                root.destroy()
##
##        elif fall==1:
##            msg=messagebox.showinfo("KBC","Wrong Option\nYOU Won 1000 Euro")
##            if msg=='ok':
##                root.destroy()
##    


def clear50_50():
    global index
    c=0
    if A1.get()!=Answers[index] and c!=2:
        A1.set=("")
        c+=1
    if A2.get()!=Answers[index] and c!=2:
        A2.set=("")
        c+=1
    if A3.get()!=Answers[index] and c!=2:
        A3.set=("")
        c+=1
    if A4.get()!=Answers[index] and c!=2:
        A4.set=("")
        c+=1

def change50_50():
    global index
    canvas = Canvas(f11,bg='black',width=160,height=80)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    Img50_50X=ImageTk.PhotoImage(Image.open('KBC/img50X.jpg'))
    canvas.create_image(80,40,image = Img50_50X)
    canvas.image=Img50_50X
    #clear50_50()
    
    c=0
    if A1.get()!=Answers[index] and c!=2:
        A1.set=("")
        c+=1
    if A2.get()!=Answers[index] and c!=2:
        A2.set=("")
        c+=1
    if A3.get()!=Answers[index] and c!=2:
        A3.set=("")
        c+=1
    if A4.get()!=Answers[index] and c!=2:
        A4.set=("")
        c+=1
    
    
#==============================TEXT,LABELS,BUTTONS=======================================



txtQuestion=Entry(f13,textvariable=Q,justify=CENTER,font=('arial',18,'bold'),bg='blue',fg='white', bd=5,width=50)
txtQuestion.grid(row=0,column=0,columnspan=4,pady=4)


l_Q1 = Label(f13,justify=CENTER,text='A:',font=('arial',14,'bold'),bg='black',fg='white', bd=5)
l_Q1.grid(row=1,column=0,pady=4,sticky=W)
txt_Q1 = Button(f13,command=checkA1,textvariable=A1,width=17,height=2,bg='blue',fg='white',bd=1,justify=CENTER, font=('arial',14,'bold'))
txt_Q1.grid(row=1, column=1,pady=4)


l_Q2 = Label(f13,justify=LEFT,text='B: ',font=('arial',14,'bold'),bg='black',fg='white', bd=5)
l_Q2.grid(row=1,column=2,pady=4,sticky=W)
txt_Q2 = Button(f13,command=checkA2,textvariable=A2,width=17,height=2,bg='blue',fg='white',bd=1,justify=CENTER, font=('arial',14,'bold'))
txt_Q2.grid(row=1, column=3,pady=4)


l_Q3 = Label(f13,justify=LEFT,text='C: ',font=('arial',14,'bold'),bg='black',fg='white', bd=5)
l_Q3.grid(row=2,column=0,pady=4,sticky=W)
txt_Q3 = Button(f13,textvariable=A3,command=checkA3,width=17,height=2,bg='blue',fg='white',bd=1,justify=CENTER, font=('arial',14,'bold'))
txt_Q3.grid(row=2, column=1,pady=4)


l_Q4 = Label(f13,justify=LEFT,text='D: ',font=('arial',14,'bold'),bg='black',fg='white', bd=5)
l_Q4.grid(row=2,column=2,pady=4,sticky=W)
txt_Q4 = Button(f13,command=checkA4,textvariable=A4,width=17,height=2,bg='blue',fg='white',bd=1,justify=CENTER, font=('arial',14,'bold'))
txt_Q4.grid(row=2, column=3,pady=4)

Img50_50=ImageTk.PhotoImage(Image.open('KBC/img50.jpg'))
Live50_50 = Button(f11, image=Img50_50 ,command=change50_50,bg='black',width=160,height=80,padx=10)
Live50_50.grid(row=0,column=0)


root.mainloop()


input("press ENTER to EXIT")
