from django.contrib import admin
from .models import User
from .models import Project
# Register your models here.
admin.site.register(User)
admin.site.register(Project)