from django.http import HttpResponse
from django.shortcuts import render
from email.message import EmailMessage
import smtplib
import ssl
import mysql.connector as msc

def sendMail(request):
    sender = request.GET.get("emailAdd",'0')
    password = request.GET.get("passUsr",'0')
    subject = request.GET.get("title",'0')
    body = request.GET.get("Describ",'0')
    print(password)
    mydb = msc.connect(host="localhost", user='root', password='Haigure#369$07', database='onlinelearn')
    cursor = mydb.cursor()
    cursor.execute("SELECT email FROM studentinfo")
    receivers = [row[0] for row in cursor.fetchall()]

    context = ssl.create_default_context()

    for receiver in receivers:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = receiver
        em['Subject'] = subject
        em.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.send_message(em)

    return render(request, 'sendmail.html')
