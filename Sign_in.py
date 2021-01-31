import pandas as pd
import sqlalchemy
from tkinter import *
from plyer import notification
import smtplib 
good_username = False 
good_pass = False
engine = sqlalchemy.create_engine('mysql+pymysql://root:raunakcodes2625@localhost:3306/xyz')
login_window = Tk()
username = Entry(login_window)
password = Entry(login_window)
passwords = pd.read_sql_table('accounts',engine,columns=['password_'])
usernames = pd.read_sql_table('accounts',engine,columns=['username'])
def sign_in():
    global username 
    global password
    global passwords 
    global usernames
    global good_username
    global good_pass
    for user in usernames:
        if user not in usernames:
            notification.Notify(
                title = 'FAIL',
                message = 'BAD USERNAME',
                app_icon=None,
                toast = False
            )
            good_username = False
        elif user in usernames:
            good_username = True
    for pass in passwords:
        if pass not in passwords:
            notification.Notify(
                title = 'FAIL',
                message = 'BAD PASSWORD',
                app_icon=None,
                toast = False
                )
            good_pass = False 
        elif pass in passwords:
            good_pass = True 
    if good_pass == True and good_username == True :
        notification.Notify(
                title = 'Success',
                message = 'successfully logged in :)',
                app_icon=None,
                toast = False
            )
        
        
