from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import os
from backend import *
from db import *



background = "#f0ddd3"
framebg = "#62a7ff"
framefg = "#fefbfb"

root = Tk()
today = date.today()
dformate = today.strftime(" %d:%m:%Y")
root.title(f'Welcome to Today {dformate} This is Heart Attack Prediction System Login | Designed by Blessedera GlowTechie  | omobuwa BLESSED ADEOYE   ')
root.geometry('1450x730+35+10')
root.resizable(0, 0)
root.config(bg=background)


# =========================== Analysis
def analysis():
    global prediction
    name = Name.get()
    D1 = Date.get()
    today = datetime.date.today()
    print(today)
    age = today.year - DOB.get()
    print(f'{age} Years Old')

    try:
        sex = gender()
    except:
        messagebox.showerror("Missing ", "Please select Gender")
        return
    print(f'the gender is {sex}')

    try:
        fbs = FBS()
    except:
        messagebox.showerror("Missing ", "Please select if fasting blood sugar > 120 mg/dl or not")
        return
    print(f'the Fasting Blood Sugar is {fbs}')

    try:
        xan = Exang()
    except:
        messagebox.showerror("Missing ", "Please select exercise induced angina or Not")
        return
    print(f' the exercise induced angina is {xan}')

    try:
        caC = int(CaCombo())
    except:
        messagebox.showerror("Missing ", "Please select number Coronary artery disease ")
        return
    print(f'the Coronary artery disease {caC}')

    try:
        cpC = int(CpCombo())
    except:
        messagebox.showerror("Missing ", "Please select chest pain type")
        return
    print(f' the chest pain type {cpC}')

    try:
        tha = int(ThalCombo())
    except:
        messagebox.showerror("Missing ", "Please select thalassemia")
        return
    print(f' the thalassemia is {tha}')

    try:
        slp = int(SlopeCombo())
    except:
        messagebox.showerror("Missing ", "Please select the slope of the peak exercise ST segment")
        return
    print(f' the slope of the peak exercise ST segment is {slp}')

    try:
        recg = int(RestecgCombo())
    except:
        messagebox.showerror("Missing ", "Please select resting electrocardiographic results")
        return
    print(f' the resting electrocardiographic results is {recg}')

    try:
        rbp = int(trestbps.get())
        print(f' the resting blood pressure is {rbp}')
        cho = int(chol.get())
        print(f' the serum cholestoral in mg/dl = {cho}')
        thc = int(thalach.get())
        print(f' the maximum heart rate achieved = {thc}')
        opk = float(oldpeak.get())
        print(f' the ST depression induced by exercise relative to rest {opk}')
    except:
        # except Exception as p:
        messagebox.showerror("Missing Data", "Few missing data Entry, Please complete it ")
        # messagebox.showerror('Error', p)
        return

    # First Graph

    first_graph = Figure(figsize=(4, 5), dpi=100)
    add = first_graph.add_subplot(111)
    add.plot(['Sex', 'Fbs', 'exang'], [sex, fbs, xan])
    canvas = FigureCanvasTkAgg(first_graph)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=BOTH, expand=True)
    canvas._tkcanvas.place(width=208, height=208, x=650, y=270)

    # Second graph

    second_graph = Figure(figsize=(5, 5), dpi=100)
    add2 = second_graph.add_subplot(111)
    add2.plot(['age', 'trestbps', 'chol', 'thalach'], [age, rbp, cho, thc])
    canvas2 = FigureCanvasTkAgg(second_graph)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM, fill=BOTH, expand=True)
    canvas2._tkcanvas.place(width=208, height=208, x=870, y=270)

    # Third graph

    third_graph = Figure(figsize=(5, 5), dpi=100)
    add3 = third_graph.add_subplot(111)
    add3.plot(['oldpeak', 'restecg', 'cp'], [opk, recg, cpC])
    canvas3 = FigureCanvasTkAgg(third_graph)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM, fill=BOTH, expand=True)
    canvas3._tkcanvas.place(width=208, height=208, x=650, y=490)

    # Fourth graph

    fourth_graph = Figure(figsize=(5, 5), dpi=100)
    add4 = fourth_graph.add_subplot(111)
    add4.plot(['slope', 'ca', 'thal'], [slp, caC, tha])
    canvas4 = FigureCanvasTkAgg(fourth_graph)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM, fill=BOTH, expand=True)
    canvas4._tkcanvas.place(width=208, height=208, x=870, y=490)

    # Inputting Data
    input_data = (age, sex, cpC, rbp, cho, fbs, recg, thc, xan, opk, slp, caC, tha)

    input_data_as_numpy_array = np.asanyarray(input_data)

    # Reshaping d numpy to predict for only on instance
    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)
    prediction = model.predict(input_data_reshape)
    print(prediction[0])

    if (prediction[0] == 0):
        print("The Person does not have a Heart Disease")
        report.config(text=f'Report (0)', fg='#8dc63f')
        report1.config(text=f'{name} \n does not have a\n Heart Disease', fg='green')

    else:
        print("The Person has Heart Disease")
        report.config(text=f'Report (1)', fg='#ed1c24')
        report1.config(text=f'{name} \n You have a Heart\n Disease', fg='blue')


