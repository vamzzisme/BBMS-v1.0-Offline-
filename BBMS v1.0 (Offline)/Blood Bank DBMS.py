
#* IMPORTS
from tkinter import *
from tkinter import Toplevel, messagebox, ttk
from tkinter.filedialog import asksaveasfile, askopenfile
from tkcalendar import DateEntry
import time
import re
import sqlite3 as sql

#* GLOBALS
ROOT_BG = "#fff8cd"

#* TKINTER INITIALISATION
root = Tk()
root.title("Blood Bank Management System")
root.config(bg = ROOT_BG)
root.geometry("1500x750+0+0")
root.resizable(False, False)
root.iconbitmap(r'Blood Bank Management System\Assets\Icons\Report.ico')

#* CREDENTIALS
USERNAME = "vamshee@dbms.com"
PASSWORD = "DBMS123"

#* FONTS
#Roboto
#Bebas Neue
#Lemon Milk
#Trebuchet MS

#* IMAGES
connectdb_img  = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Login_btn.png")
submit_img     = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Add_btn.png")
save_img       = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Save_btn.png")
delete_img     = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Delete_btn.png")
clear_img      = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Clear_btn.png")
find_img       = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Find_btn.png")
update_img     = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Update_btn.png")
admin_img      = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\V.png")
export_img     = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Export_btn.png")
exitdb_img     = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Turn_off.png")
help_img       = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Help_btn.png")
back_img       = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Back_btn.png")
credit_img     = PhotoImage(file = r"Blood Bank Management System\Assets\Backgrounds\Credits.png")
new_record_img = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Add_new.png")
loginbtn_img   = PhotoImage(file = r"Blood Bank Management System\Assets\Buttons\Signin_btn.png")
login_bg       = PhotoImage(file = r"Blood Bank Management System\Assets\Backgrounds\Login_BG.png")
username_icon  = PhotoImage(file = r"Blood Bank Management System\Assets\Backgrounds\Username_icon.png")
password_icon  = PhotoImage(file = r"Blood Bank Management System\Assets\Backgrounds\Password_icon.png")

# Class for generating tooltips for tk widgets
class CreateToolTip(object):
    '''
    create a tooltip for a given widget in normal state
    '''
    def __init__(self, widget, text = "widget info"):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)

    def enter(self, event = None):
        self.label = Label(root, text = self.text, justify = 'left', background = 'white', relief = 'solid', borderwidth = 1, font = ("Roboto", 8))
        self.label.place(x = 7, y = 640) # y = 720

    def close(self, event = None):
        self.label.destroy()

# Date and Time display function
def date_and_time():
    time_str = time.strftime("%H:%M")
    date_str = time.strftime("%d|%m|%Y")
    Clock_label.config(text = time_str + "\n" + date_str, fg = ROOT_BG)
    Clock_label.after(200, date_and_time)

int_regex = '[+-]?[0-9][0-9]*'
def check_int(int):
    if(re.search(int_regex,int)):
        return True
    else:
        return False

email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'
def check_email(email):
    if(re.search(email_regex,email)):
        return True
    else:
        return False

phone_regex = '^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'
def check_phone(phone):
    if (re.search(phone_regex, phone)):
        return True
    else:
        return False

pincode_regex = '^[1-9][0-9]{5}$'
def check_pincode(pincode):
    if (re.search(pincode_regex, pincode)):
        return True
    else:
        return False

# Creating query function for database
def show_donations():
    pass

# Creating update function for database
def update_donation():
    update_confirm = messagebox.askquestion(title = "Update Re-Confirmation", message = "Are you sure want to update the modified information?")
    if update_confirm == 'yes':
        clear_entered()
        messagebox.showinfo(title = "Update Successful", message = "Successfully updated the donation")
        save_record.config(state = DISABLED)
        submit_record.config(state = NORMAL)
        delete_record.config(state = DISABLED)
        donater_input.config(state = NORMAL)
        phone_input.config(state = NORMAL)
        email_input.config(state = NORMAL)
        dob_input.config(state = NORMAL)
        gender_input.config(state = NORMAL)
        bloodgrp_input.config(state = NORMAL)
        amount_input.config(state = NORMAL)
        address_input.config(state = NORMAL)
        city_input.config(state = NORMAL)
        state_input.config(state = NORMAL)
        pincode_input.config(state = NORMAL)
        tabcontrol.select(tab_view)
    else:
        default_settings()
        tabcontrol.select(tab_view) 

