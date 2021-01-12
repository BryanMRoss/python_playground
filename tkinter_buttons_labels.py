# tkinter_buttons_labels
from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("400x300")
        self.master.title("My GUI")
        self.grid()

        # text label on top
        self.label_text = StringVar()
        self.label_text.set("Hello there.")
        self.message = Label(self, textvariable=self.label_text,
                             font="Courier 14")
        self.message.grid(columnspan=2, pady=10)

        # label followed by text entry box
        self.name_prompt = Label(self, text="What is your name?")
        self.name_prompt.grid(row=1, column=0, padx=3)
        self.input_name = Entry(self)
        self.input_name.grid(row=1, column=1, pady=10)

        # a button to click in the next row down
        self.button_click_here = Button (self, text="Click Here",
                                         command=self.click_here_click)
        self.button_click_here.grid(columnspan=2, pady=5)

        # option to mess with the font option/attribute of the Label
        # use a checkbox to choose bold or underline or both
        self.check_message = Label(self, text="Choose how to change the text")
        self.check_message.grid(columnspan=2)
        self.bold_on = IntVar()   # int to register if checked or not
        self.underline_on = IntVar()
        self.check_bold = Checkbutton(self, text="Bold", variable=self.bold_on,
                                      command=self.change_font)
        self.check_bold.grid(row=4, column=0)
        self.check_underline = Checkbutton(self, text="Underline",
                                           variable=self.underline_on,
                                           command=self.change_font)
        self.check_underline.grid(row=4, column=1, pady=5)

        # option to mess with the font size, using radiobuttons
        self.point_size = StringVar()
        self.point_size.set("14")  # this is the font size I defaulted with
        # the Radiobutton with value 14 will show up pre-picked.
        # radio buttons label
        self.radio_message = Label(self, text="Pick a font size")
        self.radio_message.grid(columnspan=2)
        # the radiobuttons
        self.r_14 = Radiobutton(self, text="14", value="14",
                                variable=self.point_size,
                                command=self.change_font)
        self.r_18 = Radiobutton(self, text="18", value="18",
                                variable=self.point_size,
                                command=self.change_font)
        self.r_14.grid(row=6, column=0)
        self.r_18.grid(row=6, column=1)

    def change_font(self):
        """make bold and/or underline"""
        label_font = "Courier"
        # first, check on the font size
        font_size = self.point_size.get()
        label_font = label_font + " " + font_size
        # check to see if I have checked any boxes
        if self.bold_on.get() == 1:
             label_font = label_font + " bold"
        if self.underline_on.get() == 1:
            label_font = label_font + " underline"
        self.message.config (font = label_font)
            

    def click_here_click(self):
        """this is executed when the button gets clicked."""
        self.label_text.set(self.input_name.get() + ", You did it!!!")
        #print (dir(self.label_text))

frame01 = MyFrame()
#print ("WHOA")
#print ("DIR:", dir (frame01))
#print ("AFTER DIR")
frame01.mainloop()

# more information about Tkinter
# https://effbot.org/tkinterbook/
