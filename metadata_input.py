from re import I, S
import tkinter as tk
from tkinter import W, font

from matplotlib.pyplot import text

class MetaDataInput(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        
        # List box tuples
        sex = ("M","F")
        location = ("Face","Head","Torso","Limbs","Genitals")
        age = ("0-3","4-10","11-18","19 and up")

        self.sex_var = tk.StringVar(self)
        self.location_var = tk.StringVar(self)
        self.age_range_var = tk.StringVar(self)

        """ INSERT WIDGETS"""

        label = tk.Label(self,text="Supporting Data",fg="#000",font=("monospace",16))
        label.grid(row=0,column=1,pady=10,sticky=tk.EW)

        sex_label = tk.Label(self,text="Sex: ",fg="#000")
        sex_label.grid(row=2,column=0,sticky=tk.W)
        sex_option= tk.OptionMenu(self,self.sex_var,*sex)
        sex_option.config(bg="WHITE",fg="BLACK")
        sex_option.grid(row=2,column=1,sticky=tk.W)

        age_label = tk.Label(self,text="Age :",fg="#000")
        age_label.grid(row=4,column=0,sticky=tk.W)
        age_option = tk.OptionMenu(self,self.age_range_var,*age)
        age_option.config(bg="WHITE",fg="BLACK")
        age_option.grid(row=4,column=1,sticky=tk.W)

        location_label = tk.Label(self,text="Symptom location: ",fg="#000")
        location_label.grid(row=6,column=0,sticky=tk.W)
        location_option= tk.OptionMenu(self,self.location_var,*location)
        location_option.config(bg="WHITE",fg="BLACK")
        location_option.grid(row=6,column=1,sticky=tk.W)

    def get_values(self):
        sex = self.sex_var.get()
        age_range = self.age_range_var.get()
        location = self.location_var.get()

        return (sex,age_range,location)
