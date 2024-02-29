from tkinter import *
root_window = Tk()

#window size
root_window.geometry("540x360")
root_window.minsize(270,180)
root_window.maxsize(1080,720)

#Add title/lebel in the window
title= Label(text="Hello world")
title.pack() # We must pack the lebel to show

root_window.mainloop()



