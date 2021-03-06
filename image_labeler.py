import tkinter as tk
from tkinter import filedialog
from typing_extensions import IntVar
from image_viewer import ImageViewer

class ImageLabelerApp(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.title(self,"Image Annotator")

        self.project_path = None
        self.PROJECT_OPENED = False
        self.frame = None

        # construct a main container
        self.container = tk.Frame(self)

        self.container.pack(side="top",fill="both",expand=False)

        self.container.grid_rowconfigure(0,weight=1)
        self.container.grid_columnconfigure(0,weight=1)

        #Create a menu bar
        menubar = tk.Menu(self.container)
        filemenu = tk.Menu(menubar,tearoff=0)
        filemenu.add_command(label="Open Project",command=lambda:self.open_new_project())
        filemenu.add_separator()
        filemenu.add_command(label="Quit",command=quit)

        menubar.add_cascade(label="File",menu=filemenu)
        
        tk.Tk.config(self,menu=menubar) 


    def open_new_project(self):
        self.project_path= filedialog.askdirectory(initialdir="/",title="Select folder")

        if self.PROJECT_OPENED:
            self.frame.pack_forget()

        self.PROJECT_OPENED = True
        self.frame = ImageViewer(self.container,self)
        self.frame.pack()
        self.show_frame(self.frame)


        
    def show_frame(self,frame):
        frame.tkraise()

# Main image viewer and controller class

# Anchor path for loading image( issue on macos)
#os.chdir(os.path.abspath((os.path.dirname(__file__))))

        



if __name__ == "__main__":
    app = ImageLabelerApp()
    app.geometry("1024x1024")
    #app.minsize(720,720)
    #app.maxsize(720,720)
    app.mainloop()