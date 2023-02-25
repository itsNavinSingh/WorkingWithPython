import random
import tkinter
from tkinter import messagebox
import pyperclip
import PassFetch
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    passlist = [chr(random.randint(33, 123)) for i in range (random.randint(8, 13))]
    password = ''
    for i in range (len(passlist)):
        password += random.choice(passlist)
    password_Entry.delete(0, tkinter.END)
    password_Entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    Website_Name = website_Entry.get()
    Mail_Name = mail_Entry.get()
    Password_Name = password_Entry.get()
    if Website_Name != '' and Mail_Name != '' and Password_Name != '':
        confirm = messagebox.askokcancel(title=Website_Name, message=f'Username: {Mail_Name}\nPassword: {Password_Name}\nDo you want to save?')
        if confirm:
            user_data = {
                'Website': [Website_Name],
                'Username': [Mail_Name],
                'Password': [Password_Name]
            }
            PassFetch.save_pass(user_data)
            website_Entry.delete(0, tkinter.END)
            mail_Entry.delete(0, tkinter.END)
            password_Entry.delete(0, tkinter.END)
            messagebox.showinfo(title='Saved', message='Password Saved Successfully!')
    else:
        messagebox.showerror(title='Error 404', message='Please fill all the details')
# ---------------------------- FETCH PASSWORD ------------------------------- #
def fetch_password():
    try:
        site_info = website_Entry.get()
        info = PassFetch.fetch_pass(site_info)
        mail_Entry.delete(0, tkinter.END)
        mail_Entry.insert(0, info['Username'])
        password_Entry.delete(0, tkinter.END)
        password_Entry.insert(0, info['Password'])
        pyperclip.copy(info['Password'])
    except:
        messagebox.showwarning(title='OPPs', message='Data Not Found!')
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.config(padx=20, pady=20)
window.title('Password Manager')
canva = tkinter.Canvas(width=200, height=200, highlightthickness=0)
Logo = tkinter.PhotoImage(file='logo.png')
canva.create_image(100, 100, image=Logo)
canva.grid(row=0, column=1)
website_Label = tkinter.Label(text='Website: ', highlightthickness=0)
website_Label.grid(row=1, column=0)
website_Entry = tkinter.Entry(width=50)
website_Entry.grid(row=1, column=1, columnspan=2)
website_Entry.focus()
mail_Label = tkinter.Label(text='Username/Email: ', highlightthickness=0)
mail_Label.grid(row=2, column=0)
mail_Entry = tkinter.Entry(width=50, highlightthickness=0)
mail_Entry.grid(row=2, column=1, columnspan=2)
password_Label = tkinter.Label(text='Password: ', highlightthickness=0)
password_Label.grid(row=3, column=0)
password_Entry = tkinter.Entry(width=31, highlightthickness=0)
password_Entry.grid(row=3, column=1)
genPass_button = tkinter.Button(text='Generate Password', width=14, highlightthickness=0, command=password_generator)
genPass_button.grid(row=3, column=2)
add_Button = tkinter.Button(text='Add', width=31, highlightthickness=0, command=save_password)
add_Button.grid(row=4, column=1)
fetch_Button = tkinter.Button(text='Fetch', width=14, highlightthickness=0, command=fetch_password)
fetch_Button.grid(row=4, column=2)

window.mainloop()