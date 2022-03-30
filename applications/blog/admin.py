from django.contrib import admin

from applications.blog.models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)

