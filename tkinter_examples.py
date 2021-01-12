# tkinter examples

from tkinter import *
from time import *
# this class is given the Frame class in its instantiation. This
# allows me to create a class that inherits from Frame.

# a simple frame would be frame01 = Frame()
# and call mainloop to listen for events, like
# frame01.mainloop()

# some basics about Frames, Tk object, etc.:
# https://python-tricks.com/frames-in-tkinter/

#NOTE: arguments in functions are also called options in Python

class MyFrame(Frame):
    """this is my sample class. Uncomment stuff to try it."""
    def __init__(self):
        Frame.__init__(self)  # call the standard init from Frame class
        self.myCanvas = Canvas(width=300, height=200, bg="white")
        self.myCanvas.grid()
        
        #self.myCanvas.create_rectangle(10, 10, 50, 50)
        
        #self.myCanvas.create_oval(10, 10, 200, 100, fill="white")
        #self.myCanvas.create_line(1, 1, 200, 200, arrow="first")
        #self.myCanvas.create_text(20, 20, text="Hello World", width=70,
        #                          fill="blue", anchor="nw", justify="center",
        #                          font=("Times", 16))
        
        #self.myCanvas.create_text(20, 20, text="X", fill="red")
        #self.myCanvas.update()  # display what have so far...

        #sleep(1)  # the time function to pause

        #self.myCanvas.create_rectangle(20, 20, 60, 60)

        # this draws a series of rectangles down & across the canvas
        #for count in range(10):
        #    increment = 10 * count
        #    self.myCanvas.create_rectangle(10 + increment,
        #                                   10 + increment,
        #                                   50 + increment,
        #                                   50 + increment)
        #    self.myCanvas.update()
        #    sleep(1)

        # this moves a singe rectangle down & across the canvas
        my_rect_id = self.myCanvas.create_rectangle(10, 10, 50, 50)
        self.myCanvas.update()
        for count in range(10):
            increment = 10 * count
            # keep changing coordinates of the rect in the canvas
            self.myCanvas.coords(my_rect_id, 10 + increment,
                                 10 + increment,
                                 50 + increment,
                                 50 + increment)
            self.myCanvas.update()
            sleep(1)
        
            


frame02 = MyFrame()
frame02.mainloop()
        
# reference page for Canvas methods http://effbot.org/tkinterbook/canvas.htm
