from tkinter import *



info_window =Tk()
info_window.title("Info")
info_window.geometry('700x600+450+100')

# Icon
icon_img = PhotoImage(file='img/info.png')
info_window.iconphoto(False, icon_img)


# Heading
Label(info_window, text='Information Related to Dataset',  font='roboto 17 bold').pack(padx=20, pady=20)


#Info
Label(info_window, text='i. age - age in years', font='arial 11').place(x=20, y=100)
Label(info_window, text='ii. sex - sex (1 = male; 0 = female)', font='arial 11').place(x=20, y=130)
Label(info_window, text='iii. cp - chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3 = asymptomatic)', font='arial 11').place(x=20, y=160)
Label(info_window, text='iv. trestbps - resting blood pressure (in mm Hg on admission to the hospital)', font='arial 11').place(x=20, y=190)
Label(info_window, text='v. chol - serum cholestoral in mg/dl', font='arial 11').place(x=20, y=220)
Label(info_window, text='vi. fbs - fasting blood sugar > 120 mg/dl (1 = true; 0 = false)', font='arial 11').place(x=20, y=250)
Label(info_window, text='vii. restecg - resting electrocardiographic results (0 = normal; 1 = having ST-T; 2 = hypertrophy)', font='arial 11').place(x=20, y=310)
Label(info_window, text='viii. thalach - maximum heart rate achieved', font='arial 11').place(x=20, y=340)
Label(info_window, text='ix. exang - exercise induced angina (1 = yes; 0 = no)', font='arial 11').place(x=20, y=370)
Label(info_window, text='x. oldpeak - ST depression induced by exercise relative to rest', font='arial 11').place(x=20, y=400)
Label(info_window, text='xi. slope - the slope of the peak exercise ST segment (0 = upsloping; 1 = flat; 2 = downsloping)', font='arial 11').place(x=20, y=430)
Label(info_window, text='xii. ca - number of major vessels (0-3) colored by flourosopy', font='arial 11').place(x=20, y=460)
Label(info_window, text='xiii. thal - 0 = normal; 1 = fixed defect; 2 = reversable defect', font='arial 11').place(x=20, y=490)
Label(info_window, text='xiv. ', font='arial 11').place(x=20, y=520)
Label(info_window, text='xv. ', font='arial 11').place(x=20, y=550)

info_window.mainloop()



