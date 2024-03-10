from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import mysql.connector as msc
import json

def filterAll(request):
    filter1 = request.GET.get('filt1','0')
    filter2 = request.GET.get('filt2','0')
    filter3 = request.GET.get('filt3','0')
    if filter2!='all':
        a = int(filter2)
        b = int(filter2)-5
        filter2 = str(b) + ":" + str(a)
    if filter3!='all':
        a = int(filter3)
        b = int(filter3)-1000
        filter3 = str(b) + ":" + str(a)

    data = {"address":"student","filt1": filter1,
                "filt2": filter2,
                "filt3": filter3}
    return render(request,"ResultPage.html",data)



def idMatchStudent(request):
    email = request.GET.get('emailAdd','0')
    passw = request.GET.get('passUsr','0')
    print(email,passw)
    mydb = msc.connect(host="localhost",user='root',password='Haigure#369$07',database='onlinelearn')
    cursor = mydb.cursor()
    s = "SELECT email,password_student FROM studentinfo"
    cursor.execute(s)
    res = cursor.fetchall()
    for a in res:
        print(a)
        if email==a[0] and passw==a[1]:
            
            param = {"address":"student","filt1": "all",
                "filt2": "all",
                "filt3": "all"}
            return render(request,"ResultPage.html",param)
    data = {"message":"Wrong Password or email"}
    return render(request,"SignIn.html",data)

def idMatchTeacher(request):
    email = request.GET.get('emailAdd','0')
    passw = request.GET.get('passUsr','0')
    
    mydb = msc.connect(host="localhost",user='root',password='Haigure#369$07',database='onlinelearn')
    cursor = mydb.cursor()
    s = "SELECT email,password_teacher FROM teacherinfo"
    cursor.execute(s)
    res = cursor.fetchall()
    for a in res:
        if email==a[0] and passw==a[1]:
            param = {"address":"teacher"}
            return render(request,"ResultPage.html",param)
    data = {"message":"Wrong Password or email"}
    return render(request,"SignIn.html",data)

     


def studentAuth(request):
    # Sign Up process
    userName = request.GET.get('usrName','0')
    email = request.GET.get('emailAdd','0')
    passw = request.GET.get('passUsr','0')
    mob = request.GET.get('Usrmob','0')
    
    mydb = msc.connect(host="localhost",user='root',password='Haigure#369$07',database='onlinelearn')
    cursor = mydb.cursor()
    s = "SELECT email FROM studentinfo"
    cursor.execute(s)
    res = cursor.fetchall()
    for a in res:
        if(email==a):
            params = {'result':'User Already Exist','address':'Student'}
            return render(request,'ResultPage.html',params)
    s1 = f"INSERT INTO studentinfo VALUES(%s,%s,%s,%s)"
    b1 = (userName,email,passw,mob)
    cursor.execute(s1,b1)
    mydb.commit()
    params = {'result':'Registration Successful','address':'Student'}
    return render(request,'ResultPage.html',params)

def teacherAuth(request):
    # Sign Up process
    userName = request.GET.get('usrName','0')
    email = request.GET.get('emailAdd','0')
    passw = request.GET.get('passUsr','0')
    mob = request.GET.get('Usrmob','0')
    age = request.GET.get('UsrAge','0')
    experiance = request.GET.get('UsrExp','0')
    language = request.GET.get('UsrLang','0')
    price = request.GET.get('UsrPrice','0')


    
    mydb = msc.connect(host="localhost",user='root',password='Haigure#369$07',database='onlinelearn')
    cursor = mydb.cursor()
    s = "SELECT email FROM teacherinfo"
    cursor.execute(s)
    res = cursor.fetchall()
    for a in res:
        if(email==a):
            params = {'result':'User Already Exist','address':'Teacher'}
            return render(request,'ResultPage.html',params)
    s1 = f"INSERT INTO teacherinfo VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    b1 = (userName,email,passw,mob,age,experiance,price,language)
    cursor.execute(s1,b1)
    mydb.commit()
    params = {'result':'Registration Successful','address':'Teacher'}
    return render(request,'ResultPage.html')

    

