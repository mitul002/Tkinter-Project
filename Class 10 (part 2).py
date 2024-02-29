from tkinter import *

def login():
    print(f"Username is :{user.get()}")  #gate() is used for take take value from entry/input box to the program
    print(f"Password is :{password.get()}")

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
user=Entry(f1)
user.grid(row=1, column=1)

password=Label(f1,text="Input Password :",borderwidth=10)
password.grid(row=2)
password=Entry(f1)  #Entry() is used for making input box
password.grid(row=2, column=1)

B1=Button(f1,text="LOG IN", command=login, padx=39, bg="slateblue",fg="white")
B1.grid(row=3,column=1)


root.mainloop()