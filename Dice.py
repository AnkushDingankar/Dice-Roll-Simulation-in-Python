from tkinter import*
import random
from tkinter import font

root =Tk()
root.geometry("700x450")
root.title("Dice Simulator")

L1= Label(root,font=("times",200))

def roll():
    number =['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    L1.config(text=f'{random.choice(number)}{random.choice(number)}')
    L1.pack()

b1= Button(root,text="Lets Roll...",command=roll)
b1.place(x=320,y=0)

root.mainloop()