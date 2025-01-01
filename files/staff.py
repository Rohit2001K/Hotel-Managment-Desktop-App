import tkinter
from tkinter import *
from tkinter import ttk

class Staff:
    def __init__(self, root, email):
        self.root = root
        self.root.title("R Hotel Staff Dashboard")
        self.root.geometry("500x550")
        
        self.msg = Label(self.root, text=f"Welcome To Staff Dashboard ", font=("", 20))
        self.msg.grid(row=1, column=0,padx=50)

