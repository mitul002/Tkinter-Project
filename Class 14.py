from tkinter import *
def clicked_location(event):
    print(f"You clicked the button at: {event.x}, {event.y}")


root=Tk()
root.title("click anywhere")
root.geometry("540x360")

widget=Button(root, text="Click me")
widget.pack()

text=Label(text="Signle click will show the clicking location on IDE output menu. \n"
                " Double click on the button to Exit")
text.pack()
#tkinter events
widget.bind('<Button-1>',clicked_location)
widget.bind('<Double-1>',quit)

root.mainloop()