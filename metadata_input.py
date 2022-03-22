from re import I, S
import tkinter as tk
from tkinter import W, font

from matplotlib.pyplot import text

class MetaDataInput(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        
        # List box tuples
        sex = ("M","F")
        age = ("0-3","4-10","11-18","19 and up")

        yes_no = ("YES","NO")

        self.sex_var = tk.StringVar(self)
        self.location_var = tk.StringVar(self)
        self.age_range_var = tk.StringVar(self)
        self.family_hist_var = tk.StringVar(self)
        self.family_mem_itch_var = tk.StringVar(self)
        self.itch_worsens_var = tk.StringVar(self)

        """ INSERT WIDGETS"""

        label = tk.Label(self,text="Supporting Data",fg="#000",font=("monospace",16))
        label.grid(row=0,column=0,pady=10,sticky=tk.EW)

        age_label = tk.Label(self,text="Age (Years) :",fg="#000")
        age_label.grid(row=1,column=0,padx = 5,sticky=tk.W)
        age_option = tk.Entry(self,textvariable=self.age_range_var)
        age_option.config(bg="WHITE",fg="BLACK")
        age_option.grid(row=2,column=0,padx = 5,sticky=tk.W)
        
        sex_label = tk.Label(self,text="Sex: ",fg="#000")
        sex_label.grid(row=3,column=0,padx = 5,sticky=tk.W)
        sex_option= tk.OptionMenu(self,self.sex_var,*sex)
        sex_option.config(bg="WHITE",fg="BLACK")
        sex_option.grid(row=4,column=0,padx = 5,sticky=tk.W)


        location_label = tk.Label(self,text="Symptom location: ",fg="#000")
        location_label.grid(row=5,column=0,padx = 5,sticky=tk.W)
        location_option = tk.Entry(self,textvariable=self.location_var)
        location_option.config(bg="WHITE",fg="BLACK")
        location_option.grid(row=6,column=0,padx = 5,sticky=tk.W)

        family_hist_label = tk.Label(self,text="Family History of AAR: ",fg="#000")
        family_hist_label.grid(row=1,column=1,padx = 5,sticky=tk.W)
        family_hist_option = tk.OptionMenu(self,self.family_hist_var,*yes_no)
        family_hist_option.config(bg="WHITE",fg="BLACK")
        family_hist_option.grid(row=2,column=1,padx = 5,sticky=tk.W)

        family_mem_itchy_label = tk.Label(self,text = "Family Member with Itchy Skin: ",fg="#000")
        family_mem_itchy_label.grid(row=3,column=1,padx = 5,sticky=tk.W)
        family_mem_itchy_option = tk.OptionMenu(self,self.family_mem_itch_var,*yes_no)
        family_mem_itchy_option.config(bg="WHITE",fg="BLACK")
        family_mem_itchy_option.grid(row=4,column=1,padx = 5,sticky=tk.W)

        itch_worsens_label = tk.Label(self,text = "Itch Worsens at Night: ",fg="#000")
        itch_worsens_label.grid(row=5,column=1,sticky=tk.W)
        itch_worsens_option = tk.OptionMenu(self,self.itch_worsens_var,*yes_no)
        itch_worsens_option.config(bg="WHITE",fg="BLACK")
        itch_worsens_option.grid(row=6,column=1,padx = 5,sticky=tk.W)

        """  
        location_option= tk.OptionMenu(self,self.location_var,*location)
        location_option.config(bg="WHITE",fg="BLACK")
        location_option.grid(row=6,column=0,sticky=tk.W)
        """

    def get_values(self):
        sex = self.sex_var.get()
        age_range = self.age_range_var.get()
        family_hist = self.family_hist_var.get()
        family_mem_itchy = self.family_mem_itch_var.get()
        itch_worsens = self.itch_worsens_var.get()
        location = self.location_var.get()

        return (sex,age_range,family_hist,family_mem_itchy,itch_worsens,location)
