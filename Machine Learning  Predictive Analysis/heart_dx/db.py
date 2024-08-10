import mysql.connector # pip install mysql-connector-python
# import pymysql
from tkinter import messagebox




def save_Data_Mysql( name,today_date, birth_year, age, sex,fbs, xan, cpC, recg,
                    slp, caC, tha, rbp, cho,thc, opk, prediction):
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='0000'
        )
        mycursor = mydb.cursor()

    except:
        messagebox.showerror("Connection", "Database Connection Establishement was Unsuccessful")

    try:
    #    a =  command ='drop database heart_data'
    #    mycursor.execute(a)
    #    print('Database Dropped')
       command ='create database heart_data'
       mycursor.execute(command)

       command = 'use heart_data'
       mycursor.execute(command)

       command1 = 'CREATE TABLE IF NOT EXISTS data(user int auto_increment key not null, Name varchar(100), Date varchar(50), DOB varchar(50),age varchar(50), gender varchar(50),fasting_blood_sugar varchar(50), exang varchar(50), Chest_Pain varchar(50), restecg varchar(50), slope varchar(50), number_of_major_vessels varchar(50), thalassemia varchar(50), resting_blood_pressure varchar(50),serum_cholestoral varchar(50), maximum_heart_rate varchar(50),ST_depression_induced_by_exercise_relative_to_rest varchar(50), Outcome varchar(50))'
       mycursor.execute(command1)
       signupcommand = 'CREATE TABLE IF NOT EXISTS userlogin(user int auto_increment key not null, first_name varchar(100), last_name varchar(100), Contact varchar(15), Email varchar(50), Question varchar(100), Answer varchar(100), Username varchar(100), Password varchar(100))'
       mycursor.execute(signupcommand)

       command2 = 'INSERT INTO data(Name,Date,DOB,age,gender,fasting_blood_sugar,exang,Chest_Pain,restecg,slope,number_of_major_vessels,thalassemia,resting_blood_pressure,serum_cholestoral,maximum_heart_rate,ST_depression_induced_by_exercise_relative_to_rest,Outcome) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'  # CpCombo,RestecgCombo,SlopeCombo,CaCombo,ThalCombo,trestbps,chol,thalach,oldpeak,prediction
       val = (name,today_date, birth_year, age, sex,fbs, xan, cpC, recg,
                    slp, caC, tha, rbp, cho,thc, opk, prediction)
       mycursor.execute(command2, val)
       mydb.commit()
       mydb.close()
       messagebox.showinfo("Success", "Database Stored Data")
    except:    
             # Incase Db already Existed
        mycursor.execute('use heart_data')
        mydb = mysql.connector.connect(host='localhost', user='root', password='0000', database='heart_data')
        mycursor=mydb.cursor()
        command2 = 'INSERT INTO data(Name,Date,DOB,age,gender,fasting_blood_sugar,exang,Chest_Pain,restecg,slope,number_of_major_vessels,thalassemia,resting_blood_pressure,serum_cholestoral,maximum_heart_rate,ST_depression_induced_by_exercise_relative_to_rest,Outcome) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'  # CpCombo,RestecgCombo,SlopeCombo,CaCombo,ThalCombo,trestbps,chol,thalach,oldpeak,prediction
        val = (name,today_date, birth_year, age, sex,fbs, xan, cpC, recg,
                    slp, caC, tha, rbp, cho,thc, opk, prediction)
        mycursor.execute(command2, val)
        mydb.commit()
        mydb.close()
        messagebox.showinfo("Success", "User Data Stored ")
