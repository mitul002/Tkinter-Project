from tkinter import *

def hello():
    print("Hello World")

def sum():

    a = int(input())
    b = int(input())
    print(a+b)
def sub():

    a = int(input())
    b = int(input())
    print(a-b)

def mul():
    while True:
        a = int(input())
        b = int(input())
        print(a*b)

def div():
    while True:
        a = int(input())
        b = int(input())
        print(a/b)

root=Tk()
root.title("My Software")
root.geometry("540x360")
root.maxsize(1080,720)

Title=Label(text="WELCOME TO MY SOFTWARE", fg="dodgerblue", font= "arial 15 bold",pady=15)
Title.pack()

F1=Frame( pady=10, borderwidth=10, relief=SUNKEN)
F1.pack(side=LEFT, fill=Y)

B1=Button(F1, text="CLICK HERE",padx=10, pady=15, command=hello)
B1.pack()
B2=Button(F1, text="SUM OF NO.",padx=10, pady=15, command=sum)
B2.pack()
B3=Button(F1, text="SUB OF NO.",padx=10, pady=15, command=sub)
B3.pack()
B4=Button(F1, text="MUL OF NO.",padx=10, pady=15, command=mul)
B4.pack()
B5=Button(F1, text="DIV OF NO.",padx=10, pady=15, command=div)
B5.pack()


root.mainloop()

