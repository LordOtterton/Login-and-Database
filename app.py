
import sqlite3 as sql
from tkinter.constants import *
from tkinter import *
from tkinter import messagebox



'''

The goal of this app is to let a user register and login
to the application, enter a piece of data which will be sent to
a database, and then allow the user to logout and another user to login.

'''

root = Tk()

#Create database if it dosen't exsist

db = sql.connect('login.db')
cur = db.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS record(
    name text,
    password text,
    email text
   )''')
db.commit()
    

#inserts new registered data into database                

def insert_record(*args):
    
    check_counter=0
    warn = ""
    

    if username_entry.get() == "":
        warn = "Username can't be empty"
    else:
        check_counter += 1
    if register_email.get() == "":
        warn = "Email can't be empty"
    else:
        check_counter += 1
    if password_entry.get() == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if password_again.get() == "":
        warn = "Re-enter password can't be empty"
    else:
        check_counter += 1
    if password_entry.get() != password_again.get():
        warn = "Passwords didn't match!"
    else:
        check_counter += 1
    if check_counter == 5:        
        try:
            db = sql.connect('login.db')
            cur = db.cursor()
            cur.execute('INSERT INTO record VALUES(:name, :password, :email)',
             {
                'name': username_entry.get(),
                'password':password_entry.get(),
                'email': register_email.get(),
             })
            db.commit()
            messagebox.showinfo('confirmation', 'Record Saved')
        except Exception as ep:
            messagebox.showerror('', ep) 
    else:
        messagebox.showerror('Error', warn)


# Checks database for username and password for login

def login_response(*args):
    try:
        db = sql.connect('login.db')
        c = db.cursor()
        for row in c.execute("Select * from record"):
            username = row[0]
            pwd = row[1]
        
    except Exception as ep:
        messagebox.showerror('', ep)

    uname = username_verify.get()
    upwd = password_verify.get()
    check_counter=0
    if uname == "":
       warn = "Username can't be empty"
    else:
        check_counter += 1
    if upwd == "":
        warn = "Password can't be empty"
    else:
        check_counter += 1
    if check_counter == 2:
        if (uname == username and upwd == pwd):
            messagebox.showinfo('Login Status', 'Logged in Successfully!')
        
        else:
            messagebox.showerror('Login Status', 'invalid username or password')
    else:
        messagebox.showerror('', warn)



# frames for display

frame_login = Frame(root, width= 300, height=300, background = '#161616').grid(columnspan=3, rowspan= 3)
frame_register = Frame(root, width= 300, height=300, background = '#161616').grid(columnspan=3, rowspan=5, row = 3)
    
 


'''
    This portion is for the login screen
'''


username_label = Label(frame_login, text="Username", background= '#a6a6a6').grid(column= 0, row = 0, sticky = (W))
username_verify = Entry(frame_login)
username_verify.grid(column= 1, row = 0)

password_label = Label(frame_login, text="Password", background= '#a6a6a6').grid(column= 0, row = 1, sticky = (W))
password_verify = Entry(frame_login)
password_verify.grid(column= 1, row = 1)

submit_button = Button(frame_login, text="Login", command= login_response).grid(column= 1, row= 2)



'''
    This portion is for the register screen
'''


username_label = Label(frame_register, text= "Username", background= '#a6a6a6').grid(column= 0, row = 3, sticky = (W))
username_entry = Entry(frame_register)
username_entry.grid(column= 1, row = 3)

password_label = Label(frame_register, text= "Password", background= '#a6a6a6').grid(column= 0, row = 4, sticky = (W))
password_entry = Entry(frame_register,  show= '*')
password_entry.grid(column= 1, row = 4)

password_again_label = Label(frame_register, text= "Re-enter Password", background= '#a6a6a6').grid(column= 0, row = 5, sticky = (W))
password_again = Entry(frame_register, show= '*')
password_again.grid(column= 1, row = 5)

email_lable = Label(frame_register, text= "Email", background= '#a6a6a6').grid(column= 0, row= 6, sticky = (W))
register_email = Entry(frame_register)
register_email.grid(column= 1, row = 6)

submit_button = Button(frame_register, text="Submit", command= insert_record).grid(column= 1, row= 7)



root.mainloop()