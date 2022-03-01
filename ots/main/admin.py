from django.contrib import admin

from .models import questions, usercanvas, selectiveQuestion, usercanvasSelective, userInformation, paymentInformation, userProfile, docQuestions, class_suggesstion

admin.site.register(questions)
admin.site.register(usercanvas)
admin.site.register(selectiveQuestion)
admin.site.register(usercanvasSelective)
admin.site.register(userInformation)
admin.site.register(paymentInformation)
admin.site.register(userProfile)
admin.site.register(docQuestions)
admin.site.register(class_suggesstion)
