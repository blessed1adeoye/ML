from tkinter import *
from tkinter import messagebox, ttk
# from tkinter import 
import mysql.connector
from datetime import date
# from reg import *

background = '#06283D'
framebg = '#EDEDED'
framefg = '#06283D'

today = date.today()
dformate = today.strftime(" %d:%m:%Y")

log = Tk()
log.title(f'Welcome to Today {dformate} This is Heart Attack Prediction System Login | Designed by Blessedera GlowTechie  | omobuwa BLESSED ADEOYE   ')
log.geometry('1303x740+115+10')
log.config(bg=background)
log.resizable(False, False)

# Icon
icon_img = PhotoImage(file='img/ico.png')
log.iconphoto(False, icon_img)


# Background Image
frame = Frame(log, bg='red')
frame.pack(fill=Y)

background_img = PhotoImage(file='img/LOGIN4.png')
Label(frame, image=background_img).pack()


# USER ENTRY

def user_enter(e):
    txt_username.delete(0,'end')
    

def user_leave(e):
    name = txt_username.get()
    if name == '':
        txt_username.insert(0, 'Username')

txt_username = Entry(frame, width=18, fg='#fff', bg='#375174', border=0,
             font=('Arial Bold', 24))
txt_username.insert(0, 'Username')
txt_username.bind('<FocusIn>', user_enter)
txt_username.bind('<FocusOut>', user_leave)
txt_username.place(x=500, y=320)


# PASSWORD ENTRY

def password_enter(e):
    txt_password.delete(0,'end')
    

def password_leave(e):
    if txt_password.get() == '':
        txt_password.insert(0, 'Password')

txt_password = Entry(frame, width=18, fg='#fff',show='*', bg='#375174', border=0,font=('Arial Bold', 20))
txt_password.insert(0, 'Password')
txt_password.bind('<FocusIn>', password_enter)
txt_password.bind('<FocusOut>', password_leave)
txt_password.place(x=500, y=410)

# ========================= MAIN FUNCTIONS ============ ####

global trial_no 
trial_no =0
def trial():
    global trial_no 
    trial_no +=1
    print('Trial time ', trial_no) 
    if trial_no == 3:
        messagebox.showwarning("Warning", 'You have tried more than Limit')
        # Close Program
        log.destroy()



def login():
    username = txt_username.get()
    password  = txt_password.get()

    if (username=="" or username=="Username") or (password == "" or password=="Password"):
        messagebox.showerror("Entry Error", "Type username or password Correctly !!!")
    else:
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='0000', database='heart_data')
            mycursor = mydb.cursor()
            print('Database Connected')
            command1 = 'CREATE TABLE IF NOT EXISTS userlogin(user int auto_increment key not null, first_name varchar(100), last_name varchar(100), Contact varchar(15), Email varchar(50), Question varchar(100), Answer varchar(100), Username varchar(100), Password varchar(100))'
            mycursor.execute(command1)
            # print('Table Created')


        except:
            messagebox.showerror("Connected", "Database not connection ")
            return
        
        dbcommand="use heart_data"
        mycursor.execute(dbcommand)
        tabledbcommand = 'select * from userlogin where Username = %s and Password = %s'
        mycursor.execute(tabledbcommand, (username, password))
        myresult = mycursor.fetchone()
        print(myresult)

        if myresult == None:
            messagebox.showerror('Invalid', 'Invalid username and password !')
            trial()

        else:
            messagebox.showinfo('Login', f'Successfully Log {username} in\n Welcome to Our Heart Disease Prediction System {username} ')
            log.destroy()
            import a 



button_mode = True

def hidePassword():
    global button_mode
    if button_mode:
        eyebtn.config(image=close_eye, activebackground='#1f5675')
        txt_password.config(show='*')
        button_mode = False

    else:
        eyebtn.config(image=openeye, activebackground='#1f5675')
        txt_password.config(show='')
        button_mode = True


openeye = PhotoImage(file='img/openeye.png')
close_eye = PhotoImage(file='img/close_eye.png')

eyebtn = Button(log, image=openeye, bg='#375174',bd=0, command=hidePassword)
eyebtn.place(x=820, y=410)


signin_btn = Button(log, text='LOGIN', bg='#1f5675', fg='white', width=13, height=1,font=('Roboto', 16, 'bold'), bd=0, activebackground='gold', activeforeground='blue', command=login)
signin_btn.place(x=570,y=600)

def register():
    log.destroy()
    import reg

signup_label = Label(log, text=" Don't have an account ? ", bg='#00264d', fg='white', font=('Microsoft Yahei UI Light',10), anchor='center').place(x=400, y=470)



