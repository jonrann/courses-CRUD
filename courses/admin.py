from django.contrib import admin

from .models import Course, Description, Comment

# Register your models here.
admin.site.register(Course)
admin.site.register(Description)
admin.site.register(Comment)