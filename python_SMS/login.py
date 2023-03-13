from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'Fields cannot be emtpy')

    elif usernameEntry.get()=='melvin' and passwordEntry.get()=='1234':
        messagebox.showinfo('Success', 'Welcome')
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error', 'Please enter correct details')


window = Tk()     #this class helps us create a window

window.geometry('1366x768+0+0')
window.title('Student Login')

window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window, image=backgroundImage)

bgLabel.place(x=0, y=0)

loginFrame = Frame(window, bg='white')
loginFrame.place(x=400, y=150)

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)
#username
userImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, image=userImage, text='Username', compound=LEFT, font=('times new roman', 20, 'bold'))
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5)
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

#password
passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT, font=('times new roman', 20, 'bold'))
passwordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5)
passwordEntry.grid(row=2, column=1, pady=10, padx=20)



loginButton = Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'),
                     width=15, fg='white', bg='cornflowerblue', activebackground='green',
                     activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1,pady=10 )



window.mainloop()    #it will keep your window on a loop
