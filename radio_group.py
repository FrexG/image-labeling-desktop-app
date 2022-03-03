import tkinter as tk
class RadioGroup(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)

        self.parent = parent

        label_radio = tk.Label(self,text="What is the dx of this image ?",fg="#4ADEDE",font=("monospace",16))

        label_radio.pack(padx=10,pady=10)

        # value for holding a lable
        self.label_val = tk.IntVar(self,'label_val')

        for i,r in enumerate(("Atopic Dermatitis","Papular Urticaria","Scabies")):
            radio = tk.Radiobutton(self,text=r,fg="#000",variable=self.label_val,value=i,justify=tk.LEFT)
            radio.pack(anchor=tk.W)

        
        submit_btn = tk.Button(self,text="Submit",fg="#000",command=lambda:self.next_images())

        submit_btn.pack()

    def next_images(self):
        #print(self.parent.index)
        label_warning = tk.Label(self,text="Select an answer",fg="#E3242B")
       
        try: 
            self.label_val.get()
        except tk.TclError:
            print("Please select a valid answer") 
            label_warning.pack(padx=10,pady=10)
        else:
            self.updata_image()        
        finally:
         label_warning.pack_forget()

    def updata_image(self):
            self.write_annotations_to_file(self.label_val.get(),self.parent.images[self.parent.index])
            self.write_index_to_file(self.parent.index)
            self.parent.index += 1 
            self.parent.display_images()
    
    def write_index_to_file(self,index):
        file_name = "saved_index.txt"

        with open(file_name,"w") as f:
            f.write(str(index))

    def write_annotations_to_file(self,value,image):
        file_name = "labels.txt"

        with open(file_name,"a") as f:
            f.write(f"{','.join([image.split('/')[-1],str(value)])}\n")