# Creating delete function for database
def delete_donation():
    delete_confirm = messagebox.askquestion(title = "Delete Re-Confirmation", message = "Are you sure want to delete this donation?")
    if delete_confirm == 'yes':
        clear_entered()
        messagebox.showinfo(title = "Delete Successful", message = "Successfully deleted the donation")
        save_record.config(state = DISABLED)
        submit_record.config(state = NORMAL)
        delete_record.config(state = DISABLED)
        donater_input.config(state = NORMAL)
        phone_input.config(state = NORMAL)
        email_input.config(state = NORMAL)
        dob_input.config(state = NORMAL)
        gender_input.config(state = NORMAL)
        bloodgrp_input.config(state = NORMAL)
        amount_input.config(state = NORMAL)
        address_input.config(state = NORMAL)
        city_input.config(state = NORMAL)
        state_input.config(state = NORMAL)
        pincode_input.config(state = NORMAL)
        tabcontrol.select(tab_view)
    else:
        default_settings()
        tabcontrol.select(tab_view)        

# Creating export function for database
def export_donation():
    files = [('Database File', '*.db'),  
             ('Python File', '*.py'), 
             ('Text Document', '*.txt')] 
    file = asksaveasfile(filetypes = files, defaultextension = files)
    export_btn.config(command = lambda : export_donation())

# Function to Exit management system 
def exit_MS():
    confirm = messagebox.askyesnocancel('Exit Confirmation', 'Do you want to EXIT?')
    if confirm == True:
        root.destroy()

# Creating add function for database
def add_record():
    required_count  = 0
    all_validations = 0

    validate_list = [donater_input.get(), dob_value.get(), phone_input.get(), email_input.get(), dob_value.get(), gender_input.get(), bloodgrp_input.get(), amount_input.get(), address_input.get(), city_input.get(), state_input.get(), pincode_input.get()]

    for item in validate_list:
        if len(item) != 0:
            required_count += 1
        else:
            required_count += 0

    if check_phone(phone_input.get()):
        all_validations =+ 1
    else:
        messagebox.showwarning(title = "Warning", message = "Invalid Mobile number entered")

    if check_email(email_input.get()):
        all_validations += 1
    else:
        messagebox.showwarning(title = "Warning", message = "Invalid E-Mail address entered")

    if check_int(amount_input.get()):
        all_validations += 1
    else:
        messagebox.showwarning(title = "Warning", message = "Amount donated must be an integer")

    if check_pincode(pincode_input.get()):
        all_validations += 1
    else:
        messagebox.showwarning(title = "Warning", message = "Invalid Pincode entered")

    if required_count == 12:
        if all_validations == 4:
            submission_confirm = messagebox.askquestion(title = "Submission Confirmation", message = "Are you sure want to add this donation?")
            if submission_confirm == 'yes':
                clear_entered()
                messagebox.showinfo(title = "Submission Successful", message = "Successfully added the donation")
    else:
        messagebox.showwarning(title = "Warning", message = "All fields are required")

# Creating search function for database
def find_data():
    find_opt_box.get()
    find_input.get()

    if len(find_input.get()) == 0:
        messagebox.showwarning(title = "Search Warning", message = "Search field should not be empty")
        find_opt_box.delete(0, END)
        find_input.delete(0, END)

# Login function for connecting to a database
def admin_connectDB():
    login_root = Toplevel()
    login_root.grab_set()
    login_root.title("Login")
    login_root.config(bg = "#e7dec8")
    login_root.geometry("503x570+499+90")
    login_root.resizable(False, False)
    login_root.iconbitmap(r'Blood Bank Management System\Assets\Icons\Login.ico')

    #* LOGIN GLOBALS
    LOGIN_BG = "#ffffff"
    LOGIN_LABEL_FG = "#03c4a1"
    LOGIN_LABEL_BG = "#e8e8e8"

    login_bg_label =  Label(login_root, image = login_bg, bg = LOGIN_BG)
    login_bg_label.place(x = 0, y = 0)

    username_value = StringVar(root, "vamshee@dbms.com")
    password_value = StringVar(root, "DBMS123")

    username_icon_label =  Label(login_root, image = username_icon, bg = LOGIN_BG)
    username_icon_label.place(x = 10, y = 268)
    username = Label(login_root, text = "Username :", font = ('Roboto Light', 13), fg = LOGIN_LABEL_FG, bg = LOGIN_LABEL_BG)
    username.place(x = 10, y = 235)
    username_input = Entry(login_root, font = ('Roboto', 15), bd = 2, textvariable = username_value)
    username_input.place(x = 30, y = 265, width = 440, height = 25)

    password_icon_label =  Label(login_root, image = password_icon, bg = LOGIN_BG)
    password_icon_label.place(x = 10, y = 338)
    password = Label(login_root, text = "Password :", font = ('Roboto Light', 13), fg = LOGIN_LABEL_FG, bg = LOGIN_LABEL_BG)
    password.place(x = 10, y = 305)
    password_input = Entry(login_root, font = ('Roboto', 15), bd = 2, textvariable = password_value, show = "*")
    password_input.place(x = 30, y = 335, width = 440, height = 25)

    def show_password():
        check_value = output_val.get()
        if check_value == 0:
            password_input.configure(show = "*")
        else:
            password_input.configure(show = "")  

    output_val = IntVar()
    show_btn = Checkbutton(login_root, text = "Show", offvalue = 0, onvalue = 1, variable = output_val, command = show_password)
    show_btn.place(x = 410, y = 365)
    show_btn.deselect()

    def login_confirming():
        entered_username = username_input.get()
        entered_password = password_input.get()
        login_confirm = False

        if entered_username == USERNAME and entered_password == PASSWORD:
            login_confirm = True
            login_info = messagebox.showinfo(title = "Login Confirmation", message = "Connection confirmed with existing database")
            login_root.destroy()
            connect_db.place_forget()
            replace_login()
        else:
            login_confirm = False
            #username_input.delete(0, END)
            #password_input.delete(0, END)
            login_info = messagebox.showerror(title = "Login Declined", message = "Incorrect Username or Password")

    login_button = Button(login_root, image = loginbtn_img, bd = 0, bg = LOGIN_BG, activebackground = LOGIN_BG, command = login_confirming)
    login_button.place(x = 180, y = 375)
  
    login_root.mainloop()

