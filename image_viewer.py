import os
import tkinter as tk
import pandas as pd
from PIL import ImageTk, Image
from radio_group import RadioGroup
from metadata_input import MetaDataInput

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
        
        if self.index != len(self.images):
            self.display()
            
    def display(self):
        self.image_num_label = tk.Label(self,text=f"{self.index + 1} / {len(self.images)}",bg="#E3242B")
        self.image_num_label.pack(padx=2,pady=2)

        self.image_1 = Image.open(self.images[self.index])
        # Resize image
        self.image_1 = self.image_1.resize((640,480))

        self.image_1_tk = ImageTk.PhotoImage(self.image_1.convert('RGB'))

        self.label_image = tk.Label(self,image=self.image_1_tk,bg="#fff")
        self.label_image.pack()

        self.label_image.image = self.image_1_tk
        self.radio_frame = RadioGroup(self)
        self.radio_frame.pack(side=tk.LEFT)

        self.metadata_frame = MetaDataInput(self)
        self.metadata_frame.pack(side=tk.RIGHT)

        self.submit_btn = tk.Button(self,text="Submit Data",fg="#000",justify=tk.LEFT,command=lambda:self.insert_data())
        self.submit_btn.pack(side=tk.BOTTOM)

    def display_images(self):
        if self.index == len(self.images):
            print(self.index)
            self.end_display()
        else:
            self.label_image.pack_forget()
            self.radio_frame.pack_forget()
            self.image_num_label.pack_forget()
            self.metadata_frame.pack_forget()
            self.submit_btn.pack_forget()
        
            self.display()

    def insert_data(self):
        assigned_label = self.radio_frame.get_val()
        supporting_data = self.metadata_frame.get_values()

        if assigned_label != -1:
            print(supporting_data)
            if self.index <= len(self.images):
                self.write_annotations_to_file(assigned_label,supporting_data,self.images[self.index])
                self.index += 1 
                self.write_index_to_file(self.index)    
                self.display_images()
            else:
                self.end_display()


    def write_index_to_file(self,index):
        file_name = "saved_index.txt"

        with open(file_name,"w") as f:
            f.write(str(index))

    def write_annotations_to_file(self,value,support,image):
        file_name = "labels.csv"

         # parameters
        image_id = image.split('/')[-1]
        dx = value
        sex,age,location = support

        """       
         with open(file_name,"a") as f:
            f.write(f"{','.join([image.split('/')[-1],str(value),sex,age,location])}\n")
        """

        if os.path.exists(file_name):
            df = pd.read_csv(file_name)
            data = {"image_id":image_id,"dx":dx,"sex":sex,"age":age,"location":location}
            df = df.append(data,ignore_index=True)
            df.to_csv(file_name,index=False)
        else:
            # create a pandas dataframe
            data = {"image_id":image_id,"dx":dx,"sex":sex,"age":age,"location":location}

            df = pd.DataFrame(columns=("image_id","dx","sex","age","location"))
            df = df.append(data,ignore_index=True)

            df.to_csv(file_name,index=False)


    def end_display(self):
        self.radio_frame.pack_forget()
        self.metadata_frame.pack_forget()
        self.submit_btn.pack_forget()
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