import tkinter
from tkinter import ttk
from tkinter.messagebox import askokcancel

#quit button messgae
def quit_program():
    if askokcancel("Close","Are you sure you want to close?"):
        window.quit()

window = tkinter.Tk()
window.title("Party Hire")

frame = tkinter.Frame(window)
frame.pack()
frame.config(bg="white")

#adding a frame to my GUI
Customer_info_frame = tkinter.LabelFrame(frame, text="Enter details below",bg="#AA336A",)
Customer_info_frame.grid(row=1, column=0)

#the actual button quit
Close_button = tkinter.Button(frame,text="Close",command=quit)
Close_button.grid(row=0,column=0,sticky="nw")
Close_button.config(bg="#fcd9df")


Full_name_label = tkinter.Label(Customer_info_frame, text="Full Name")
Full_name_label.grid(row=1, column=0)

#Adding colour to lables
Full_name_label.config(bg="#fcd9df")

Full_name_label = tkinter.Label(Customer_info_frame, text="Full Name")
Full_name_label.grid(row=1, column=0)
Full_name_entry = tkinter.Entry(Customer_info_frame)
Full_name_entry.grid(row=2, column=0)
Full_name_label.config(bg="#fcd9df")
Full_name_entry.config(bg="#fcbbd9")


#Receipt Number entry/label
Recipt_Number_label = tkinter.Label(Customer_info_frame, text= "Reciept Number")
Recipt_Number_label.grid(row=1,column=2)
Recipt_Number_entry = tkinter.Entry(Customer_info_frame)
Recipt_Number_entry.grid(row=2,column=2)
Recipt_Number_label.config(bg="#fcd9df")
Recipt_Number_entry.config(bg="#fcbbd9")

#creating a dropbox for all the items available 
Item_hired_label =tkinter.Label(Customer_info_frame,text="Item Hired")
Item_hired_label.grid(row=3,column=0)
Item_hired_combobox = ttk.Combobox(Customer_info_frame,values=["chair","baloon"])
Item_hired_combobox.grid(row=4,column=0)
Item_hired_label.config(bg="#fcd9df")
#Item_hired_combobox.config(bg="#fcbbd9")
#adding colour to the drop box

#adding a spinbox
Qty_items_label = tkinter.Label(Customer_info_frame, text="Qty hired")
Qty_items_label.grid(row=3,column=2)
Qty_items_spinbox = tkinter.Spinbox(Customer_info_frame, from_=1, to=500,bg="#fcd9df")
Qty_items_spinbox.grid(row=4,column=2)
Qty_items_spinbox.config(bg="#fcbbd9")
Qty_items_label.config(bg="#fcd9df")

#adding a add item button
add_item_button = tkinter.Button(frame, text = "Add item")
add_item_button.grid(row=0, column=0)
add_item_button.config(bg="#fcd9df")

#adding a display box
columns = ('Full Name', 'Receipt Number', 'Item hired','Qty')
tree = ttk.Treeview(Customer_info_frame, columns=columns, show="headings")
tree.heading('Full Name', text="Full Name")
tree.heading('Receipt Number', text="Receipt Number")
tree.heading('Item hired', text="Item hired")
tree.heading('Qty', text="Qty")
tree.grid(row=5,column=0,columnspan=3, padx=20,pady=10)



window.config(bg="#FFC0CB")
window.mainloop()
