from django.contrib import admin
from .models import User
from .models import Project
from .models import Slides


# replace with decorators
# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Slides)
