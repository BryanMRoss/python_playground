# tkinter assignment
from tkinter import *
from time import *

# I draw a picture of at least 5 shapes and one animation. I am going to make
# a rainbow with a setting sun over a grassy field

# make the class that extends Frame
class MyFrame(Frame):
    """this is the class that extends Frame and creates a Canvas to draw."""
    def __init__(self):
        Frame.__init__(self)
        # create the canvas to draw on.
        self.myCanvas = Canvas(width=300, height=200, bg="white")
        self.myCanvas.grid() # set the layout manager

        # use two rectangles to make sky and land
        # draw the sky
        self.myCanvas.create_rectangle(1, 1, 300, 100, fill="skyblue")

        # draw the rainbow. Make the biggest oval first; super-impose
        # smaller ones to creat the illusion of a rainbow, centered in
        # the canvas so half of it will be below the ground
        # NOTE: I could have used create_arc, too.
        self.myCanvas.create_oval(75, 25, 225, 175, fill="red")
        self.myCanvas.create_oval(85, 35, 215, 165, fill="yellow")
        self.myCanvas.create_oval(95, 45, 205, 155, fill="purple")
        self.myCanvas.create_oval(105, 55, 195, 145, fill="pink")
        self.myCanvas.create_oval(115, 65, 185, 135, fill="skyblue")

        # draw the ground on top of rainbow lower half
        self.myCanvas.create_rectangle(1, 100, 300, 200, fill="green")

        # create my sun
        my_sun = self.myCanvas.create_oval(10, 10, 50, 50, fill="orange")

        # move my sun over and down the horizon
        for count in range(10):
            increment = 10 * count
            self.myCanvas.coords(my_sun, 10 + increment, 10 + increment,
                                 50 + increment, 50 + increment)
            # redraw the grass
            self.myCanvas.create_rectangle(1, 100, 300, 200, fill="green")
            self.myCanvas.update()
            sleep(1)

        

frame01 = MyFrame()
frame01.mainloop()
