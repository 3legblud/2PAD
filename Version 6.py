import tkinter
from tkinter import ttk
from tkinter.messagebox import askokcancel,showerror,showinfo
# Allows for a random generating to be made(the reeipt number).
import random
# Function to make sure the only letters and space. 
def Name_checker(input_str):
    return all(char.isalpha() or char.isspace() for char in input_str) #isaplha makes it only letters


# Adding a function to make a record appear in the message box. 
def add_item():
    Full_name = Full_name_entry.get()
    # This pulls the data from the entry to be printed in the message box below. 
    Receipt_Number = random.randint(1000,10000)
    # This makes sure the receipt number is randomly generated. 
    Item= Item_hired_combobox.get()
    # This pull the selection from the drop down box.
    qty_str = Qty_items_spinbox.get().strip()
# This is to fix the error so all details have to be entered before you can add the record.
# Checking if any fields are empty 
    if not Full_name or not Item or not qty_str:
        tkinter.messagebox.showerror("Invalid Input","Please fill in all the details before adding a record")
        return

    try:
        # This section is for Quanity, making sure it meets the requirements.
        qty = int(qty_str)
        # Int makes sure only numbers are inputed.
        if qty < 1 or qty > 500:
            raise ValueError
    except ValueError:
        # This is the error message if the users dont input doesnt fit the if and or statements.
        tkinter.messagebox.showerror("Invalid Input", "Please enter a valid quantity (between 1 and 500")# The error message.
        return
    if not Name_checker(Full_name): # This is a error message for the full name entry which looks for.
        tkinter.messagebox.showerror("Invalid Input","Please enter a valid Full name(letter only).") # The error message.
        return
    # This is the list which has all the things which will be printed in my messagebox below the code.
    data_load = [ Full_name,Receipt_Number,Item,qty]
    tree.insert('',0,values= data_load)
    all_records.append(data_load)



# Quit button message
def quit_program(): # This is for the quit button which asks if the user wants to close the program.
    if askokcancel("Close","Are you sure you want to close?"):
        window.quit()


# Adding a delete button to delete records
def delete_records():
    selected_item = tree.selection() # This allows me to make it easy to delete  records just be selecting it.
    if not selected_item: # This is for if the user presses the delete button without a selection being made.
        tkinter.messagebox.showerror("Error", "Please select an record to delete") # The Error message.
        return
    confirmed = askokcancel("Delete record", " Are you want to delete the selected record") # This message pops up after a record is selected and the delete button is pressed.
    if confirmed: # Confirming if they want to delete the record.
         tree.delete(selected_item)

def Search():
    search_text = Search_entry.get().strip()
    if not search_text:
        tkinter.messagebox.showerror("Invalid search","Please enter a Full Name to pull up a record")
        return
    tree.delete(*tree.get_children())

    found_records = []
    for item in all_records:     
        if item[0].lower() == search_text.lower():
            found_records.append(item)
    if not found_records:
        tkinter.messagebox.showinfo("No Record Found" ,f"for '{search_text}'.")
    else:
        for record in found_records:
            tree.insert("",'end', values=record)
        
# Function to pull all records entered after a search
def show_all_records():
    tree.delete(*tree.get_children())
    for record in all_records:
         tree.insert('', 'end', values=record)
        
       

    


# Frame and window creation
window = tkinter.Tk()
window.title("Party Hire") # This is main window where everything will be placed.
window.config(bg="#FFC0CB") # This is the colour for the window in its hex code.

frame = tkinter.Frame(window) # This is the frame which creates a edge around all the buttons. 
frame.pack()
frame.config(bg="white") # This is the colour for the frame.



# Adding the frame to my GUI.
Customer_info_frame = tkinter.LabelFrame(frame, text="Enter details below",bg="#AA336A",)
Customer_info_frame.grid(row=1, column=0) # This position my frame.

# This is a label  which supports the frame.
Full_name_label = tkinter.Label(Customer_info_frame, text="Full Name") 
Full_name_label.grid(row=1, column=0)

# Adding colour to lables.
Full_name_label.config(bg="#fcd9df") # This is for my label and adding to a colour to it.
 # This is for the label which will say Full name, and in the brackets says it will go in the frame we created.
