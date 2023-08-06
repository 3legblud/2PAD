# Party hire, version 7: Raihan Mohammed
import tkinter
from tkinter import ttk
from tkinter.messagebox import askokcancel,showerror,showinfo

# Allows for a message box to be displayed.
# Shows error and bring a error box.

import random # Allows for a random generating to be made(the reeipt number).

# Constant things in my code.
ITEMS_FOR_HIRE = ["Chair","Balloon","Table's","Party Hat's"] # All the items  that people can hire at the party hire store in a list.
LABEL_COLOUR = '#fcd9df' # Colour for all my labels.


# Function to make sure the only letters and space.
def name_checker(input_str): # Function check the full name entries so only spaces and letters.
    # Function to make sure only letters and spaces are allowed for the Full name entry.
    return all(char.isalpha() or char.isspace() for char in input_str) #is.alpha and isspace allows for only letters and spaces.


# Adding a function to make a record appear in the message box. 
def add_item(): # Adding a new record.
    full_name = Full_name_entry.get()
    # This pulls the data from the entry to be printed in the message box below. 
    receipt_Number = random.randint(1000,10000)
    # This makes sure the receipt number is randomly generated. 
    item= Item_hired_combobox.get()
    # This pull the selection from the drop down box.
    qty_str = Qty_items_spinbox.get().strip()
# This is to fix the error so all details have to be entered before you can add the record.
# Checking if any fields are empty. 
    if not full_name or not item or not qty_str:
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
    if not name_checker(full_name): # This is a error message for the full name entry which looks for.
        tkinter.messagebox.showerror("Invalid Input","Please enter a valid Full name(letter only).") # The error message.
        return
    # This is the list which has all the things which will be printed in my messagebox below the code.
    data_load = [ full_name,receipt_Number,item,qty] # This is a list which hold all the values which get entered.
    tree.insert('',0,values= data_load)
    all_records.append(data_load) # This if for show all entries button.

    # These lines will reset the entries,drop downn box, spinbox after a record has been addded.
    Full_name_entry.delete(0,tkinter.END) # Resets the full name entry box.
    Item_hired_combobox.set('') # Resets the dropdown box.
    Qty_items_spinbox.delete(0, tkinter.END) # Resets the spinbox.
    

    showinfo("Success" , "Record added successfully") # This message pops after a records goes through letting the user know the record got entered successfully.



# Quit button message
def quit_program(): # This is for the quit button which asks if the user wants to close the program.
    if askokcancel("Close","Are you sure you want to close?"): # This pops up after pressing the quit button to make sure no accidental closes happen.
        window.quit()



def delete_records(): # Function for deleteing records selected in the message box.
    selected_items = tree.selection()  # This allows me to make it easy to delete records just by selecting them.

    if not selected_items: # These if no statements check if no records are being selected when the button is pressed.
        tkinter.messagebox.showerror("Error", "Please select a record to delete") # If there is no record being selected and the button is pressed this error message will pop up.
        return

    if len(selected_items) > 1: # This is so only one record can be deleted a time not multiple. The len counts the how much records are being selected when the button is pressed.
        tkinter.messagebox.showerror("Error", "Please select one record at a time to delete") # This errro message pops up when more than one record is trying to be deleted at once.
        return

    confirmed = askokcancel("Delete record", "Are you sure you want to delete the selected record?") # This confirms with the user to see if they really want to delete the record.
    if confirmed: # If yes is pressed the code will continue and delete the selected record.
        tree.delete(selected_items) # This means to delete the selected record in the display box.

def search_for_records(): # Function for searching up records using the search entry.
    search_text = Search_entry.get().strip() # This pulls the what was written in the search entry(Name).
    if not search_text: # This is for if nothing was written in the entry and the function was being called.
        tkinter.messagebox.showerror("Invalid search","Please enter a Full Name to pull up a record") # This is a error message if no name is entered and the button is used.
        return
    tree.delete(*tree.get_children()) # This deletes all the records which where entered before a search is made to clear not wanted records based on the search.

    found_records = [] # Empty list to store record which were searched for.
    for item in all_records:    # Checks for a record which matches what was searched for.  
        if item[0].lower() == search_text.lower(): # Checks if the entry is in upper or lower and matches it.
            found_records.append(item)
    if not found_records: # This is for no record was matched to the entry.
        tkinter.messagebox.showinfo("No Record", f"Found for '{search_text}'.") # This is a message if no record is found by the entered name.
    else:  # If records were found this will insert the one or many records which matched.
        for record in found_records:
            tree.insert("",'end', values=record) # Inserting found records from the name.
        