def on_tab_selected(event):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == "View":
        clear_entered()
        save_record.config(state = DISABLED)
        submit_record.config(state = NORMAL)
        delete_record.config(state = DISABLED)
        clear_btn.config(state = NORMAL)
        donater_input.config(state = NORMAL)
        phone_input.config(state = NORMAL)
        email_input.config(state = NORMAL)
        dob_input.config(state = NORMAL)
        gender_input.config(state = NORMAL)
        bloodgrp_input.config(state = NORMAL)
        amount_input.config(state = NORMAL)
        address_input.config(state = NORMAL)
        city_input.config(state = NORMAL)
        state_input.config(state = NORMAL)
        pincode_input.config(state = NORMAL)

tabcontrol = ttk.Notebook(root)
tab_view   = Frame(tabcontrol,  bg = ROOT_BG)
tab_modify = Frame(tabcontrol, bg = ROOT_BG)
tab_help   = Frame(tabcontrol, bg = ROOT_BG)
tabcontrol.add(tab_view, text = 'View')
tabcontrol.add(tab_modify, text = 'Modify', state = DISABLED)
tabcontrol.add(tab_help, text = 'Help')
tabcontrol.pack(expand = 1, fill = "both")

if messagebox.askokcancel(title = "Recommended", message = "It is highly recommended to view the 'HELP' page once, to avoid damage to your information"):
    tabcontrol.select(tab_help)

def default_settings():
    save_record.config(state = DISABLED)
    submit_record.config(state = NORMAL)
    delete_record.config(state = DISABLED)
    clear_btn.config(state = NORMAL)
    donater_input.config(state = NORMAL)
    phone_input.config(state = NORMAL)
    email_input.config(state = NORMAL)
    dob_input.config(state = NORMAL)
    gender_input.config(state = NORMAL)
    bloodgrp_input.config(state = NORMAL)
    amount_input.config(state = NORMAL)
    address_input.config(state = NORMAL)
    city_input.config(state = NORMAL)
    state_input.config(state = NORMAL)
    pincode_input.config(state = NORMAL)
 
def change_to_update():
    modify_value.get()
    if modify_value.get() == 0:
        enter_sno = messagebox.askquestion(title = "Update Confirmation", message = "Default serial number chosen, Are you sure want to proceed ahead?")
        if enter_sno == 'yes':
            tabcontrol.select(tab_modify)
            save_record.config(state = NORMAL)
            submit_record.config(state = DISABLED)
            delete_record.config(state = DISABLED)
            clear_btn.config(state = NORMAL)
            donater_input.config(state = NORMAL)
            phone_input.config(state = NORMAL)
            email_input.config(state = NORMAL)
            dob_input.config(state = NORMAL)
            gender_input.config(state = NORMAL)
            bloodgrp_input.config(state = NORMAL)
            amount_input.config(state = NORMAL)
            address_input.config(state = NORMAL)
            city_input.config(state = NORMAL)
            state_input.config(state = NORMAL)
            pincode_input.config(state = NORMAL)

        else:
            modify_value.get()
    else:
        tabcontrol.select(tab_modify)
        save_record.config(state = NORMAL)
        submit_record.config(state = DISABLED)
        delete_record.config(state = DISABLED)
        donater_input.config(state = NORMAL)
        phone_input.config(state = NORMAL)
        email_input.config(state = NORMAL)
        dob_input.config(state = NORMAL)
        gender_input.config(state = NORMAL)
        bloodgrp_input.config(state = NORMAL)
        amount_input.config(state = NORMAL)
        address_input.config(state = NORMAL)
        city_input.config(state = NORMAL)
        state_input.config(state = NORMAL)
        pincode_input.config(state = NORMAL)

