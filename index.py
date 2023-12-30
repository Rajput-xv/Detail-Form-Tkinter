from tkinter import *
import tkinter.ttk as tkk
from PIL import Image, ImageTk

def clicked():

    btn1.configure(text="SUBMITTED",bg='green')
    
    res=label.cget("text")+"   :   "+txt.get()
    n=Label(window,text=res,font=("Algerian", 30),fg="red")
    n.grid(row=6,column=4,pady=(60,0),padx=(30,0))

    res1=label1.cget("text")+"   :   "+txt1.get()
    n1=Label(window,text=res1,font=("Algerian", 30),fg="red")
    n1.grid(row=7,column=4,pady=(10,0),padx=(30,0))

    v=sv.get()
    t="MALE" if v==1 else "FEMALE"
    res2=label2.cget("text")+"   :   "+t
    n2=Label(window,text=res2,font=("Algerian", 30),fg="red")
    n2.grid(row=8,column=4,pady=(10,0),padx=(30,0))

    res3=label3.cget("text")+"   :   "+cv.get()
    n3=Label(window,text=res3,font=("Algerian", 30),fg="red")
    n3.grid(row=9,column=4,pady=(10,0),padx=(30,0))

    image_fun()
    
def resize_image(image, new_width, new_height):
     return image.resize((new_width, new_height), Image.LANCZOS)

def image_fun():
    path = "C:/Users/acer/Desktop/pic1.png"
    ic=Image.open(path)
    ic = resize_image(ic,250,450)
    photo=ImageTk.PhotoImage(ic)
    l = Label(window, image=photo)
    l.image=photo
    l.grid(row=6,rowspan=5,column=5)

window = Tk()
window.title("RAJPUT")
window.geometry('1100x700')
window.configure(bg='lightblue') 

l1=Label(window,text="INFORMATION FORM",font=("Algerian", 50),fg='orange')
l1.grid(column=4,pady=(10,0))

label = Label(window, text="NAME", font=("Algerian", 20),fg="dark blue")
label.grid(row=1,column=2,pady=(30, 0),padx=(20,0))

txt =Entry(window,width=20,font=("Algerian", 20),fg='purple')
txt.grid(row=1,column=4,pady=(30, 0))

label1 = Label(window, text="ADDRESS", font=("Algerian", 20),fg="dark blue")
label1.grid(row=2,column=2,pady=(10, 0),padx=(20,0))

txt1 =Entry(window,width=20,font=("Algerian", 20),fg='purple')
txt1.grid(row=2,column=4,pady=(10, 0))

label2 = Label(window, text="GENDER ", font=("Algerian", 20),fg="dark blue")
label2.grid(row=3,column=2,pady=(10, 0),padx=(20,0))

sv = IntVar()
r1=Radiobutton(window,text=" MALE",value=1,font=("Algerian",20),fg='purple',variable=sv)
r1.grid(row=3,column=4,pady=(10, 0))
r2=Radiobutton(window,text="FEMALE",value=2,font=("Algerian",20),fg='purple',variable=sv)
r2.grid(row=3,column=5,pady=(10, 0))
r1.select()

label3 = Label(window, text="EDUCATION", font=("Algerian", 20),fg="dark blue")
label3.grid(row=4,column=2,pady=(10, 0),padx=(20,0))

cv=StringVar()
s=tkk.Style()
s.configure("TCombobox", foreground="purple")
co=tkk.Combobox(window,textvariable=cv,font=("Algerian", 20),style="TCombobox")
co['values']=("PG","UG","XII","X")
co.current(1)
co.grid(row=4,column=4,pady=(10, 0))

btn1=Button(window,text="SUBMIT",bg="red",fg="white",
           font=("Algerian",20),command=clicked)
btn1.grid(row=5,column=4,pady=(30, 0))


window.mainloop()
