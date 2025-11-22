# Source for Multi-Page function - https://stackoverflow.com/a
# Posted by Bryan Oakley, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-13, License - CC BY-SA 4.0

import tkinter as tk               
from tkinter import font as tkfont  

def parse():
    #recieve input and parse grammar
    return("string")
    pass

def saveTXT():
    #save parsed grammar to text file
    pass

class gramParse(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("Grammar Parser")
        self.geometry("400x300")


        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Grammar Parser!", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        labl = tk.Label(self, text="Enter Sentence for Grammar Parsing:")
        labl.pack(pady=20) 

        # keep a reference to the Entry so we can read it when Submit is pressed
        self.text_widget = tk.Entry(self)
        self.text_widget.pack(padx=10, pady=10)

        # When submit is pressed, read the Entry and update PageOne's label
        def submit_action():
            entered = self.text_widget.get()
            # get PageOne frame and call its setter to update the displayed sentence
            page_one = controller.frames.get("PageOne")
            if page_one is not None and hasattr(page_one, 'set_sentence'):
                page_one.set_sentence(entered)
            controller.show_frame("PageOne")

        submit = tk.Button(self, text="Submit", command=submit_action)
        submit.pack()

        note = tk.Label(self, text="Note: The program returns a list of verbs and nouns in " \
        "accordance with the database. This data may be edited after the list is presented.", wraplength=250)
        note.pack(pady=20)
        note.config(state=tk.DISABLED, disabledforeground="grey")


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        # sentence_label will be updated when Submit is pressed on StartPage
        self.sentence_label = tk.Label(self, text="", font=controller.title_font)
        self.sentence_label.pack(side="top", fill="x", pady=10)

        save = tk.Button(self, text="Save Parse List as Text File", command=saveTXT)
        save.pack()
        home = tk.Button(self, text="Parse Another Sentance", command=lambda: controller.show_frame("StartPage"))
        home.pack()

    def set_sentence(self, text):
        self.sentence_label.config(text=text)


if __name__ == "__main__":
    app = gramParse()
    app.mainloop()
