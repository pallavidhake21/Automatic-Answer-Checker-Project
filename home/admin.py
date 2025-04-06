from django.contrib import admin
from .models import Exam,Answer,Registration


# Register your models here
class Examadmin(admin.ModelAdmin):
        list_display = ['id','Question','Option1','Option2','Option3','Option4','Corrans']
admin.site.register(Exam, Examadmin)

class AnswerAdmin(admin.ModelAdmin):
        list_display = ['id', 'ans']
admin.site.register(Answer,AnswerAdmin)

admin.site.register(Registration)