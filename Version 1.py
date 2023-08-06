import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Party Hire")

frame = tkinter.Frame(window)
frame.pack()

Customer_info_frame = tkinter.LabelFrame(frame, text="Full name")
Customer_info_frame.grid(row=0, column=0)

Full_name_label = tkinter.Label(frame, text="Full Name")
Full_name_label.grid(row=0, column=0)
Recipt_Number_label = tkinter.Label(frame, text= "Recipt Number")
Recipt_Number_label.grid(row=0,column=1)

Full_name_entry = tkinter.Entry(frame)
Recipt_Number_entry = tkinter.Entry(frame)
Full_name_entry.grid(row=1, column=0)
Recipt_Number_entry.grid(row=1,column=1)

window.config(bg="#FFC0CB")
window.mainloop()