Full_name_label = tkinter.Label(Customer_info_frame, text="Full Name")
Full_name_label.grid(row=1, column=0) # This postions where the label on the Gui.
Full_name_entry = tkinter.Entry(Customer_info_frame)
Full_name_entry.grid(row=2, column=0)
Full_name_label.config(bg="#fcd9df") # Colour for the label.
Full_name_entry.config(bg="#fcbbd9") # Colour for the entry.


# Receipt Number entry/label.
Receipt_Number_label = tkinter.Label(Customer_info_frame, text= "Receipt Number")
Receipt_Number_label.grid(row=1,column=2)
Receipt_Number_entry = tkinter.Entry(Customer_info_frame,state="readonly")
Receipt_Number_entry.grid(row=2,column=2) # This poistion where the entry will be.
Receipt_Number_label.config(bg="#fcd9df") # Colour for the label.
Receipt_Number_entry.config(bg="#fcbbd9") # Colour for the entry.



# Creating a dropbox for all the items available.
# The drop box will have common items which would be for hire.
Item_hired_label =tkinter.Label(Customer_info_frame,text="Item Hired")
Item_hired_label.grid(row=3,column=0)
Item_hired_combobox = ttk.Combobox(Customer_info_frame,values=["chair","baloon"],state="readonly") # This is where i enter what items can be selected.
 # State = readonly means users cannot write thier own input for that and have to use the drop with all items selected in there.
Item_hired_combobox.grid(row=4,column=0)
Item_hired_label.config(bg="#fcd9df") # Colour for the label.
 


# Adding a spinbox for the qty hired.
Qty_items_label = tkinter.Label(Customer_info_frame, text="Qty hired")
Qty_items_label.grid(row=3,column=2)
Qty_items_spinbox = tkinter.Spinbox(Customer_info_frame, from_=1, to=500,bg="#fcd9df") #  This puts a value which the spinbox can go to.
Qty_items_spinbox.grid(row=4,column=2)
Qty_items_spinbox.config(bg="#fcbbd9") # Spin Box colour.
Qty_items_label.config(bg="#fcd9df")  # Colour for the label.

# Adding a add item button.
add_item_button = tkinter.Button(Customer_info_frame, text = "Add item", command = add_item)
add_item_button.grid(row=6, column=0,columnspan=3,sticky = "news", padx=20, pady=5) # The news means the button will spread north,east,west,south on the gui.
add_item_button.config(bg="#fcd9df") # The button colour.

# Adding a display box.
# Tree is for the message box. 
columns = ('Full Name', 'Receipt Number', 'Item hired','Qty') # These are the coloumns for the display box.
tree = ttk.Treeview(Customer_info_frame, columns=columns, show="headings") # This places the display box in the frame.
tree.heading('Full Name', text="Full Name") # This is for the display box headings.
tree.heading('Receipt Number', text="Receipt Number")
tree.heading('Item hired', text="Item hired")
tree.heading('Qty', text="Qty")
tree.grid(row=5,column=0,columnspan=3, padx=20,pady=10) # This is the positions the display box on the Gui.

# The actual button quit.
Close_button = tkinter.Button(frame,text="Close",command=quit)
Close_button.grid(row=0,column=0,sticky="nw", padx=10,pady=2)
Close_button.config(bg="#fcd9df")  # The button colour.


# Position of delete button.
delete_button = tkinter.Button(Customer_info_frame, text="Delete", command=delete_records)
delete_button.grid(row=7, column=0,columnspan=3,sticky="news", padx=20, pady=5)
delete_button.config(bg="#fcd9df") # The button colour.

# Search entries  which allows the user to enter the name of a customer to pull thier record.
Search_entry = tkinter.Entry(frame)
Search_entry.grid(row=0, column=1,padx=5,pady=5)
Search_entry.config(bg="#fcbbd9")

# The actual search button.
Search_button = tkinter.Button(frame,text="Search", command = Search)
Search_button.grid(row=0,column=2,padx=5,pady=5)
Search_button.config(bg="#fcd9df")

# Now adding  a button to bring up all the records after one has searched for a certain record.
All_entries_button = tkinter.Button(frame,text="Bring up all records", command= show_all_records)
All_entries_button.grid(row=0,column=3,padx=5,pady=5)
All_entries_button.config(bg="#fcd9df")

all_records = []
window.mainloop()
