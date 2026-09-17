import tkinter
from PIL import Image, ImageTk
import random

# top-level widget which represents the main window of an application
root = tkinter.Tk()
root.geometry('400x400')
root.title('DataFlair Roll the Dice')

# Adding label into the frame
BlankLine = tkinter.Label(root, text="")
BlankLine.pack()

# adding label with different font and formatting
HeadingLabel = tkinter.Label(root, text="Welcome to Dice Rolling",
   fg = "light green",
     bg = "dark green",
     font = "Helvetica 16 bold italic")
HeadingLabel.pack()

# images
dice = ["D:\\python_programs\\dice_2.png",
        "D:\\python_programs\\dice_3.png",
        "D:\\python_programs\\dice_4.png",
        "D:\\python_programs\\dice_5.png",
        "D:\\python_programs\\dice_6.png",
        "D:\\python_programs\\dice_1.png"]

# simulating the dice with random numbers between 0 to 5 and generating image
DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
ImageLabel = tkinter.Label(root, image=DiceImage)
ImageLabel.image = DiceImage

# packing a widget in the parent widget 
ImageLabel.pack(expand=True)

# function activated by button
def rolling_dice():
    DiceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    ImageLabel.configure(image=DiceImage)
    # keep a reference
    ImageLabel.image = DiceImage

# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)
# pack a widget in the parent widget
button.pack(expand=True)

# call the mainloop of Tk
# keeps window open
root.mainloop()