def change_to_delete():
    modify_value.get()
    if modify_value.get() == 0:
        enter_sno = messagebox.askquestion(title = "Delete Confirmation", message = "Default serial number chosen, Are you sure want to proceed ahead?")
        if enter_sno == 'yes':
            tabcontrol.select(tab_modify)
            delete_record.config(state = NORMAL)
            submit_record.config(state = DISABLED)
            save_record.config(state = DISABLED)
            clear_btn.config(state = DISABLED)
            donater_input.config(state = DISABLED)
            phone_input.config(state = DISABLED)
            email_input.config(state = DISABLED)
            dob_input.config(state = DISABLED)
            gender_input.config(state = DISABLED)
            bloodgrp_input.config(state = DISABLED)
            amount_input.config(state = DISABLED)
            address_input.config(state = DISABLED)
            city_input.config(state = DISABLED)
            state_input.config(state = DISABLED)
            pincode_input.config(state = DISABLED)
        else:
            modify_value.get()
    else:
        tabcontrol.select(tab_modify)
        delete_record.config(state = NORMAL)
        submit_record.config(state = DISABLED)
        save_record.config(state = DISABLED)
        clear_btn.config(state = DISABLED)
        donater_input.config(state = DISABLED)
        phone_input.config(state = DISABLED)
        email_input.config(state = DISABLED)
        dob_input.config(state = DISABLED)
        gender_input.config(state = DISABLED)
        bloodgrp_input.config(state = DISABLED)
        amount_input.config(state = DISABLED)
        address_input.config(state = DISABLED)
        city_input.config(state = DISABLED)
        state_input.config(state = DISABLED)
        pincode_input.config(state = DISABLED)

def change_to_help():
    tabcontrol.select(tab_help)

def change_to_view():
    default_settings()
    tabcontrol.select(tab_view) 

def change_to_modify():
    tabcontrol.select(tab_modify)
    default_settings()

TITLE_FONT      = ('Lemon Milk', 30, 'bold')
TITLE_BG        = "#16697a"
TITLE_FG        = "#f8f1f1"
CLOCK_FONT      = ('Bebas Neue', 12, 'bold')
CLOCK_BG        = "#F05454"
LABEL_FONT      = ('Bebas Neue', 10, 'bold')
LABEL_BG        = "#003049"
LABEL_FG        = "#fcbf49"
INPUT_FONT      = ('Bebas Neue', 13)
BUTTON_FRAME_BG = "#f25c54"
BUTTON_ROOT_BG  = "#fff8cd"
FRAME_BG        = "#f25c54"

# Title
Title_label = Label(root, text = "Blood Bank Management System", font = TITLE_FONT, relief = SOLID, borderwidth = 3, bg = TITLE_BG, fg = TITLE_FG)
Title_label.place(x = 200, y = 30, width = 1100, height = 60)

separator = ttk.Separator(root, orient = HORIZONTAL)
separator.place(x = 0, y = 95, width = 1500, height = 2)

# Clock
Clock_label = Label(root, font = CLOCK_FONT, relief = SOLID, borderwidth = 3, bg = CLOCK_BG)
Clock_label.place(x = 1390, y = 690, width = 100, height = 55)
date_and_time()

# Exit
exit_db = Button(root, image = exitdb_img, bd = 0, bg = BUTTON_ROOT_BG, activebackground = BUTTON_ROOT_BG, command = exit_MS)
exit_db.place(x = 1450, y = 100)
exit_db_ttp = CreateToolTip(exit_db, "Click to exit")

# Help
help_btn = Button(root, image = help_img, bd = 0, bg = BUTTON_ROOT_BG, activebackground = BUTTON_ROOT_BG, command = change_to_help)
help_btn.place(x = 1415, y = 100)
help_btn_ttp = CreateToolTip(help_btn, "Click to see credits and annexures")

def on_closing():
    if messagebox.askyesnocancel("Exit Confirmation", "Do you want to EXIT?"):
        root.destroy()

# Connect to Database
connect_db = Button(root, image = connectdb_img, bd = 0, bg = BUTTON_ROOT_BG, activebackground = BUTTON_ROOT_BG, command = admin_connectDB)
connect_db.place(x = 1320, y = 35)
connectdb_ttp = CreateToolTip(connect_db, "Login to connect to a database")