################### Information Window (Controlled by info_btn) ###########################
def info():
    info_window = Toplevel(root)
    info_window.title("Info")
    info_window.geometry('700x600+450+100')

    # Icon
    icon_img = PhotoImage(file='img/info.png')
    info_window.iconphoto(False, icon_img)

    # Heading
    Label(info_window, text='Information Related to Dataset', font='roboto 17 bold').pack(padx=20, pady=20)

    #Info
    Label(info_window, text='i. age - age in years', font='arial 11').place(x=20, y=100)
    Label(info_window, text='ii. sex - sex (1 = male; 0 = female)', font='arial 11').place(x=20, y=130)
    Label(info_window,text='iii. cp - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)',font='arial 11').place(x=20, y=160)
    Label(info_window, text='iv. trestbps - resting blood pressure (in mm Hg on admission to the hospital)',font='arial 11').place(x=20, y=190)
    Label(info_window, text='v. chol - serum cholestoral in mg/dl', font='arial 11').place(x=20, y=220)
    Label(info_window, text='vi. fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)', font='arial 11').place(x=20, y=250)
    Label(info_window, text='vii. restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)',font='arial 11').place(x=20, y=280)
    Label(info_window, text='viii. thalach - maximum heart rate achieved', font='arial 11').place(x=20, y=310)
    Label(info_window, text='ix. exang - exercise induced angina (1 = yes; 0 = no)', font='arial 11').place(x=20, y=340)
    Label(info_window, text='x. oldpeak - ST depression induced by exercise relative to rest', font='arial 11').place(x=20, y=370)
    Label(info_window,
          text='xi. slope - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)',font='arial 11').place(x=20, y=400)
    Label(info_window, text='xii. ca - number of major vessels (0-3) colored by flourosopy', font='arial 11').place(x=20, y=430)
    Label(info_window, text='xiii. thal - 0 = normal; 1 = fixed defect; 2 = reversable defect', font='arial 11').place(x=20, y=460)
    Label(info_window, text='xiv. ', font='arial 11').place(x=20, y=490)
    Label(info_window, text='xv. ', font='arial 11').place(x=20, y=510)

    info_window.mainloop()


# ============= Logout
def logout():
    root.destroy()
    import login


# ================== Save Function helps us to save all entry field at once
def SavE():
    name = Name.get()
    today_date = Date.get()
    birth_year = DOB.get()

    today = datetime.date.today()
    age = today.year - DOB.get()

    try:
        sex = gender()
    except:
        messagebox.showerror('Missing Data', "Please Select Gender")
    try:
        fbs = FBS()
    except:
        messagebox.showerror('Missing Data', "Please Select fbs")

    try:
         xan = Exang()
    except:
        messagebox.showerror("Missing ", "Please select exercise induced angina or Not")
        
    try:
        cpC = int(CpCombo())
    except:
        messagebox.showerror("Missing ", "Please select chest pain type")

    try:
        recg = int(RestecgCombo())
    except:
        messagebox.showerror("Missing ", "Please select resting electrocardiographic results")

    try:
        slp = int(SlopeCombo())
    except:
        messagebox.showerror("Missing ", "Please select the slope of the peak exercise ST segment")
        
    try:
         caC = int(CaCombo())
    except:
        messagebox.showerror("Missing ", "Please select number Coronary artery disease ")
        
    try:
         tha = int(ThalCombo())
    except:
        messagebox.showerror("Missing ", "Please select thalassemia")

    rbp = int(trestbps.get())
    cho = int(chol.get())
    thc = int(thalach.get()) 
    opk = float(oldpeak.get())
    save_Data_Mysql(name,today_date, birth_year, int(age), int(sex), int(fbs), int(xan), int(cpC), int(recg),
                    int(slp), int(caC), int(tha), int(rbp), int(cho), int(thc), float(opk),int(prediction[0]))
    messagebox.showinfo("Success", "User data Stored ")  
    Clear()
    os.system('a.py')


