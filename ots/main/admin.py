from django.contrib import admin

from .models import questions, usercanvas, selectiveQuestion

admin.site.register(questions)
admin.site.register(usercanvas)
admin.site.register(selectiveQuestion)
