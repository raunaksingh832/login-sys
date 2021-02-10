# Hi This is Raunak singh a student of class 9 
# This is one of my projects which is basically a login system 
# to contact me gmail - raunakprogrammer@gamil.com or raunak.priya.dinkar@gmail.com
#Github - raunak832
import pandas as pd
import sqlalchemy
from tkinter import *
from plyer import notification
import smtplib
from random import shuffle
'''imported required libs'''
good_username = False
good_pass = False
engine = sqlalchemy.create_engine('mysql+pymysql://root:raunakcodes2625@localhost:3306/xyz')
main_window = Tk()
login_window = Tk()
sign_up_window = Tk()
main_window.title('MAIN WINDOW')
login_window.title('LOGIN')
sign_up_window.title('SIGN_UP')
username = Entry(login_window)
password = Entry(login_window)
New_Username = Entry(sign_up_window)
New_password = Entry(sign_up_window)
New_Email = Entry(sign_up_window)
OTP = Entry(sign_up_window)
'''some tkinter work and connecting to database'''
username_query = 'SELECT username FROM accounts'
password_query = 'SELECT password_ FROM accounts'
'''making sql queries to execute later'''
usernames = str(pd.read_sql_query(username_query,engine)).split()
passwords = str(pd.read_sql_query(password_query,engine)).split()
'''executing sql queries and making lists of usernames and passwords'''
def window():
    global username    
    global password
    global passwords 
    global usernames
    global good_username
    global good_pass
    global login_window
#main window func 
    def Login():
        global good_pass
        global good_username
        Label(login_window,text='Username',fg='red').pack()
        username.pack()
        Label(login_window,text='Password',fg='blue').pack()
        password.pack()
        # login window front end work
        def login():
            '''logic for logging in'''
            global good_pass
            global good_username
            for user in usernames:
                if username.get() not in usernames:
                    Label(login_window,text='*NO such username',bg='red').pack()
                    good_username = False
                elif username.get() in usernames:
                    good_username = True
            for pas in passwords:
                if password.get() not in passwords:
                    Label(login_window,text='*incorrect password',bg='red').pack()
                    good_pass = False 
                elif password.get() in passwords and passwords.index(password.get()) == usernames.index(username.get()):
                    good_pass = True 
            if good_pass == True and good_username == True :
                Label(login_window,text='SIGN IN SUCCESSFULLY',bg='blue').pack()
            else:
                Label(login_window,text='bad username or password',fg='red').pack()
        Button(login_window,text='LOGIN',command=login,bg='blue').pack()
        login_window.mainloop()
        #mainloop and a button to open login window 
    def sign_up():
        #for signing up 
        Otps = list(range(5000,10000))
        shuffle(Otps)
        x = Otps[6]
        Label(sign_up_window,text='Username',fg='blue').pack()
        New_Username.pack()
        Label(sign_up_window,text='Password',fg='red').pack()
        New_password.pack()
        Label(sign_up_window,text='Email',fg='blue').pack()
        New_Email.pack()
        Label(sign_up_window,text='OTP',fg='red').pack()
        OTP.pack()
        # creates the sign up window 
        def send_otp():
            #sends a otp to mail
            smtp_object = smtplib.SMTP('smtp.gmail.com',587)
            smtp_object.ehlo()
            smtp_object.starttls()
            email = 'raunak.priya.dinkar@gmail.com'
            password = 'mbpzcoqjrigbuher'
            smtp_object.login(email,password)
            to = New_Email.get()
            subject = 'Your login OTP'
            content = 'your OTP is' + str(x)
            msg =  subject + '\n' + content 
            smtp_object.sendmail(email,to,msg)
        def sign():
            if OTP.get() == str(x):
                Query = f'''insert into accounts values('{New_Username.get()}',{int(New_password.get())},'{New_Email.get()}')'''
                with engine.begin() as conn:
                    conn.execute(Query)
                Label(sign_up_window,text='SIGNED up !',bg='blue').pack()
            else:
                Label(sign_up_window,text='BAD OTP',bg='red').pack()
            #verifies and signs you in 
        Button(sign_up_window,text='Send otp',command=send_otp,bg='green').pack()
        Button(sign_up_window,text='SIGN UP', command=sign,bg='purple').pack()
        sign_up_window.mainloop()
        #mainloop and some buttons
    Button(main_window,text='Login',command=Login,bg='blue').pack()
    Button(main_window,text='Sign up',command=sign_up,bg='red').pack()
    main_window.mainloop()
    #mainloop for main window 
    #some buttons
if __name__ == '__main__':
    window()
#Done!
