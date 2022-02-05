from PIL import Image
from django.forms.widgets import Input
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.template.loader import get_template
from django.urls import reverse
from django.views import View

from .models import usercanvas, questions

from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from .permission import allowed_users
from . import forms

from bijoytounicode import bijoy2unicode


@login_required(login_url="/accounts/login/")
# @allowed_users(allowed_roles=['staff'])
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
def classAndSubjects(request):
    classAndSubjects.classInput = ""
    classAndSubjects.subjectInput = ""
    classAndSubjects.classInput = request.POST.get('class-Input')
    classAndSubjects.subjectInput = request.POST.get('subject-Input')
    context = {'classInput': classAndSubjects.classInput, 'subjectInput': classAndSubjects.subjectInput}
    return render(request, 'main/classAndSubjects.html', context)


@login_required(login_url="/account/login/")
def Canvas(request):
    canvass = usercanvas.objects.filter(user=request.user)
    context = {'canvass': canvass}
    return render(request, "main/canvas.html", context)


@login_required(login_url="/account/login/")
def removequestion(request, pk):
    instance = usercanvas.objects.get(id=pk)
    instance.delete()
    return redirect('articles:canvas')


@login_required(login_url="/account/login/")
def questionsss(request):
    questionss = questions.objects.filter(classes=int(classAndSubjects.classInput), subject=classAndSubjects.subjectInput)
    context = {'questionss': questionss}
    return render(request, 'main/questionAdd.html', context)


@login_required(login_url="/account/login/")
def addquestion(request, pk):
    instance = questions.objects.get(id=pk)
    instance2 = usercanvas.objects.create(user=request.user, scenario=instance.scenario, ques_img=instance.ques_img, q_a=instance.q_a, q_b=instance.q_b, q_c=instance.q_c, q_d=instance.q_d)
    instance2.save()
    return redirect('articles:canvas')


@login_required(login_url="/account/login/")
def editquestion(request, pk):
    instance = usercanvas.objects.get(id=pk)
    context = {}
    context['editCanvas'] = instance

    scenario = request.POST.get('canv-scenario')
    qa = request.POST.get('canv-qa')
    qb = request.POST.get('canv-qb')
    qc = request.POST.get('canv-qc')
    qd = request.POST.get('canv-qd')

    if scenario is not None and scenario != '':
        instance.scenario = scenario

    if qa is not None and qa != '':
        instance.q_a = qa

    if qb is not None and qb != '':
        instance.q_b = qb

    if qc is not None and qc != '':
        instance.q_c = qc

    if qd is not None and qd != '':
        instance.q_d = qd

    instance.save()
    return render(request, 'main/editQuestion.html', context)


@login_required(login_url="/account/login/")
def questionsGenerate(request):
    canvass = usercanvas.objects.filter(user=request.user)
    context = {'canvass': canvass}
    return render(request, 'main/QuestionGenerate.html', context)


@login_required(login_url="/account/login/")
@allowed_users(allowed_roles=['staff'])
def questioninput(request):
    return render(request, 'main/QuestionInput.html')


@login_required(login_url="/account/login/")
@allowed_users(allowed_roles=['staff'])
def bijoyinput(request):
    scenario = request.POST.get('scenario')
    qa = request.POST.get('qa')
    qb = request.POST.get('qb')
    qc = request.POST.get('qc')
    qd = request.POST.get('qd')
    if scenario is not None:
        convertedScenario = bijoy2unicode(scenario)
    if qa is not None:
        convertedqa = bijoy2unicode(qa)
    if qb is not None:
        convertedqb = bijoy2unicode(qb)
    if qc is not None:
        convertedqc = bijoy2unicode(qc)
    if qd is not None:
        convertedqd = bijoy2unicode(qd)
    form = forms.questionInputBijoy()
    if request.method == 'POST':
        form = forms.questionInputBijoy(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.scenario = convertedScenario
            instance.q_a = convertedqa
            instance.q_b = convertedqb
            instance.q_c = convertedqc
            instance.q_d = convertedqd
            instance.save()
            url = reverse('articles:questioninput')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(url)
    return render(request, 'main/bijoyquestions.html', {'form': form})


@login_required(login_url="/account/login/")
@allowed_users(allowed_roles=['staff'])
def unicodeinput(request):
    form = forms.questionInput()
    if request.method == 'POST':
        form = forms.questionInput(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            url = reverse('articles:questioninput')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(url)
    return render(request, 'main/unicodequestions.html', {'form': form})