def show_all_records(): # Function to pull all records entered after a search has been done.
    tree.delete(*tree.get_children()) # This code deletes the records being displayed(after a search).
    for record in all_records:
         tree.insert('', 'end', values=record) # This is inserts all the records back in the display box.



def print_hirees():  # Function to print all full names on records in a message box, also detects if no records have been added then popping a message saying no records added.     
    if not all_records:
        showinfo("No Records", " No records added.") # If no records have been added this message will pop up.
    else:
        full_names = "\n".join(record[0] for record in all_records) # This collects all the full names from the record and join them. 
        showinfo("All Hiree's",full_names.title()) # .title() tells the code tha, when printing thge full names the first letter will be in capital.

    


# Frame and window creation.
window = tkinter.Tk()
window.title("Party Hire") # This is main window where everything will be placed.
window.config(bg="#FFC0CB") # This is the colour for the window in its hex code.

frame = tkinter.Frame(window) # This is the frame which creates a edge around all the buttons. 
frame.pack()
frame.config(bg="white") # This is the colour for the frame.



# Adding the frame to my GUI.
Customer_info_frame = tkinter.LabelFrame(frame, text="Enter Details Below",bg="#AA336A") # This adds the frame to the GUI and gives it a heading and a colour.
Customer_info_frame.grid(row=1, column=0) # This position the  frame.






# This is for the label which will say Full name, and in the brackets says it will go in the frame we created.
Full_name_label = tkinter.Label(Customer_info_frame, text="Full Name") # Creating the label with a text and placing it the frame.
Full_name_label.grid(row=1, column=0) # This postions where the label on the Gui.
Full_name_entry = tkinter.Entry(Customer_info_frame) # This creates and tells the code that the entry will be in the frame.
Full_name_entry.grid(row=2, column=0) # This position the entry in the frame.
Full_name_label.config(bg=LABEL_COLOUR) # Colour for the label.
Full_name_entry.config(bg="#fcbbd9") # Colour for the entry.
# Hex colour code.

# Receipt Number entry/label.
Receipt_Number_label = tkinter.Label(Customer_info_frame, text= "Receipt Number") # Creating the label with a text and placing it the frame.
Receipt_Number_label.grid(row=1,column=2) # This postions where the label on the Gui.
Receipt_Number_entry = tkinter.Entry(Customer_info_frame,state="readonly") # This position the entry in the frame.
# State readonly means that a user cant enter anything into that detail since it will be genreated for them.
Receipt_Number_entry.grid(row=2,column=2) # This poistion where the entry will be.
Receipt_Number_label.config(bg=LABEL_COLOUR) # Colour for the label.
Receipt_Number_entry.config(bg="#fcbbd9") # Colour for the entry.
# Hex colour code.


# Creating a dropbox for all the items available.
# The drop box will have common items which would be for hire.
Item_hired_label =tkinter.Label(Customer_info_frame,text="Item Hired")  # Creating the label with a text and placing it the frame.
Item_hired_label.grid(row=3,column=0)  # This position the entry in the frame.
Item_hired_combobox = ttk.Combobox(Customer_info_frame,values= ITEMS_FOR_HIRE,state="readonly") # This is where i enter what items can be selected.
 # State = readonly means users cannot write thier own input for that and have to use the drop with all items selected in there.
Item_hired_combobox.grid(row=4,column=0) # Positioning the drop box in the frame.
Item_hired_label.config(bg=LABEL_COLOUR) # Colour for the label. # Using hex code. 
 # Hex colour code.


