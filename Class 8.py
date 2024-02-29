from tkinter import *
root=Tk()
root.title("My Software")
root.geometry("540x360")

f1= Frame(root, bg="tomato",borderwidth=5, relief=SUNKEN,padx=10)
f1.pack(side=LEFT, fill="y")

l1=Label(f1, text="Hello World",pady=10)
l1.pack( pady=165)

f2= Frame(root, bg="dodgerblue",borderwidth=5, relief=SUNKEN, pady=10)
f2.pack(side=TOP, fill="x")

l2=Label(f2, text="Welcome To Project", font="arial 15 bold",bg="skyblue", fg="white")
l2.pack()

root.mainloop()

