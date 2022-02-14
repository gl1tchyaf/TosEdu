from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import usercanvas, questions, selectiveQuestion, usercanvasSelective, userInformation, userProfile

from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
from .permission import allowed_users
from . import forms

from bijoytounicode import bijoy2unicode


@login_required(login_url="/accounts/login/")
# @allowed_users(allowed_roles=['staff'])
def homepage(request):
    try:
        user = userInformation.objects.get(user=request.user)
    except:
        return redirect('articles:userInfo')
    return render(request, 'main/homepage.html', {'user': user})


@login_required(login_url="/account/login/")
def userInfo(request):
    try:
        user = userInformation.objects.get(user=request.user)
        if user is not None:
            return redirect('articles:list')
    except:
        print("Stay here")
    form = forms.userInformation()
    if request.method == 'POST':
        form = forms.userInformation(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            url = reverse('articles:list')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(url)
    return render(request, 'main/updateInformation.html', {'form': form})


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
    canvass1 = usercanvasSelective.objects.filter(user=request.user)
    context = {'canvass': canvass, 'canvass1': canvass1}
    return render(request, "main/canvas.html", context)


@login_required(login_url="/account/login/")
def removequestion(request, pk):
    instance = usercanvas.objects.get(id=pk)
    instance.delete()
    return redirect('articles:canvas')


@login_required(login_url="/account/login/")
def removequestionSelective(request, pk):
    instance = usercanvasSelective.objects.get(id=pk)
    instance.delete()
    return redirect('articles:canvas')


@login_required(login_url="/account/login/")
def questionsss(request):
    questionss = questions.objects.filter(classes=int(classAndSubjects.classInput),
                                          subject=classAndSubjects.subjectInput)
    questionsSelective = selectiveQuestion.objects.filter(classes=int(classAndSubjects.classInput),
                                                          subject=classAndSubjects.subjectInput)
    context = {'questionss': questionss, 'questionsSelective': questionsSelective}
    return render(request, 'main/questionAdd.html', context)


@login_required(login_url="/account/login/")
def addquestion(request, pk):
    instance = questions.objects.get(id=pk)
    instance2 = usercanvas.objects.create(user=request.user, scenario=instance.scenario, ques_img=instance.ques_img,
                                          q_a=instance.q_a, q_b=instance.q_b, q_c=instance.q_c, q_d=instance.q_d)
    instance2.save()
    return redirect('articles:canvas')


@login_required(login_url="/account/login/")
def addquestionSelective(request, pk):
    instance = selectiveQuestion.objects.get(id=pk)
    instance2 = usercanvasSelective.objects.create(user=request.user, scenario=instance.scenario, ques_img=instance.ques_img,
                                          q_a=instance.q_a, q_b=instance.q_b, q_c=instance.q_c, q_d=instance.q_d)
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
def editquestionSelective(request, pk):
    instance = usercanvasSelective.objects.get(id=pk)
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
    userInfo = userInformation.objects.get(user=request.user)
    count = 0
    canvass = usercanvas.objects.filter(user=request.user)
    for i in canvass:
        count += 1
    canvassSelective = usercanvasSelective.objects.filter(user=request.user)
    for i in canvassSelective:
        count += 1
    print(count)
    if userInfo.point >= count:
        userInfo.point = userInfo.point - count
        userInfo.save()
    else:
        return redirect('articles:list')
    context = {'canvass': canvass, 'canvassSelective': canvassSelective}
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


@login_required(login_url="/account/login/")
@allowed_users(allowed_roles=['staff'])
def bijoyinputSelective(request):
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
    form = forms.questionInputBijoySelective()
    if request.method == 'POST':
        form = forms.questionInputBijoySelective(request.POST, request.FILES)
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
    return render(request, 'main/bijoySelective.html', {'form': form})


@login_required(login_url="/account/login/")
@allowed_users(allowed_roles=['staff'])
def unicodeinputSelective(request):
    form = forms.questionInputSelective()
    if request.method == 'POST':
        form = forms.questionInputSelective(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            url = reverse('articles:questioninput')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(url)
    return render(request, 'main/unicodeSelective.html', {'form': form})


@login_required(login_url="/account/login/")
def purchasePoint(request):
    form = forms.paymentInformation()
    if request.method == 'POST':
        form = forms.paymentInformation(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            url = reverse('articles:list')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(url)
    return render(request, 'main/PurchasePoint.html', {'form': form})


@login_required(login_url="/account/login/")
def updateUserProfile(request, pk):
    instance = userProfile.objects.get(id=pk)
    instance.save()
    updateUserProfile.primaryKey = pk
    return redirect('articles:user_profile')


@login_required(login_url="/account/login/")
def UserProfile(request):
    primaryKey = request.POST.get('primaryKey')
    if primaryKey is None:
        primaryKey = 1
    instance = userProfile.objects.get(id=primaryKey)
    UserProfile.user_name = request.POST.get('user_name')
    UserProfile.phone = request.POST.get('phone_number')
    UserProfile.address = request.POST.get('address')
    UserProfile.bio = request.POST.get('bio')
    UserProfile.image = request.FILES.get('image')

    if UserProfile.user_name is not None and UserProfile.user_name != '':
        instance.user_name = UserProfile.user_name

    if UserProfile.phone is not None and UserProfile.phone != '':
        instance.user_phone = UserProfile.phone

    if UserProfile.address is not None and UserProfile.address != '':
        instance.user_address = UserProfile.address

    if UserProfile.bio is not None and UserProfile.bio!= '':
        instance.bio = UserProfile.bio

    if UserProfile.image is not None:
        instance.user_image = UserProfile.image
    instance.save()

    profile = userProfile.objects.all()
    profile2 = userProfile.objects.filter(user=request.user).first()
    b = ''
    if profile2 is None:
        b = 'NoData'

    context = {}
    context['profile'] = profile
    context['booli'] = b
    context['name'] = UserProfile.user_name
    context['phone'] = UserProfile.phone
    context['address'] = UserProfile.address
    context['bio'] = UserProfile.bio
    context['image'] = UserProfile.image

    return render(request, 'main/user_profile.html', context)


@login_required(login_url="/account/login/")
def createProfile(request):
    form = forms.UserProfile()
    if request.method == 'POST':
        form = forms.UserProfile(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(next)
    else:
        form = forms.UserProfile()
    return render(request, 'main/createprofile.html', {'form': form})