def replace_login():
    tabcontrol.tab(tab_modify, state = NORMAL)
    export_btn.config(state = NORMAL)
    delete_btn.config(state = NORMAL)
    update_btn.config(state = NORMAL)
    add_new_btn.config(state = NORMAL)
    modify_input.config(state = NORMAL)
    admin_menu = Menubutton(root, image = admin_img, bd = 0, bg = BUTTON_ROOT_BG, activebackground = BUTTON_ROOT_BG)
    admin_menu.menu = Menu(admin_menu, tearoff = 0)
    admin_menu["menu"] = admin_menu.menu
    
    def open_file(): 
        file = askopenfile(mode ='r', filetypes =[('Database File', '*.db')]) 
        if file is not None: 
            content = file.read()
            print(content)

    var1 = IntVar()
    admin_menu.menu.add_checkbutton(label = "Other Databases", variable = var1, command = open_file)

    def sign_out():
        confirm_signout = messagebox.askquestion(title = "Confirm Signout", message = "Do you want to really Signout?")
        if confirm_signout == 'yes':
            admin_menu.place_forget()
            connect_db.place(x = 1320, y = 35)
            tabcontrol.tab(tab_modify, state = DISABLED)
            export_btn.config(state = DISABLED)
            delete_btn.config(state = DISABLED)
            update_btn.config(state = DISABLED)
            add_new_btn.config(state = DISABLED)
            modify_input.config(state = DISABLED)
        else:
            admin_menu.menu.entryconfig(1, onvalue = 0)

    var2 = IntVar()
    admin_menu.menu.add_checkbutton(label = "Sign Out", variable = var2, command = sign_out)
    admin_menu.place(x = 1440, y = 35)

#* Data modificattion frame
Modification_frame = Frame(tab_modify, bg = FRAME_BG, relief = SOLID, borderwidth = 3)
Modification_frame.place(x = 5, y = 150, width = 1485, height = 510)

# Back
back_btn = Button(tab_modify, image = back_img, bd = 0, bg = BUTTON_ROOT_BG, activebackground = BUTTON_ROOT_BG, command = change_to_view)
back_btn.place(x = 5, y = 80)
back_btn_ttp = CreateToolTip(back_btn, "Go back to view mode")

