import pandas as pd
import sqlalchemy
from tkinter import *
from plyer import notification
import smtplib
from random import shuffle
good_username = False
good_pass = False
engine = sqlalchemy.create_engine('mysql+pymysql://root:raunakcodes2625@localhost:3306/xyz')
main_window = Tk()
login_window = Tk()
sign_up_window = Tk()
username = Entry(login_window)
password = Entry(login_window)
New_Username = Entry(sign_up_window)
New_password = Entry(sign_up_window)
New_Email = Entry(sign_up_window)
OTP = Entry(sign_up_window)
passwords = pd.read_sql_table('accounts',engine,columns=['password_'])
usernames = pd.read_sql_table('accounts',engine,columns=['username'])
def window():
    global username    
    global password
    global passwords 
    global usernames
    global good_username
    global good_pass
    global login_window

    def Login():
        global good_pass
        global good_username
        Label(login_window,text='Username').pack()
        username.pack()
        Label(login_window,text='Password').pack()
        password.pack()
        def login():
            global good_pass
            global good_username
            for user in usernames:
                if username.get() not in usernames:
                    notification.Notify(
                        title = 'FAIL',
                        message = 'BAD USERNAME',
                        app_icon=None,
                        toast = False
                    )
                    good_username = False
                elif username.get() in usernames:
                    good_username = True
            for pas in passwords:
                if password.get() not in passwords:
                    notification.Notify(
                        title = 'FAIL',
                        message = 'BAD PASSWORD',
                        app_icon=None,
                        toast = False
                        )
                    good_pass = False 
                elif password.get() in passwords:
                    good_pass = True 
            if good_pass == True and good_username == True :
                notification.Notify(
                        title = 'Success',
                        message = 'successfully logged in :)',
                        app_icon=None,
                        toast = False
                    )
        login_window.mainloop()
        Button(login_window,text='LOGIN',command=login).pack()
    def sign_up():
        Otps = list(range(5000,10000))
        shuffle(Otps)
        x = Otps[6]
        Label(sign_up_window,text='Username').pack()
        New_Username.pack()
        Label(sign_up_window,text='Password').pack()
        New_password.pack()
        Label(sign_up_window,text='Email').pack()
        New_Email.pack()
        Label(sign_up_window,text='OTP').pack()
        OTP.pack()
        def send_otp():
            smtp_object = smtplib.SMTP('smtp.gmail.com',587)
            smtp_object.ehlo()
            smtp_object.starttls()
            email = 'raunakprogrammer@gmail.com'
            password = 'ohskexslaukiwaff'
            smtp_object.login(email,password)
            to = New_Email.get()
            subject = 'Your login OTP'
            content = 'your OTP is' + str(x)
            msg =  subject + '\n' + content 
            smtp_object.sendmail(email,to,msg)
        if OTP.get() == x:
            Query = f'''insert into accounts values({New_Username.get()},{int(New_password.get())},{New_Email.get()})'''
            pd.read_sql_query(Query,engine)
            notification.Notify(
                title = 'SUCCESS',
                message= 'signed up successfully',
                app_icon = None,
                toast=False
            )
        else:
            notification.Notify(
                title='Fail',
                message = 'Failed Signing Up',
                app_icon = None,
                toast = False 
            )
        sign_up_window.mainloop()
        Button(sign_up_window,text='Send otp',command=send_otp).pack()
    Button(main_window,text='Login',command=Login).pack()
    Button(main_window,text='Sign up',command=sign_up).pack()
    main_window.mainloop()
if __name__ == '__main__':
    window()
