from re import I, S
import tkinter as tk
from tkinter import font

class MetaDataInput(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self,parent)
        
        # List box tuples
        sex = ("M","F")
        location = ("Face","Head","Torso","Limbs","Genitals")
        age = ("0-3","4-10","11-18","19 and up")

        sex_var = tk.StringVar(self)
        location_var = tk.StringVar(self)
        age_range_var = tk.StringVar(self)

        # Set default value
        sex_var.set("Select Sex")
        location_var.set("Symptoms occured on the ... ")
        age_range_var.set("Select patients age range")

        """ INSERT WIDGETS"""

        label = tk.Label(self,text="Supporting Data",fg="#000",font=("monospace",16))
        label.pack(padx=10,pady=10)

        sex_option= tk.OptionMenu(self,sex_var,*sex)
        sex_option.config(bg="WHITE",fg="BLACK")
        sex_option.pack(anchor=tk.W,pady=5)

        age_option = tk.OptionMenu(self,age_range_var,*age)
        age_option.config(bg="WHITE",fg="BLACK")
        age_option.pack(anchor=tk.W,pady=5)


        location_option= tk.OptionMenu(self,location_var,*location)
        location_option.config(bg="WHITE",fg="BLACK")

        location_option.pack(anchor=tk.W,pady=5)
