from django.conf.urls import url
from django.urls import path

from . import views


app_name = 'articles'


urlpatterns = [
    url(r'^$', views.homepage, name="list"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^classAndSubjects/$', views.classAndSubjects, name="classAndSubjects"),
    url(r'^canvas/$', views.Canvas, name="canvas"),
    url(r'^questions/$', views.questionsss, name="questions"),
    url(r'^questionsGenerate/$', views.questionsGenerate, name="questionsGenerate"),
    path('removequestion/<str:pk>/$', views.removequestion, name="removequestion"),
    path('removequestionSelective/<str:pk>/$', views.removequestionSelective, name="removequestionSelective"),
    path('editquestion/<str:pk>/$', views.editquestion, name="editquestion"),
    path('editquestionSelective/<str:pk>/$', views.editquestionSelective, name="editquestionSelective"),
    path('addquestion/<str:pk>/$', views.addquestion, name="addquestion"),
    path('addquestionSelective/<str:pk>/$', views.addquestionSelective, name="addquestionSelective"),
    url(r'^questioninput/$', views.questioninput, name="questioninput"),
    url(r'^bijoyinput/$', views.bijoyinput, name="bijoyinput"),
    url(r'^unicodeinput/$', views.unicodeinput, name="unicodeinput"),
    url(r'^unicodeinputSelective/$', views.unicodeinputSelective, name="unicodeinputSelective"),
    url(r'^bijoyinputSelective/$', views.bijoyinputSelective, name="bijoyinputSelective"),
    url(r'^userInfo/$', views.userInfo, name="userInfo"),

    url(r'^purchasePoint/$', views.purchasePoint, name="purchasePoint"),

    url(r'^user_profile/$', views.UserProfile, name="user_profile"),
    url(r'^create_profile/$', views.createProfile, name="create_profile"),

    path('openDocx/<str:pk>/$', views.openDocx, name="openDocx"),
    path('openEnglishDocx/<str:pk>/$', views.openEnglishDocx, name="openEnglishDocx"),
    url(r'^lessThanSix/$', views.lessThanSix, name="lessThanSix"),
    url(r'^englishQuestions/$', views.englishQuestions, name="englishQuestions"),
    url(r'^showDoc/$', views.showDoc, name="showDoc"),
    url(r'^showEnglishDoc/$', views.showEnglishDoc, name="showEnglishDoc"),
    url(r'^docQuestionPage/$', views.docQuestionPage, name="docQuestionPage"),
    url(r'^docEnglishQuestionPage/$', views.docEnglishQuestionPage, name="docEnglishQuestionPage"),
    url(r'^DocumentQuestionsForm/$', views.DocumentQuestionsform, name="DocumentQuestionsform"),
    url(r'^EnglishDocQuestionsForm/$', views.EnglishDocQuestionsform, name="EnglishDocQuestionsform"),

    url(r'^ClassSuggesstionForm/$', views.ClassSuggesstionform, name="ClassSuggesstionform"),
    url(r'^classSugesstionChoser/$', views.classSugesstionChoser, name="classSugesstionChoser"),
    url(r'^classsuggession/$', views.sugesstion_class, name="classsuggession"),

    url(r'^admitCardGenerator/$', views.admitCard, name="admitCard"),
    url(r'^admitCardGeneratorPage/$', views.admitCardGen, name="admitCardGen"),
]