to_reg_btn = Button(log, text='SIGN UP', font='Arial 10 bold' ,command=register, border=0, cursor='hand2', fg='#57a1f8', bg='#00264d', activebackground='gold', activeforeground='blue') #  fg='#deeefb',
to_reg_btn.place(x=550, y=470)


def forget_password():
    if cmb_question.get() == 'Select One' or txt_answer.get() == '' or txt_new_password.get() == '':
        messagebox.showerror('Error',  'All Fields are Required', parent=forgetP)

    else:
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='0000', database='heart_data')
            mycursor = mydb.cursor()
            mycursor.execute('select * from userlogin where Username=%s and Question=%s and Answer=%s',
                              (txt_username.get(), cmb_question.get(), txt_answer.get())
                            )
            print(txt_username.get(), cmb_question.get(), txt_answer.get())
            row = mycursor.fetchone()
            if row == None:
                print(row)
                messagebox.showerror('Error', 'Please Select the correct Security Question / Enter Correct Answer to reset your password ', parent=forgetP)
            else:
                mycursor.execute('update userlogin set Password=%s where Username=%s',
                              (txt_new_password.get(), txt_username.get())
                            )
                mydb.commit()
                mydb.close()
                messagebox.showinfo('Success','Your Password has been successfully reset, Please login with the New Password', parent=log )
                forgetP.destroy()

        except Exception as es :  # Exception as es
            # messagebox.showwarning('Success','Your Password was not successfully reset, Please Try Again', parent=log )          
            messagebox.showerror('Error', f'Error due to: {es}', parent=log)




def forget_passwordwindow():
    global forgetP
    global cmb_question
    global txt_answer
    global txt_new_password
    
    if txt_username.get() == '' or txt_username.get() == 'Username':
        messagebox.showerror('Error',  'Please Enter your username to reset your password', parent=log)
    else:
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='0000', database='heart_data')
            mycursor = mydb.cursor()
            mycursor.execute('select * from userlogin where Username=%s', (txt_username.get(),))
            row = mycursor.fetchone()
            if row == None:
                print(row)
                messagebox.showerror('Error', 'Please Enter the Invalid USERNAME to reset your password ', parent=log)
            else:
                mydb.close()
                forgetP = Toplevel()
                forgetP.title('Forget Password')
                forgetP.geometry('570x450+480+220')
                forgetP.config(bg='#00264d')
                forgetP.resizable(False, False)
                forgetP.focus_force()
                forgetP.grab_set()

                Label(forgetP, text='Forget Password', font=('times new roman', 20, 'bold'), bg='#00264d', fg='white').place(x=180, y=5)

                # Icon
                icon_img = PhotoImage(file='img/ico.png')
                forgetP.iconphoto(False, icon_img)

                ####################################### Forget Password
                Label(forgetP, text='Security Question', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=220, y=70)
                cmb_question = ttk.Combobox(forgetP, font=('times new roman', 15,"bold"), state='readonly', justify=CENTER)
                cmb_question['values'] = ("Select One", "Your First Pet Name", "Your Place of Birth", "Your Best Friend's Name")
                cmb_question.place(x=150, y=100, width=250)
                cmb_question.current(0)

                

                Label(forgetP, text='Answer ', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=230, y=150)
                txt_answer = Entry(forgetP, font=('times new roman', 15,"bold"), fg='green')
                txt_answer.place(x=150, y=180, width=250)


                

                Label(forgetP, text='New Password ', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=220, y=230)
                txt_new_password = Entry(forgetP, show='*', font=('times new roman', 15,"bold"), fg='green')
                txt_new_password.place(x=150, y=255, width=250)


                change_password_btn = Button(forgetP, command=forget_password, text='Reset Password', font=('times new roman', 15, 'bold'), bg='green', bd=2, cursor='hand2', fg='white', activebackground='gold', activeforeground='#00264d')
                change_password_btn.place(x=200, y=310)

        except Exception as q:
            messagebox.showerror('Error', f'Error due to: {q}', parent=log)
        


forgotten_password = Button(log, text='Forget  Password', font='Arial 10 bold' ,command=forget_passwordwindow, border=0, cursor='hand2', fg='#57a1f8', bg='#00264d', activebackground='gold', activeforeground='blue') #  fg='#deeefb',
forgotten_password.place(x=700, y=470)

# ================== Footer ================
lbl_footer = Label(log, text=' Blessedera Techies - Heart Disease Prediction System | Developed by Omobuwa Blessed Adeoye (O.B.A.) \nFor any Technical Issue Contact: +2348132986310', font=("times new roman",11, "bold"),bg=background, fg="white").place(x=0, y=707, relwidth=1, height=30) # pack(side=BOTTOM, fill=X)











log.mainloop()