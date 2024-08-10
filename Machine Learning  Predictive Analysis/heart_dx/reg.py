from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from datetime import date
# from PIL import ImageTk, Image

background = '#06283D'
framebg = '#EDEDED'
framefg = '#06283D'

today = date.today()
dformate = today.strftime(" %d:%m:%Y")

reg = Tk()
reg.title(f'Welcome to Today {dformate} This is Heart Attack Prediction System SignUp | Designed by Blessedera GlowTechie  | omobuwa BLESSED ADEOYE   ')
reg.geometry('1303x740+115+10')
reg.config(bg=background)
reg.resizable(False, False)

# Icon
icon_img = PhotoImage(file='img/ico.png')
reg.iconphoto(False, icon_img)


# ++++++++++++++++++++++++====



#  Frame 1
# ade = PhotoImage(file='img/loc.jpg')
adef = Frame(reg, background=background)
adef.place(x=50, y=50, width=470, height=600)
ade = PhotoImage(file='img/gold.png')
a = Label(adef, image=ade)
a.place(x=0, y=0, width=470)

adex = PhotoImage(file='img/gold1.png')
b = Label(adef, image=adex)
b.place(x=0, y=270, width=470)
Label(adef, text='We are the best', fg='white', bg=background, font=('Helvetica', 25, 'bold')).place(x=80, y=560)


#======================== FUNCTIONS
def clearuserData():
    txt_fname.delete(0, END)
    txt_lname.delete(0, END)
    txt_contact.delete(0, END)
    txt_email.delete(0, END)
    cmb_question.delete(0, END)
    txt_answer.delete(0, END)
    txt_username.delete(0, END)
    txt_password.delete(0, END)
    txt_cpassword.delete(0, END)


def registerUser():
    if txt_fname.get() == '' or txt_lname.get() == '' or txt_contact.get() == '' or txt_email.get() == '' or cmb_question.get() == 'Select One' or txt_answer.get() == '' or txt_username.get() == '' or txt_password.get() == '' or txt_cpassword.get() == '':
        messagebox.showerror('Error', 'All Field are Required', parent=reg)

    elif txt_password.get() != txt_cpassword.get():
        messagebox.showerror('Error', 'Password & Confirm Password Should be the same', parent=reg)

    elif var_chk.get() == 0:
        messagebox.showerror('Error', 'Please Agree to our terms & conditions', parent=reg)

    else:
        try:
            mydb = mysql.connector.connect(host='localhost', user='root', password='0000', database='heart_data')
            mycursor = mydb.cursor()

            command1 = 'CREATE TABLE IF NOT EXISTS userlogin(user int auto_increment key not null, first_name varchar(100), last_name varchar(100), Contact varchar(15), Email varchar(50), Question varchar(100), Answer varchar(100), Username varchar(100), Password varchar(100))'
            mycursor.execute(command1)
            print('Table Created')
            dbcommand="use heart_data"
            mycursor.execute(dbcommand)
            tabledbcommand = 'select * from userlogin where Username=%s'
            val = (txt_username.get(),)
            mycursor.execute(tabledbcommand,  val)
            row = mycursor.fetchone()
            print(row)
            if row != None:
                messagebox.showerror('Error', 'User Already exist, Please try with another Username', parent=reg)
            else:
                mycursor.execute("insert into userlogin (first_name, last_name, Contact, Email, Question, Answer, Username, Password) values(%s, %s, %s, %s, %s, %s, %s, %s) ",

                                    (
                                        txt_fname.get(),
                                        txt_lname.get(),
                                        txt_contact.get(),
                                        txt_email.get(),
                                        cmb_question.get(),
                                        txt_answer.get(),
                                        txt_username.get(),
                                        txt_password.get()
                                    )
                                
                                )
                mydb.commit()
                mydb.close()
                messagebox.showinfo('Success', 'Successfully Sign Up', parent=reg)
                clearuserData()
        except Exception as q:
            messagebox.showerror('Error', f'Error due to: {q}', parent=reg)
        #     return
        # dbcommand="use heart_data"
        # mycursor.execute(dbcommand)
      

        
            # messagebox.showinfo('Success', 'Successfully Sign Up', parent=reg)
        print('ONAGA')
        # txt_lname.get(),
        # txt_contact.get(),
        # txt_email.get(),
        # cmb_question.get(),
        # txt_answer.get(),
        # txt_username.get(),
        # txt_password.get(),
        # txt_cpassword.get())



