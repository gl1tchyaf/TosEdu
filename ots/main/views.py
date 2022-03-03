from datetime import date

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import usercanvas, questions, selectiveQuestion, usercanvasSelective, userInformation, userProfile, \
    docQuestions, english_docQuestions, class_suggesstion

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
    if classAndSubjects.classInput and classAndSubjects.subjectInput is not None:
        return redirect('articles:questions')
    return render(request, 'main/classAndSubjects.html')


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
    instance2 = usercanvasSelective.objects.create(user=request.user, scenario=instance.scenario,
                                                   ques_img=instance.ques_img,
                                                   q_a=instance.q_a, q_b=instance.q_b, q_c=instance.q_c,
                                                   q_d=instance.q_d)
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

    if UserProfile.bio is not None and UserProfile.bio != '':
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


import docx


@login_required(login_url="/account/login/")
def openDocx(request, pk):
    openDocx.docOpen = request.POST.get('doc-Open')
    if openDocx.docOpen is not None:
        return redirect('articles:docQuestionPage')
    docc = docQuestions.objects.get(id=pk)
    context = {}
    context['doc'] = docc
    doc = docx.Document(docc.docs)
    fullText = []
    for para in doc.paragraphs:
        convertedpara = bijoy2unicode(para.text)
        fullText.append(convertedpara)
    context = {'data': fullText}

    return render(request, 'main/openDocx.html', context)


@login_required(login_url="/account/login/")
def lessThanSix(request):
    lessThanSix.classInput = ""
    lessThanSix.subjectInput = ""
    lessThanSix.classInput = request.POST.get('class-Input')
    lessThanSix.subjectInput = request.POST.get('subject-Input')
    if lessThanSix.classInput and lessThanSix.subjectInput is not None:
        return redirect('articles:showDoc')
    return render(request, 'main/classAndSubjectlessThenSix.html')


@login_required(login_url="/account/login/")
def showDoc(request):
    qlist = docQuestions.objects.filter(classes=lessThanSix.classInput, subject=lessThanSix.subjectInput)
    context = {'qlist': qlist}
    return render(request, 'main/showDocQuestions.html', context)


@login_required(login_url="/account/login/")
def docQuestionPage(request):
    context = {'docOpen': openDocx.docOpen}
    return render(request, 'main/docQuestionPage.html', context)


@login_required(login_url="/account/login/")
def openEnglishDocx(request, pk):
    openEnglishDocx.docOpen = request.POST.get('doc-Open')
    if openEnglishDocx.docOpen is not None:
        return redirect('articles:docEnglishQuestionPage')
    docc = english_docQuestions.objects.get(id=pk)
    context = {}
    context['doc'] = docc
    doc = docx.Document(docc.docs)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    context = {'data': fullText}

    return render(request, 'main/openEnglishDocx.html', context)


@login_required(login_url="/account/login/")
def englishQuestions(request):
    englishQuestions.classInput = ""
    englishQuestions.paperInput = ""
    englishQuestions.classInput = request.POST.get('class-Input')
    englishQuestions.paperInput = request.POST.get('paper-Input')
    print(englishQuestions.paperInput)
    if englishQuestions.classInput and englishQuestions.paperInput is not None:
        return redirect('articles:showEnglishDoc')
    return render(request, 'main/englishQuestions.html')


@login_required(login_url="/account/login/")
def showEnglishDoc(request):
    qlist = english_docQuestions.objects.filter(classes=englishQuestions.classInput, paper=englishQuestions.paperInput)
    context = {'qlist': qlist}
    return render(request, 'main/showEnglishDocQuestions.html', context)


@login_required(login_url="/account/login/")
def docEnglishQuestionPage(request):
    context = {'docOpen': openEnglishDocx.docOpen}
    return render(request, 'main/docQuestionPage.html', context)


@login_required(login_url="/account/login/")
def sugesstion_class(request):
    today = date.today()
    print(today.weekday())
    month, day = today.month, today.day
    instance = class_suggesstion.objects.filter(classes=1)
    for i in instance:
        if i.date.month == month and i.date.day == day:
            print(i.bangla)
            print(i.english)
            print(i.math)
            print(i.science)
            print(i.social)
            print(i.islamReligion)
            print(i.hinduReligion)
            print(i.boudhuReligion)
            print(i.cristantianReligion)
            print(i.artsAndCrafts)
            print(i.physicalEducation)
            print(i.music)
            print(i.comment)
    return render(request, 'main/suggesstion_class.html')


@login_required(login_url="/account/login/")
@allowed_users(allowed_roles=['staff'])
def DocumentQuestionsform(request):
    form = forms.DocumentQuestions()
    if request.method == 'POST':
        form = forms.DocumentQuestions(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            url = reverse('articles:DocumentQuestionsform')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(url)
    return render(request, 'main/DocumentQuestionsForm.html', {'form': form})


@login_required(login_url="/account/login/")
@allowed_users(allowed_roles=['staff'])
def EnglishDocQuestionsform(request):
    form = forms.EnglishDocQuestions()
    if request.method == 'POST':
        form = forms.EnglishDocQuestions(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            url = reverse('articles:EnglishDocQuestionsform')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(url)
    return render(request, 'main/EnglishDocQuestionsForm.html', {'form': form})


@login_required(login_url="/account/login/")
@allowed_users(allowed_roles=['staff'])
def ClassSuggesstionform(request):
    form = forms.ClassSuggesstion()
    if request.method == 'POST':
        form = forms.ClassSuggesstion(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            url = reverse('articles:ClassSuggesstionform')
            next = request.POST.get('next', '/')
            return HttpResponseRedirect(url)
    return render(request, 'main/ClassSuggesstionForm.html', {'form': form})