# Adding a spinbox for the qty hired.
Qty_items_label = tkinter.Label(Customer_info_frame, text="Qty Hired")  # Creating the label with a text and placing it the frame.
Qty_items_label.grid(row=3,column=2)  # This position the entry in the frame.
Qty_items_spinbox = tkinter.Spinbox(Customer_info_frame, from_=1, to=500,bg="#fcd9df") #  This puts a value which the spinbox can go from and to.
Qty_items_spinbox.grid(row=4,column=2) # Position of the spin box.
Qty_items_spinbox.config(bg="#fcbbd9") # Spin Box colour.
Qty_items_label.config(bg=LABEL_COLOUR)  # Colour for the label.
# Hex colour code.

# Adding a add item button.
add_item_button = tkinter.Button(Customer_info_frame, text = "Add Item", command = add_item) # This means that button will be placed in the frame and use the function add_item.
add_item_button.grid(row=6, column=0,columnspan=3,sticky = "news", padx=20, pady=5) # The news means the button will spread north,east,west,south on the gui.
add_item_button.config(bg="#fcd9df") # The button colour.

# Adding a display box.
# Tree is for the message box. 
columns = ('Full Name', 'Receipt Number', 'Item hired','Qty') # These are the coloumns for the display box.
tree = ttk.Treeview(Customer_info_frame, columns=columns, show="headings") # This places the display box in the frame.
tree.heading('Full Name', text="Full Name") # This is for the display box headings.
tree.heading('Receipt Number', text="Receipt Number") # This is for the display box headings.
tree.heading('Item hired', text="Item Hired") # This is for the display box headings.
tree.heading('Qty', text="Qty") # This is for the display box headings.
tree.grid(row=5,column=0,columnspan=3, padx=20,pady=10) # This is the positions the display box on the Gui.

# The actual button quit.
Close_button = tkinter.Button(frame,text="Close",command=quit) # This positons the close button outside the frame and gives it the command to quit.
Close_button.grid(row=0,column=0,sticky="nw", padx=10,pady=2) # The position of the button outside the frame.
Close_button.config(bg="red")  # The button colour.
# Hex colour code.

# Position of delete button.
delete_button = tkinter.Button(Customer_info_frame, text="Delete", command=delete_records) # This is for the delete button,telling it to be in the frame and have the text delete on it.
# Also giving the function of delete_record.
delete_button.grid(row=7, column=0,columnspan=3,sticky="news", padx=20, pady=5) 
delete_button.config(bg="#fcd9df") # The button colour.
# Hex colour code.

# Search entries  which allows the user to enter the name of a customer to pull thier record.
Search_entry = tkinter.Entry(frame) # Where the search entry is.
Search_entry.grid(row=0, column=1,padx=5,pady=5) # Positon the the entry.
Search_entry.config(bg="#fcbbd9") # The colour of the search entry.
# Hex colour code.

# The actual search button.
Search_button = tkinter.Button(frame,text="Search(Full Name)", command = search_for_records) # This for the search button and says its commaned is the Search function.
Search_button.grid(row=0,column=2,padx=5,pady=5)  #Position of the button.
Search_button.config(bg="lime") # The colour of the search button.
# Hex colour code.

# Now adding  a button to bring up all the records after one has searched for a certain record.
All_entries_button = tkinter.Button(frame,text="Bring Up All Records", command= show_all_records) # Positions the all entries button and gives it command.
All_entries_button.grid(row=0,column=3,padx=5,pady=5) # Positon of the button outside the frame.
All_entries_button.config(bg="#fcd9df") # The colour of the button.
# Hex colour code.

# Adding a menu function which prints all the records displayed.
# Creating  the acctual  menu bar on GUI.
menu_bar = tkinter.Menu(window)
window.config(menu=menu_bar)
 # Creating a inspect menu bar.
file_menu = tkinter.Menu(menu_bar , tearoff=0)
menu_bar.add_cascade(label="Inspect", menu=file_menu)

file_menu.add_command(label=" Print All Hiree's", command= print_hirees) # Adding the  function to the menu. 



all_records = [] # Empty list.
window.mainloop()
