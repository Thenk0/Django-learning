from django.contrib import admin
from .models import User
from .models import Project
from .models import Slides
from .models import ChoiceList


class ChoiceInLine(admin.TabularInline):
    model = ChoiceList
    extra = 1


# replace with decorators
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (ChoiceInLine,)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (ChoiceInLine,)


@admin.register(Slides)
class SlidesAdmin(admin.ModelAdmin):
    pass