title = Label(reg, text='Register Here', font=("times new roman",20, "bold"),bg=background, fg="gold").place(x=750, y=30)
##################################### ROW 1
var_fname = StringVar()

var_lname = StringVar()

f_name = Label(reg, text='First Name', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=630, y=100)
txt_fname = Entry(reg, font=('times new roman', 15,"bold"), fg='green', textvariable=var_fname)
txt_fname.place(x=550, y=130, width=250)

l_name = Label(reg, text='Last Name', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=1000, y=100)
txt_lname = Entry(reg, textvariable=var_lname, font=('times new roman', 15,"bold"), fg='green')
txt_lname.place(x=920, y=130, width=250)

###################################### ROW 2
var_contact = StringVar()

var_email = StringVar()


contact = Label(reg, text='Contact NO.', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=630, y=170)
txt_contact = Entry(reg, textvariable=var_contact, font=('times new roman', 15,"bold"), fg='green')
txt_contact.place(x=550, y=200, width=250)

email = Label(reg, text='Email ', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=1000, y=170)
txt_email = Entry(reg, textvariable=var_email, font=('times new roman', 15,"bold"), fg='green')
txt_email.place(x=920, y=200, width=250)


####################################### ROW 3
question = Label(reg, text='Security Question', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=600, y=240)
cmb_question = ttk.Combobox(reg, font=('times new roman', 15,"bold"), state='readonly', justify=CENTER)
cmb_question['values'] = ("Select One", "Your First Pet Name", "Your Place of Birth", "Your Best Friend's Name")
cmb_question.place(x=550, y=270, width=250)
cmb_question.current(0)

var_answer = StringVar()

answer = Label(reg, text='Answer ', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=1000, y=240)
txt_answer = Entry(reg, textvariable=var_answer, font=('times new roman', 15,"bold"), fg='green')
txt_answer.place(x=920, y=270, width=250)


######################################### ROW 4

var_username = StringVar()

var_password = StringVar()

username = Label(reg, text='Username', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=630, y=320)
txt_username = Entry(reg,textvariable=var_username, font=('times new roman', 15,"bold"), fg='green')
txt_username.place(x=550, y=350, width=250)

password = Label(reg, text=' Password ', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=1000, y=320)
txt_password = Entry(reg, textvariable=var_password, show='*', font=('times new roman', 15,"bold"), fg='green')
txt_password.place(x=920, y=350, width=250)


####################################### Row 5

var_confirm_password = StringVar()

cpassword = Label(reg, text='Confirm Password ', font=("times new roman",13, "bold"),bg=background, fg="gold").place(x=970, y=380)
txt_cpassword = Entry(reg,textvariable=var_confirm_password,  show='*', font=('times new roman', 15,"bold"), fg='green')
txt_cpassword.place(x=920, y=410, width=250)

############################# Terms



