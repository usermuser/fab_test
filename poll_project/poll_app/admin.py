from django.contrib import admin

from .models import Poll, Question

# class PollAdmin(admin.ModelAdmin):
#     list_display = (,)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('short_text', 'poll')

admin.site.register(Poll)
admin.site.register(Question, QuestionAdmin)
