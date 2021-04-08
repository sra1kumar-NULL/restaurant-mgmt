import tkinter as tk
from tkinter import Label,Button

class App1:
	def __init__(self,top):
		self.top=top
		top.title("Restaurant Management")
		top.geometry("1028x500")
		top.configure(background="#091833")

root = tk.Tk()
my_gui = App1(root)
root.mainloop()
