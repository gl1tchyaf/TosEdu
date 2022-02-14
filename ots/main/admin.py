from django.contrib import admin

from .models import questions, usercanvas, selectiveQuestion, usercanvasSelective, userInformation, paymentInformation, userProfile

admin.site.register(questions)
admin.site.register(usercanvas)
admin.site.register(selectiveQuestion)
admin.site.register(usercanvasSelective)
admin.site.register(userInformation)
admin.site.register(paymentInformation)
admin.site.register(userProfile)
