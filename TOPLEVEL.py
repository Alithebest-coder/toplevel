from tkinter import*
from PIL import Image,ImageTk

root=Tk()
root.geometry("400x300")
root.title("main")

lable=Label(root,text="this is a main root window")
lable.pack()

upload=Image.open("cute.jpg")
image=ImageTk.PhotoImage(upload)
lable3=Label(root ,image=image,bg="white")
lable3.pack()
def top():
    TW=Toplevel()
    TW.geometry("180x100")
    TW.title("top level window")
    label1=Label(TW,text="this is a top level label")
    label1.pack()
    TW.mainloop

butt=Button(root,text="presss meeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", command=top)
butt.pack()

root.mainloop()