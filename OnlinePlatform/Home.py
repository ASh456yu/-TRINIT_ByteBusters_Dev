from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import mysql.connector as msc
from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from django.core.serializers import serialize

def mailPage(request):
    return render(request,'sendmail.html')


def homePage(request):
    params = {'message':'None'}
    return render(request, 'StuOrTeach.html',params)

def SignIn(request):
    user = request.GET.get('user')
    if(user=='student'):
        params = {'address':'Student'}
        return render(request,'SignIn.html',params)
    elif(user=='teacher'):
        params = {'address':'Teacher'}
        return render(request,'SignIn.html',params)


from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def your_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        print("hanji")
        json_string = json.dumps(data)
        with open('data.txt', 'w') as file:
            file.write(json_string)
        return JsonResponse({'status': 'success', 'data': data})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)

def retrive(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        print("hanji1")
        with open("data.txt", "r") as file:
            # Read the entire contents of the file
            file_contents = file.read()
        print(type(file_contents))
        dictionary_from_json = json.loads(file_contents)

        print(type(dictionary_from_json))
        return JsonResponse({'status': 'success', 'data': dictionary_from_json})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def SignUp(request):
    user = request.GET.get('user')
    if(user=='Student'):
        params = {'address':'Student'}
        return render(request,'SignUp.html',params)
    elif(user=='Teacher'):
        params = {'address':'Teacher'}
        return render(request,'SignUp.html',params)


def showTeacherProfile(request):
    teacher = request.GET.get('user')
    mydb = msc.connect(host="localhost",user='root',password='Haigure#369$07',database='onlinelearn')
    cursor = mydb.cursor()
    s = f"SELECT * FROM teacherinfo WHERE Teacher_name = '{teacher}'"
    cursor.execute(s)
    res = cursor.fetchone()
    s = f"SELECT * FROM teacherprofile WHERE Teacher_name = '{teacher}'"
    cursor.execute(s)
    pes = cursor.fetchone()
    params = {'name':teacher,'age':res[4],'email':res[1],'lang':res[7],'mob':res[3],'exp':pes[5],'price':pes[4]}
    return render(request,'TeachetProfile.html',params)




def get_data(request):
    mydb = msc.connect(host="localhost",user='root',password='Haigure#369$07',database='onlinelearn')
    cursor = mydb.cursor()
    s = "SELECT * FROM teacherprofile"
    cursor.execute(s)
    res = cursor.fetchall()
    param = []
    for dat in res:
        info = {'name':dat[0],
                'vid':dat[1],
                'duration':dat[2],
                'lan':dat[3],
                'price':dat[4],
                'experiance':dat[5],
                'videoID':dat[6]
                }
        param.append(info)
    return JsonResponse(param,safe=False)



def showPaymentPage(request):
    # videoId = request.GET.get('pay','0')
    # mydb = msc.connect(host="localhost",user='root',password='Haigure#369$07',database='onlinelearn')
    # cursor = mydb.cursor()
    # s = f"SELECT * FROM teacherprofile WHERE videoID = {videoId}"
    # cursor.execute(s)
    # pes = cursor.fetchone()
    # a = int(pes[6])
    # b = a - 84
    # params = {'price1':pes[6],'price2':str(b)}
    return render(request,'Payment.html')