# Labels and INput Boxes
donater_label = Label(Modification_frame, text = "Name of the Donor :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT,relief = SOLID, borderwidth = 2, width = 22, anchor = N)
donater_label.place(x = 5, y = 5, height = 30, width = 150)
donater_value = StringVar()
donater_input = Entry(Modification_frame, font = INPUT_FONT, bd = 2, textvariable = donater_value)
donater_input.place(x = 5, y = 40, height = 25, width = 300)
donater_ttp = CreateToolTip(donater_input, "Enter Donor's Fullname")

phone_label = Label(Modification_frame, text = "Mobile Number :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT, relief = SOLID, borderwidth = 2, width = 22, anchor = N)
phone_label.place(x = 5, y = 70, height = 30, width = 150)
phone_value = IntVar()
phone_input = Entry(Modification_frame, font = INPUT_FONT, bd = 2, textvariable = phone_value)
phone_input.delete(0, END)
phone_input.place(x = 5, y = 105, height = 25, width = 300)
phone_ttp = CreateToolTip(phone_input, "Enter Donor's Mobile number")

email_label = Label(Modification_frame, text = "E-mail :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT, relief = SOLID,borderwidth = 2, width = 22, anchor = N)
email_label.place(x = 5, y = 135, height = 30, width = 150)
email_value = StringVar()
email_input = Entry(Modification_frame, font = INPUT_FONT, bd = 2, textvariable = email_value)
email_input.place(x = 5, y = 170, height = 25, width = 300)
email_ttp = CreateToolTip(email_input, "Enter Donor's E-Mail address")

dob_label = Label(Modification_frame, text = "Date of Birth :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT, relief =SOLID, borderwidth = 2, width = 22, anchor = N)
dob_label.place(x = 5, y = 200, height = 30, width = 150)
dob_value = StringVar()
dob_input = DateEntry(Modification_frame, font = ('Bebas Neue', 15), bd = 2, year = 2000, month = 1, date = 1, showweeknumbers =False, showothermonthdays = False, calendar_cursor = "left_ptr", background = "#ec524b", foreground = "#f3eac2", bordercolor ="#595b83", headersbackground = "#f5b461", headersforeground = "#734046", selectforeground = "#f8f1f1", selectbackground ="#db6400", weekendbackground = "#1a1c20", weekendforeground = "#f9813a", textvariable = dob_value)
dob_input.delete(0, END)
dob_input.place(x = 5, y = 235, height = 25, width = 300)
dob_ttp = CreateToolTip(dob_input, "Enter Donor's Date of Birth")

gender_label = Label(Modification_frame, text = "Gender :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT, relief = SOLID,borderwidth = 2, width = 22, anchor = N)
gender_label.place(x = 5, y = 265, height = 30, width = 150)
gender_value = StringVar()
gender_input = ttk.Combobox(Modification_frame, font = INPUT_FONT, state = 'readonly')
gender_input['values'] = ("Male", "Female", "Trans", "Non-Binary")
gender_input.place(x = 5, y = 300, height = 25, width = 300)
gender_ttp = CreateToolTip(gender_input, "Enter Donor's Gender")

ver_separator1 = ttk.Separator(tab_modify, orient = VERTICAL)
ver_separator1.place(x = 330, y = 155, width = 2, height = 330)

bloodgrp_label = Label(Modification_frame, text = "Blood group :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT, relief =SOLID, borderwidth = 2, width = 22, anchor = N)
bloodgrp_label.place(x = 355, y = 5, height = 30, width = 150)
bloodgrp_value = StringVar()
bloodgrp_input = ttk.Combobox(Modification_frame, font = INPUT_FONT, state = 'readonly')
bloodgrp_input['values'] = ("O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-")
bloodgrp_input.place(x = 355, y = 40, height = 25, width = 300)
bloodgrp_ttp = CreateToolTip(bloodgrp_input, "Enter Donor's Blood group")

amount_label = Label(Modification_frame, text = "Amount of Blood [in ml] :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT,relief = SOLID, borderwidth = 2, width = 22, anchor = N)
amount_label.place(x = 355, y = 70, height = 30, width = 180)
amount_value = IntVar()
amount_input = Entry(Modification_frame, font = INPUT_FONT, bd = 2, textvariable = amount_value)
amount_input.delete(0, END)
amount_input.place(x = 355, y = 105, height = 25, width = 300)
amount_ttp = CreateToolTip(amount_input, "Enter Amount of Blood donated by the Donor")

ver_separator2 = ttk.Separator(tab_modify, orient = VERTICAL)
ver_separator2.place(x = 680, y = 155, width = 2, height = 330)

address_label = Label(Modification_frame, text = "Address :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT, relief =SOLID, borderwidth = 2, width = 22, anchor = N)
address_label.place(x = 705, y = 5, height = 30, width = 150)
address_value = StringVar()
address_input = Entry(Modification_frame, font = INPUT_FONT, bd = 2, textvariable = address_value)
address_input.place(x = 705, y = 40, height = 25, width = 300)
address_ttp = CreateToolTip(address_input, "Enter Donor's Address")

city_label = Label(Modification_frame, text = "City :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT, relief = SOLID,borderwidth = 2, width = 22, anchor = N)
city_label.place(x = 705, y = 70, height = 30, width = 150)
city_value = StringVar()
city_input = Entry(Modification_frame, font = INPUT_FONT, bd = 2, textvariable = city_value)
city_input.place(x = 705, y = 105, height = 25, width = 300)
city_ttp = CreateToolTip(city_input, "Enter name of the city where Donor reside")

state_label = Label(Modification_frame, text = "State :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT, relief = SOLID,borderwidth = 2, width = 22, anchor = N)
state_label.place(x = 705, y = 135, height = 30, width = 150)
state_value = StringVar()
state_input = Entry(Modification_frame, font = INPUT_FONT, bd = 2, textvariable = state_value)
state_input.place(x = 705, y = 170, height = 25, width = 300)
state_ttp = CreateToolTip(state_input, "Enter name of the state where Donor reside")

pincode_label = Label(Modification_frame, text = "Pincode :", bg = LABEL_BG, fg = LABEL_FG, font = LABEL_FONT, relief = SOLID, borderwidth = 2, width = 22, anchor = N)
pincode_label.place(x = 705, y = 200, height = 30, width = 150)
pincode_value = IntVar()
pincode_input = Entry(Modification_frame, font = INPUT_FONT, bd = 2, textvariable = pincode_value)
pincode_input.delete(0, END)
pincode_input.place(x = 705, y = 235, height = 25, width = 300)
pincode_ttp = CreateToolTip(pincode_input, "Enter pincode of the area where Donor reside")

hor_separator1 = ttk.Separator(tab_modify, orient = HORIZONTAL)
hor_separator1.place(x = 10, y = 490, width = 1475, height = 2)

def clear_entered():
    donater_input.delete(0, END)
    phone_input.delete(0, END)
    email_input.delete(0, END)
    dob_input.delete(0, END)
    gender_input.set('')
    bloodgrp_input.set('')
    amount_input.delete(0, END)
    address_input.delete(0, END)
    city_input.delete(0, END)
    state_input.delete(0, END)
    pincode_input.delete(0, END)

#* Tab_add/Submit Button["ADD RECORD"]
submit_record = Button(Modification_frame, image = submit_img, bd = 0, bg = BUTTON_FRAME_BG, activebackground = BUTTON_FRAME_BG,  command = add_record)
submit_record.place(x = 1350, y = 5)
submit_ttp = CreateToolTip(submit_record, "Click to add the record to the database")

#* Tab_add/Save Button["SAVE RECORD"]
save_record = Button(Modification_frame, image = save_img, bd = 0, bg = BUTTON_FRAME_BG, activebackground = BUTTON_FRAME_BG, command = update_donation, state = DISABLED)
save_record.place(x = 1350, y = 50)
save_ttp = CreateToolTip(save_record, "Click to save the updated record to the database")

#* Tab_add/Delete Button["DELETE"]
delete_record = Button(Modification_frame, image = delete_img, bd = 0, bg = BUTTON_FRAME_BG, activebackground = BUTTON_FRAME_BG, command = delete_donation, state = DISABLED)
delete_record.place(x = 1350, y = 95)
delete_ttp = CreateToolTip(delete_record, "Click to delete the record from the database")

#* Tab_Add/Clear Button["CLEAR"]
clear_btn = Button(Modification_frame, image = clear_img, bd = 0, bg = BUTTON_FRAME_BG, activebackground = BUTTON_FRAME_BG, command = clear_entered)
clear_btn.place(x = 705, y = 270)
clear_ttp = CreateToolTip(clear_btn, "Click to clear the entered info")

#* Inside Modification Frame
# Search box for our management system
find_label = Label(tab_view, text = "Find by : ", font = ('Bebas Neue', 23, 'bold'), relief = SOLID, borderwidth = 2, bg = LABEL_BG, fg = LABEL_FG, anchor = S)
find_label.place(x = 5, y = 100, width = 100, height = 45)
find_opt_box = ttk.Combobox(tab_view, font = ('Bebas Neue', 16, 'bold'), state = 'normal')
find_opt_box['values'] = ("Name", "Mobile number", "Blood group", "Amount donated", "Gender", "DOB", "E-mail", "City", "State")
find_opt_box.place(x = 110, y = 100, width = 150, height = 45)
find_opt_ttp = CreateToolTip(find_opt_box, "Select the attribute you want to search")
search_value = StringVar()
find_input = Entry(tab_view, font = INPUT_FONT, bd = 2, textvariable = search_value)
find_input.place(x = 265, y = 100, width = 150, height = 45)
find_ttp = CreateToolTip(find_input, "Enter name of the attribute you want to find")
find_button = Button(tab_view, image = find_img, borderwidth = 0, bg = BUTTON_ROOT_BG, activebackground = BUTTON_ROOT_BG, command = find_data)
find_button.place(x = 420, y = 100)

tabcontrol.bind("<<NotebookTabChanged>>", on_tab_selected)

#* Data show frame
Show_frame = Frame(tab_view, bg = FRAME_BG, relief = SOLID, borderwidth = 3)
Show_frame.place(x = 5, y = 150, width = 1485, height = 510)

# Styling for viewing data in Data show frame
Show_style = ttk.Style()
Show_style.configure('Treeview.Heading', font = ('Trebuchet MS', 13, 'bold'))

#* Inside Modification Frame
# Creating Scroll bars
scroll_X = Scrollbar(Show_frame, orient = HORIZONTAL)
scroll_Y = Scrollbar(Show_frame, orient = VERTICAL)

# Creating table's top column 
info_show = ttk.Treeview(Show_frame, columns = ("ID", "Name", "Date", "Time", "Mobile number", "E-Mail", "DOB", "Gender", "Blood group", "Amount donated", "Address", "City", "State", "Pincode"), height = 15, xscrollcommand = scroll_X.set, yscrollcommand = scroll_Y.set)

# Placing scrollbars in Data Show frame
scroll_X.pack(side = BOTTOM, fill = X)
scroll_Y.pack(side = RIGHT, fill = Y)
scroll_X.config(command = info_show.xview)
scroll_Y.config(command = info_show.yview)

# All columns placing in Data Show frame
info_show.column("#0", width = 130, minwidth = 130)
info_show.column("ID", width = 120, anchor = W, minwidth = 120)
info_show.column("Name", width = 150, anchor = W, minwidth = 100)
info_show.column("Date", width = 190, anchor = W, minwidth = 150)
info_show.column("Time", width = 190, anchor = W, minwidth = 190)
info_show.column("Mobile number", width = 130, anchor = W, minwidth = 130)
info_show.column("E-Mail", width = 200, anchor = W, minwidth = 100)
info_show.column("DOB", width = 150, anchor = W, minwidth = 150)
info_show.column("Gender", width = 100, anchor = W, minwidth = 100)
info_show.column("Blood group", width = 130, anchor = W, minwidth = 130)
info_show.column("Amount donated", width = 220, anchor = W, minwidth = 200)
info_show.column("Address", width = 150, anchor = W, minwidth = 100)
info_show.column("City", width = 150, anchor = W, minwidth = 100)
info_show.column("State", width = 150, anchor = W, minwidth = 100)
info_show.column("Pincode", width = 150, anchor = W, minwidth = 100)

# All columns naming in Data Show frame
info_show.heading("#0", text = "Serial Number")
info_show.heading("ID", text = "Donor ID")
info_show.heading("Name", text = "Donor Name")
info_show.heading("Date", text = "Date of Donation")
info_show.heading("Time", text = "Time of Donation")
info_show.heading("Mobile number", text = "Mobile Number")
info_show.heading("E-Mail", text = "E-Mail")
info_show.heading("DOB", text = "Date of Birth")
info_show.heading("Gender", text = "Gender")
info_show.heading("Blood group", text = "Blood Group")
info_show.heading("Amount donated", text = "Amount Donated (in ml)")
info_show.heading("Address", text = "Address")
info_show.heading("City", text = "City")
info_show.heading("State", text = "State")
info_show.heading("Pincode", text = "Pincode")
info_show.pack()

modify_label = Label(Show_frame, text = "Enter Serial number of the record you want modify :", font = ('Trebuchet MS', 11, 'bold'), relief = SOLID, borderwidth = 2, bg = LABEL_BG, fg = LABEL_FG)
modify_label.place(x = 5, y = 330, width = 400, height = 45)

modify_value = IntVar()
modify_input = Entry(Show_frame, font = INPUT_FONT, bd = 2, textvariable = modify_value, state = DISABLED)
modify_input.place(x = 410, y = 330, width = 100, height = 45)

#* Tab_view/Update Button["UPDATE"]
update_btn = Button(Show_frame, image = update_img, bd = 0, bg = BUTTON_FRAME_BG, activebackground = BUTTON_FRAME_BG, command = change_to_update, state = DISABLED)
update_btn.place(x = 5, y = 380)
update_ttp = CreateToolTip(update_btn, "Click to update the selected record")

#* Tab_view/Delete Button["DELETE"]
delete_btn = Button(Show_frame, image = delete_img, bd = 0, bg = BUTTON_FRAME_BG, activebackground = BUTTON_FRAME_BG, command = change_to_delete, state = DISABLED)
delete_btn.place(x = 140, y = 380)
delete_ttp = CreateToolTip(delete_btn, "Click to delete the selected record")

#* Tab_view/Export Button["EXPORT"]
export_btn = Button(Show_frame, image = export_img, bd = 0, bg = BUTTON_FRAME_BG, activebackground = BUTTON_FRAME_BG, command = export_donation, state = DISABLED)
export_btn.place(x = 1300, y = 380)
export_ttp = CreateToolTip(export_btn, "Click to export the database")

#* Tab_view/Add a new record Button["ADD A NEW RECORD"]
add_new_btn = Button(Show_frame, image = new_record_img, bd = 0, bg = BUTTON_FRAME_BG, activebackground = BUTTON_FRAME_BG, command = change_to_modify, state = DISABLED)
add_new_btn.place(x = 40, y = 420)
add_new_ttp = CreateToolTip(add_new_btn, "Click to add a new record")

#* Help Frame
Help_frame = Frame(tab_help, bg = FRAME_BG)
Help_frame.place(x = 5, y = 150, width = 1485, height = 450)

help_label = Label(tab_help, image = credit_img, bg = BUTTON_ROOT_BG, fg = BUTTON_ROOT_BG, relief = SOLID, borderwidth = 3)
help_label.place(x = 5, y = 120, width = 1485, height = 500)

# Back
back_btn = Button(tab_help, image = back_img, bd = 0, bg = BUTTON_ROOT_BG, activebackground = BUTTON_ROOT_BG, command = change_to_view)
back_btn.place(x = 5, y = 80)
back_btn_ttp = CreateToolTip(back_btn, "Go back to view mode")

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

#* SQL COMMANDS
'''
SELECT - extracts data from a database
UPDATE - updates data in a database
DELETE - deletes data from a database
INSERT INTO - inserts new data into a database
CREATE DATABASE - creates a new database
ALTER DATABASE - modifies a database
CREATE TABLE - creates a new table
ALTER TABLE - modifies a table
DROP TABLE - deletes a table
CREATE INDEX - creates an index (search key)
DROP INDEX - deletes an index
'''