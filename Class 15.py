from tkinter import *
from PIL import ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text


root=Tk()
root.geometry("1000x800")
root.maxsize(1080,720)
root.title("My Newspaper")

texts=[]
photos=[]
for i in range(0,3):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(text)
        texts.append(every_100(text))

        pic = Image.open(f"{i+1}.jpg")
        photos.append(ImageTk.PhotoImage(pic))




f0 = Frame(root, width=800, height=70)
Label(f0, text="My News", font = "arial 15 bold").pack()
f0.pack()

f1=Frame(root, width= 900, height=200)
Label(f1, text=text[3]).pack()
f1.pack()


root.mainloop()