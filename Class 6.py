from tkinter import *
root_window = Tk()

#window title
root_window.title("My GUI")

#window size
root_window.geometry("540x360")
root_window.minsize(270,180)
root_window.maxsize(1080,720)

#Add title/lebel in the window
title= Label(text="MAGNETIEGHT EU")
title.pack() # We must pack the lebel to show

#Add image in lebel

pic=PhotoImage(file="M logo.png", height=200, width=200) #Jpg not supports normally
titleImage=Label(image=pic)
titleImage.pack()

text = Label(text="Lorem Ipsum is simply dummy text of the printing \n "
                  "and typesetting industry. Lorem Ipsum has been the \n"
                  "industry's standard dummy text ever since",
             bg="dodgerblue", fg="white", padx=10, pady=10, font="arial 10 bold",relief=RIDGE, borderwidth=1)
text.pack()

footer=Label(text="Ready", bg="tomato", fg="white", padx=50, pady=20)
footer.pack(side=BOTTOM, fill=X)
root_window.mainloop()


# Important Label Options
# text - adds the text
# bg - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE