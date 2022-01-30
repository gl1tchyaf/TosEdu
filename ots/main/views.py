from PIL import Image
from django.forms.widgets import Input
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse

from .models import usercanvas, questions

from django.contrib.auth.decorators import login_required

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

from django.core.mail import send_mail
from . import forms


@login_required(login_url="/accounts/login/")
def homepage(request):
    return render(request, 'main/homepage.html')


@login_required(login_url="/account/login/")
def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message-message']

        # send email
        send_mail( 
            'Mail Sent By ' + message_name,  # subject
            '\n' + 'Senders Phone: ' + message_phone + '\nSenders Email: ' + message_email + ' \nMessage: ' + message,
            # message
            message_email,  # from mail
            ['rashikbuksh71@gmail.com'],  # tomail
        )
        return render(request, 'main/contact.html', {'message_name': message_name})
    else:
        return render(request, 'main/contact.html')


@login_required(login_url="/account/login/")
def hotel_bookingPdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)
    logo = ImageReader('https://i.ibb.co/MPcBtHf/logo1.jpg')


    lines = [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",

        "                                     Welcome to Green Travel",
        " ",
        "                           Your Reservation confirmation is below",
        " ",
        " ",
        " ",
        "        Full name: ",
        " ",
        "        Email: " ,
        " ",
        "        Phone: " ,
        " ",
        "        Check-in date: " ,
        " ",
        "        Check-out date: " ,
        " ",
        "        Hotel name: " ,
        " ",
        "        Total number of rooms: " ,
        " ",
        "        Room type: " ,
        " ",
        " ",
        "",
        "                               Thank you for using Green Travel",
        "",
        "                               All right reserved by Green Travel",

    ]

    for line in lines:
        textob.textLine(line)

    c.drawImage(logo, 170, 10, mask='auto', anchor='c')
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='room.pdf')


@login_required(login_url="/account/login/")
def classAndSubjects(request):
    classAndSubjects.classInput = ""
    classAndSubjects.subjectInput = ""
    classAndSubjects.classInput = request.POST.get('class-Input')
    classAndSubjects.subjectInput = request.POST.get('subject-Input')
    return render(request, 'main/classAndSubjects.html')


@login_required(login_url="/account/login/")
def Canvas(request):
    canvass = usercanvas.objects.all()
    context = {'canvass': canvass}
    return render(request, "main/canvas.html", context)


@login_required(login_url="/account/login/")
def removequestion(request, pk):
    instance = usercanvas.objects.get(id=pk)
    instance.delete()
    return redirect('articles:canvas')


@login_required(login_url="/account/login/")
def questionsss(request):
    questionss = questions.objects.all()
    context = {'questionss': questionss, 'classinput': int(classAndSubjects.classInput), 'subjectinput': classAndSubjects.subjectInput}
    return render(request, 'main/questionAdd.html', context)


@login_required(login_url="/account/login/")
def addquestion(request, pk):
    instance = questions.objects.get(id=pk)
    instance2 = usercanvas.objects.create(user=request.user, questions=instance)
    instance2.save()
    return redirect('articles:canvas')