# ================== Clear Function helps us to clear all entry field at once
def Clear():
    Name.set('')
    DOB.set('')
    Registration.set('')
    trestbps.set('')
    chol.set('')
    thalach.set('')
    oldpeak.set('')


##################################################################

#============================ICON=========================== 1
icon = PhotoImage(file='img/icon.png')
root.iconphoto(False, icon)

#============================HEADER SECTION=========================== 2
logo = PhotoImage(file='img/head.png')
myimage = Label(image=logo, bg=background)
myimage.place(x=0, y=0)

#============================HEADING FRAME=========================== 3

Left = Frame(root, width=800, height=210, bg='lightgreen') 
Left.place(x=650, y=0)

Label(Left, text='Registration Number', font='arial 13 bold', bg='lightgreen', fg=framebg).place(x=100, y=0)
Label(Left, text='Date', font='arial 13 bold', bg='lightgreen', fg=framebg).place(x=510, y=0)
Label(Left, text='Patient Name   ', font='arial 13 bold', bg='lightgreen', fg=framebg).place(x=100, y=90)
Label(Left, text='Birth Year', font='arial 13 bold', bg='lightgreen', fg=framebg).place(x=510, y=90)

Entry_image = PhotoImage(file='img/Rounded Rectangle 1.png')
Entry_image2 = PhotoImage(file='img/Rounded Rectangle 2.png')

Label(Left, image=Entry_image, bg='#df2d4b').place(x=0, y=25)
Label(Left, image=Entry_image, bg='#df2d4b').place(x=370, y=25)

Label(Left, image=Entry_image2, bg='#df2d4b').place(x=0, y=115)
Label(Left, image=Entry_image2, bg='#df2d4b').place(x=370, y=115)

Registration = StringVar()
reg_entry = Entry(Left, textvariable=Registration, width=28, font='arial 15', bg='#0e5363', fg='#fff', bd=5)
reg_entry.place(x=10, y=32)

Date = StringVar()
today = date.today()
d1 = today.strftime(" %d/%m/%Y")
date_entry = Entry(Left, textvariable=Date, width=15, font='arial 15', bg='#0e5363', fg='white', bd=5)
date_entry.place(x=450, y=32)
Date.set(d1)

Name = StringVar()
name_entry = Entry(Left, textvariable=Name, width=28, font='arial 15', bg='#ededed', fg='#222222', bd=5)
name_entry.place(x=10, y=125)

DOB = IntVar()
dob_entry = Entry(Left, textvariable=DOB, width=28, font='arial 15', bg='#ededed', fg='#222222', bd=5)
dob_entry.place(x=380, y=125)

# ================================================Body ============================================== 4
Detail_entry = Frame(root, width=490, height=260, bg=framebg, bd=2)
Detail_entry.place(x=5, y=425)


#==============================Radio Button ========================== 5
# ======= Radio Functions +==========

def gender():
    if gen.get() == 1:
        Gender = '1'
        return (Gender)
        

    elif gen.get():
        Gender = '0'
        return (Gender)
    else:
        print(Gender)


def FBS():
    if fbs.get() == 1:
        Fbs = 1
        return (Fbs)
        print(Fbs)

    elif fbs.get():
        Fbs = 0
        return (Fbs)
        print(Fbs)
    else:
        print(Fbs)


def Exang():
    if exang.get() == 1:
        ExanG = '1'
        return (ExanG)
        print(ExanG)

    elif exang.get():
        ExanG = '0'
        return (ExanG)
        print(ExanG)
    else:
        print(ExanG)


###################
Label(Detail_entry, text='Sex:', font='arial 13 bold', bg='magenta', fg='white').place(x=7, y=10)


# Gender
gen = IntVar()
gender_radio_male = Radiobutton(Detail_entry, text='Male', variable=gen, value=1, command=gender)
gender_radio_male.place(x=45, y=10)
gender_radio_female = Radiobutton(Detail_entry, text='Female', variable=gen, value=2, command=gender)
gender_radio_female.place(x=101, y=10)

# Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false) ==  (fbs)
Label(Detail_entry, text='fbs:', font='arial 13 bold', bg='magenta', fg='white').place(x=175, y=10)
fbs = IntVar()
fbs_radio_true = Radiobutton(Detail_entry, text='True', variable=fbs, value=1, command=FBS)
fbs_radio_true.place(x=210, y=10)
fbs_radio_false = Radiobutton(Detail_entry, text='False', variable=fbs, value=2, command=FBS)
fbs_radio_false.place(x=263, y=10)

#  exercise induced angina (exang {1 = yes; 0 = no})
Label(Detail_entry, text='exang:', font='arial 13 bold', bg='magenta', fg='white').place(x=325, y=10)
exang = IntVar()
exang_radio_yes = Radiobutton(Detail_entry, text='Yes', variable=exang, value=1, command=Exang)
exang_radio_yes.place(x=380, y=10)
exang_radio_no = Radiobutton(Detail_entry, text='No', variable=exang, value=2, command=Exang)
exang_radio_no.place(x=427, y=10)


# ============================ ComboBox ============================6

# Functions

def CpCombo():
    input = cp_combobox.get()
    if input == '0 = typical angina':
        return (0)
    elif input == '1 = atypical angina':
        return (1)

    elif input == '2 = non-anginal pain':
        return (2)

    elif input == '3 = asymptomatic':
        return (3)
    else:
        print(input)


def SlopeCombo():
    input = slope_combobox.get()
    if input == '0 = upsloping':
        return (0)
    elif input == '1 = flat':
        return (1)

    elif input == '2 = downsloping':
        return (2)
    else:
        print(input)


def CaCombo():
    input = ca_combobox.get()
    if input == '0':
        return (0)
    elif input == '1':
        return (1)

    elif input == '2':
        return (2)

    elif input == '3':
        return (3)
    elif input == '4':
        return (4)
    else:
        print(input)


def ThalCombo():
    input = thal_combobox.get()
    if input == '0 = normal':
        return (0)
    elif input == '1 = fixed defect':
        return (1)

    elif input == '2 = reversable defect':
        return (2)
    else:
        print(input)


def RestecgCombo():
    input = restecg_combobox.get()
    if input == '0 = normal':
        return (0)
    elif input == '1 = having ST-T':
        return (1)

    elif input == '2 = hypertrophy':
        return (2)
    else:
        print(input)


# number of major vessels (0-3) colored by flourosopy
Label(Detail_entry, text='ca', font='arial 13 bold', bg='magenta', fg='white').place(x=10, y=50)
ca_combobox = Combobox(Detail_entry, values=['0', '1', '2', '3', '4'], font='arial 11', state='r', width=16)
ca_combobox.place(x=50, y=50)

# chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)
Label(Detail_entry, text='cp', font='arial 13 bold', bg='magenta', fg='white').place(x=10, y=90)
cp_combobox = Combobox(Detail_entry,
                       values=['0 = typical angina', '1 = atypical angina', '2 = non-anginal pain', '3 = asymptomatic'],
                       font='arial 11', state='r', width=16)
cp_combobox.place(x=50, y=90)

# thal - 0 = normal; 1 = fixed defect; 2 = reversable defect
Label(Detail_entry, text='thal', font='arial 13 bold', bg='magenta', fg='white').place(x=10, y=130)
thal_combobox = Combobox(Detail_entry, values=['0 = normal', '1 = fixed defect', '2 = reversable defect'],
                         font='arial 10', state='r', width=18)
thal_combobox.place(x=50, y=130)

# the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)
Label(Detail_entry, text='slope', font='arial 13 bold', bg='magenta', fg='white').place(x=10, y=170)
slope_combobox = Combobox(Detail_entry, values=['0 = upsloping', '1 = flat', '2 = downsloping'], font='arial 12',
                          state='r', width=13)
slope_combobox.place(x=60, y=170)

#restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)
Label(Detail_entry, text='restecg', font='arial 13 bold', bg='magenta', fg='white').place(x=10, y=210)
restecg_combobox = Combobox(Detail_entry, values=['0 = normal', '1 = having ST-T', '2 = hypertrophy'], font='arial 10',
                            state='r', width=14)
restecg_combobox.place(x=80, y=210)

# ======================= Data Entry Box ==========================

trestbps = StringVar()
chol = StringVar()
thalach = StringVar()
oldpeak = StringVar()

Label(Detail_entry, text='smoking:', font='arial 13 bold', width=7, bg=framebg, fg=framefg).place(x=220, y=50)

