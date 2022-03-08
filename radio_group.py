import tkinter as tk
class RadioGroup(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)

        self.parent = parent

        label_radio = tk.Label(self,text="What is the dx of this image ?",bg="#4ADEDE",font=("monospace",16))

        label_radio.pack(padx=10,pady=10)

        # value for holding a lable
        self.label_val = tk.IntVar(self,'label_val')

        for i,r in enumerate(("Atopic Dermatitis","Papular Urticaria","Scabies")):
            radio = tk.Radiobutton(self,text=r,fg="#000",variable=self.label_val,value=i,justify=tk.LEFT)
            radio.pack(anchor=tk.W)

        

    def get_val(self):
        try:
            self.label_val.get()
        except tk.TclError:
            return -1
        else:
            return self.label_val.get()