# =============== Terms & Conditions Button =================
def TC():
    terms_conditions = Toplevel(reg)
    terms_conditions.title("Terms and Conditions")
    terms_conditions.geometry('700x600+650+80')

    # Icon
    icon_img = PhotoImage(file='img/info.png')
    terms_conditions.iconphoto(False, icon_img)

    # Heading
    Label(terms_conditions, text='Information Related to Terms and Conditions', font='roboto 17 bold').pack(padx=20, pady=20)

    #Info
    Label(terms_conditions, text=' When you agree  ', fg='magenta' , font='arial 11').place(x=20, y=100)
    Label(terms_conditions, text='We ensure that your sensitive data, such as Email, Health Informationis only accessed by authorized personnel', font='arial 11').place(x=20, y=130)
    Label(terms_conditions,text='we consider this Heart Disease Predictive app help people to track their heart status',font='arial 11').place(x=20, y=160)
    Label(terms_conditions, text='for prompt medical care if need arises',font='arial 11').place(x=20, y=190)
    Label(terms_conditions, text='confidentiality is our Watch word and you are always safe with us ', font='arial 11').place(x=20, y=220)
    # Label(terms_conditions, text='vi. fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)', font='arial 11').place(x=20, y=250)
    # Label(terms_conditions, text='vii. restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)',font='arial 11').place(x=20, y=280)
    # Label(terms_conditions, text='viii. thalach - maximum heart rate achieved', font='arial 11').place(x=20, y=310)
    # Label(terms_conditions, text='ix. exang - exercise induced angina (1 = yes; 0 = no)', font='arial 11').place(x=20, y=340)
    # Label(terms_conditions, text='x. oldpeak - ST depression induced by exercise relative to rest', font='arial 11').place(x=20, y=370)
    # Label(terms_conditions, text='xi. slope - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)',font='arial 11').place(x=20, y=400)
    # Label(terms_conditions, text='xii. ca - number of major vessels (0-3) colored by flourosopy', font='arial 11').place(x=20, y=430)
    # Label(terms_conditions, text='xiii. thal - 0 = normal; 1 = fixed defect; 2 = reversable defect', font='arial 11').place(x=20, y=460)
    # Label(terms_conditions, text=f'xiv. x. oldpeak - ST depression induced by exercise relative to rest(0vgcwee', font='arial 11').place(x=20, y=490)
    # Label(terms_conditions, text='xv. x. oldpeak - ST depression induced by exercise relative to rest ', font='arial 11').place(x=20, y=510)
    btn_finish_reading = Button(terms_conditions, text='Continue', command=terms_conditions.destroy ,bg='gold', fg='blue', font=('times new Roman ', 15, 'bold') ,activebackground='blue', activeforeground='gold')
    btn_finish_reading.place(x=300, y=550)
    terms_conditions.mainloop()




# info_btn = PhotoImage(file='img/info.png')
Button(reg, text='Read Terms and Conditions', bd=0, font=("times new roman",12, "bold"), activebackground='gold', activeforeground=background, fg='gold', bg=background, command=TC, cursor='hand2').place(x=550,y=415)

var_chk = IntVar()
chk = Checkbutton(reg, variable=var_chk, text = 'I Agree to the Terms & Conditions ', onvalue=1, offvalue=0, bg=background, fg='red', font=("times new roman",12, "bold")).place(x=550, y=460)



################################# Sign Up Button


signup_btn = Button(reg, text='SIGN UP', command=registerUser, cursor='hand2', bg='green', fg='white', font=('Arial' ,15,'bold'),activebackground='gold', activeforeground='blue', width=15)
signup_btn.place(x=700, y=500)


########################################################### LOGIN

signin_label = Label(reg, text=" Already a Member ? ", bg=background, fg='white', font=('times new roman',10,'bold'), anchor='center').place(x=600, y=580)

def loginpage():
    reg.destroy()
    import login



to_login_btn = Button(reg, text='Click to Login', font=('times new roman', 12, 'bold') ,command=loginpage, border=0, cursor='hand2', fg='gold', bg=background, activebackground='gold', activeforeground='blue') #  fg='#deeefb',
to_login_btn.place(x=720, y=575)



# ================== Footer ================
lbl_footer = Label(reg, text=' Blessedera Techies - Heart Disease Prediction System | Developed by Omobuwa Blessed Adeoye (O.B.A.) \nFor any Technical Issue Contact: +2348132986310', font=("times new roman",11, "bold"),bg=background, fg="white").place(x=0, y=707, relwidth=1, height=30) # pack(side=BOTTOM, fill=X)



reg.mainloop()