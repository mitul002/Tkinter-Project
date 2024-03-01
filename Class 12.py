from tkinter import *

def login():
    print(f"Username is :{userValue.get()}")  #gate() is used for take take value from entry/input box to the program
    print(f"Password is :{passValue.get()}")
    print(f"Phone no :{phoneValue.get()}")
    a= agreementValue.get()
    if a==1:
        print("Agreed")
    else:
        print("Not Agreed")

    with open("records.txt", "a") as file:
        file.write(f"Username is :{userValue.get()}\nPassword is :{passValue.get()}"
                   f"\nPhone no :{phoneValue.get()}\nAgreement :{agreementValue.get()} \n\n")

root=Tk()
root.title("Sign Up Form")
root.geometry("540x360")
root.maxsize(1080,720)

Title=Label(text="Sign Up Form", font="arial 18 bold", bg="slateblue",fg="white", padx=20)
Title.pack(fill=X)


f1=Frame(relief=SUNKEN, borderwidth=2,padx=10, pady=20)
f1.pack()
'''
grid() is used instead of pack(). grid() has extra advantage. We can define column and row in grid()
if there is no parameter between grid() it means colum=0, row=0
'''
user=Label(f1,text="Input Username :",borderwidth=10)
user.grid(row=1)

userValue=StringVar()
user=Entry(f1, textvariable=userValue)      #Entry() is used for making input box
user.grid(row=1, column=1)



password=Label(f1,text="Input Password :",borderwidth=10)
password.grid(row=2)

passValue=StringVar()   #what type of value will be inputed that defined here. Types are StringVar(), IntVar(), BooleanVar(), DoubleVar
password=Entry(f1, textvariable=passValue)
password.grid(row=2, column=1)



phone=Label(f1,text="Input Phone      :",borderwidth=10)
phone.grid(row=3)

phoneValue=IntVar()
phone=Entry(f1, textvariable=phoneValue)
phone.grid(row=3, column=1)

#we need to use variable instead of textvariable for checkbox
agreementValue=BooleanVar()
agreement=Checkbutton(f1,text="Terms & Condition", borderwidth=5, variable=agreementValue)
agreement .grid(row=4, column=1)


B1=Button(f1,text="LOG IN", command=login, padx=39, bg="slateblue",fg="white")
B1.grid(row=5,column=1)


root.mainloop()