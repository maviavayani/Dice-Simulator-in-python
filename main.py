import tkinter as tk
from PIL import Image, ImageTk   #(Python Imaging Library) is used to handle and display images
import random


def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.config(image=image1)
    label1.image=image1

    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.config(image=image2)
    label2.image = image2




win =tk.Tk()
win.geometry("500x350")
win.config(bg="lightblue")
win.title("Dice Simulator")

dice = ["dice-1.png","dice-2.png","dice-3.png","dice-4.png","dice-5.png","dice-6.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))  #ImageTk.PhotoImage is used to convert and display the image in the GUI.
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))  #ImageTk.PhotoImage is used to convert and display the image in the GUI.

label1 = tk.Label(win,image=image1)
label1.image = image1
label1.place(x=40,y=100)

label2 = tk.Label(win,image=image2)
label2.image = image2
label2.place(x=300,y=100)

button = tk.Button(win,text="Dice",bg="Black",fg="white",font=("Arial",19,"bold"),command=dice_roll)
button.place(x=220,y=10)
win.mainloop()