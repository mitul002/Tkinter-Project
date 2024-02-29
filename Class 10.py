from tkinter import *

def login():
    print(user.get())  #gate() is used for take take value from entry/input box to the program
    print(password.get())

root=Tk()
root.title("Sign Up Form")
root.geometry("540x360")
root.maxsize(1080,720)

Title=Label(text="Sign Up Form", font="arial 18 bold", bg="slateblue",fg="white", padx=20)
Title.pack()


user=Label(text="Input Username")
user.pack()
user=Entry()
user.pack()

password=Label(text="Input Password")
password.pack()
password=Entry()  #Entry() is used for making input box
password.pack()

B1=Button(text="LOG IN", command=login)
B1.pack()


root.mainloop()