from django.contrib import admin

from .models import Choice, Question, Assignment, GradedAssignment, Deadline

admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(Deadline)
admin.site.register(Assignment)
admin.site.register(GradedAssignment)
