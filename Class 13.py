from tkinter import *
root = Tk()
root.title("My Project")

canvas_width=540
canvas_height=360
root.geometry(f"{canvas_width}x{canvas_height}")
root.maxsize(1080,720)

canvas1 = Canvas(root, width=canvas_width, height=canvas_height)
canvas1.pack()

#create line in canvas
canvas1.create_line(0,0, 300,300, fill="Blue")
canvas1.create_line(300,0 ,0,300, fill="Green")

#create rectange in canvas
canvas1.create_rectangle(300,10, 500,300, fill="slateblue")

#create circle in canvas
canvas1.create_oval(350,150, 450,250, fill="tomato")

#create text in canvas

canvas1.create_text(230,150, text="Canvas", font="arial 17 bold",fill="dodgerblue")
root.mainloop()