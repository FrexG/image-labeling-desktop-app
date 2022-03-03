import os
import tkinter as tk
from PIL import ImageTk, Image
from radio_group import RadioGroup

class ImageViewer(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.path = controller.project_path 
        # Chango directory to project path
        os.chdir(self.path)

        self.images = self.get_image_list()
        file_name = "saved_index.txt"
        self.index = 0
        if os.path.exists(file_name):
            with open(file_name,"r") as f:
                line_content = f.readline()
                if line_content != "":
                    
                    self.index = int(line_content)

        else:
            with open(file_name,"w") as f:
                f.write("0")
        
        
        self.image_num_label = tk.Label(self,text=f"{self.index + 1} / {len(self.images)}",fg="#E3242B")
        self.image_num_label.pack(padx=2,pady=2)

        self.image_1 = Image.open(self.images[self.index])
        # Resize image
        self.image_1 = self.image_1.resize((640,480))

        self.image_1_tk = ImageTk.PhotoImage(self.image_1.convert('RGB'))

        self.label_image = tk.Label(self,image=self.image_1_tk,bg="#fff")
        self.label_image.pack()

        self.label_image.image = self.image_1_tk
        self.radio_frame = RadioGroup(self)
        self.radio_frame.pack()


    def display_images(self):
        if self.index == len(self.images):
            print(self.index)
            self.end_display()
        else:
            self.label_image.pack_forget()
            self.radio_frame.pack_forget()
            self.image_num_label.pack_forget()
        
            self.image_num_label = tk.Label(self,text=f"{self.index + 1} / {len(self.images)}",fg="#E3242B")
            self.image_num_label.pack(padx=2,pady=2)

            # read the image
            self.image_1 = Image.open(self.images[self.index])
        

        
            # Resize image
            self.image_1 = self.image_1.resize((640,480))

            self.image_1_tk = ImageTk.PhotoImage(self.image_1.convert('RGB'))

            self.label_image = tk.Label(self,image=self.image_1_tk,bg="#fff")
            self.label_image.pack()

            self.label_image.image = self.image_1_tk
            self.radio_frame = RadioGroup(self)
            self.radio_frame.pack()
        
    def end_display(self):
        self.radio_frame.pack_forget()
        tk.Label(self,text="You're all done!",fg="#000",font=("monospace,24")).pack()
        tk.Label(self,text="THANK YOU!!",bg="#E3242B",font=("Verdana",30)).pack()
    

    def get_image_list(self):
        IMAGE_PATH = self.path
        image_list = []

        for dir_path,dir_names,file_names in os.walk(IMAGE_PATH):
            for file in file_names:
                if file.endswith((".jpg",".png",".jpeg")):
                    image_list.append(os.path.join(IMAGE_PATH,file))

        return image_list