Label(Detail_entry, text='trestbps:', font='arial 13 bold', width=7, bg=framebg, fg=framefg).place(x=220, y=80)
trestbps_entry = Entry(Detail_entry, textvariable=trestbps, width=15, font='arial 13 bold', bg='#ededed', fg='#222222',
                       bd=5)
trestbps_entry.place(x=290, y=80)

Label(Detail_entry, text='chol:', font='arial 13 bold', width=7, bg=framebg, fg=framefg).place(x=220, y=110)
chol_entry = Entry(Detail_entry, textvariable=chol, width=15, font='arial 13 bold', bg='#ededed', fg='#222222', bd=5)
chol_entry.place(x=290, y=110)

Label(Detail_entry, text='thalach:', font='arial 13 bold', width=7, bg=framebg, fg=framefg).place(x=220, y=140)
thalach_entry = Entry(Detail_entry, textvariable=thalach, width=15, font='arial 13 bold', bg='#ededed', fg='#222222',
                      bd=5)
thalach_entry.place(x=290, y=140)

Label(Detail_entry, text='oldpeak:', font='arial 13 bold', width=7, bg=framebg, fg=framefg).place(x=220, y=170)
oldpeak_entry = Entry(Detail_entry, textvariable=oldpeak, width=15, font='arial 13 bold', bg='#ededed', fg='#222222',
                      bd=5)
oldpeak_entry.place(x=290, y=170)

#######################################################################################

############# ========= Report ######################################## 8
square_report_image = PhotoImage(file='img/report.png')
report_bg = Label(image=square_report_image, bg=background)
report_bg.place(x=1110, y=300)

report = Label(root, font='arial 20 bold', bg='white', fg='#8dc63f')
report.place(x=1150, y=510)

report1 = Label(root, font='arial 10 bold', bg='white')
report1.place(x=1160, y=610)

#######################################################################

# ======================  Graph ======================= 9
graph_img = PhotoImage(file='img/graph.png')
# Label(image=graph_img).place(x=650, y=270)
# Label(image=graph_img).place(x=870, y=270)
# Label(image=graph_img).place(x=650, y=490)
# Label(image=graph_img).place(x=870, y=490)

#######################################################################

# ======================  Buttons ======================= 10

# =============== Analysis Button =================
analysis_btn = PhotoImage(file='img/analysis.png')
Button(root, image=analysis_btn, bd=0, activebackground=background, bg=background, cursor='hand2', command=analysis).place(x=1130, y=220)

# =============== Info Button =================
info_btn = PhotoImage(file='img/info.png')
Button(root, image=info_btn, bd=0, activebackground=background, bg=background, command=info, cursor='hand2').place(x=10,y=380)

# =============== Save Button =================
save_btn = PhotoImage(file='img/save.png')
Button(root, image=save_btn, bd=0, activebackground=background, bg=background, cursor='hand2', command=SavE).place(x=1370, y=230)

#######################################################################

# ====================== Smoking and Not Smoking  Buttons ======================= 11
button_mode = True
choice = 'smoking'


def changemode():
    global button_mode
    global choice

    if button_mode:
        choice = 'not_smoking'
        mode.config(image=not_smoking_img)
        button_mode = False

    else:
        choice = 'smoking'
        mode.config(image=smoking_img)
        button_mode = True

    print(choice)


smoking_img = PhotoImage(file='img/smoker.png')
not_smoking_img = PhotoImage(file='img/not-smoker.png')
mode = Button(root, image=smoking_img, command=changemode, bg=framebg, bd=0, activebackground=framebg, cursor='hand2')
mode.place(x=310, y=470)

# ====================== Logout Button ======================= 12
logout_img = PhotoImage(file='img/logout.png')
logout_btn = Button(root, image=logout_img, bg='lightgreen', activebackground='lightgreen', cursor='hand2', bd=0,command=logout)
logout_btn.place(x=1390, y=60)

#=====================================#########################

# ================== Footer ================
lbl_footer = Label(root, text=' Blessedera Techies - Heart Disease Prediction System | Developed by Omobuwa Blessed Adeoye (O.B.A.) \nFor any Technical Issue Contact: +2348132986310', font=("times new roman",11, "bold"),bg=background, fg="#00264d").place(x=0, y=690, relwidth=1, height=30) # pack(side=BOTTOM, fill=X)




root.mainloop()
