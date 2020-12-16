from django.shortcuts import render
from .models import User, Project
from .forms import ProjectForm

posts = [
    {
        "title": "1 post",
        "text": "this is a 1st post text",
    },
    {
        "title": "2 post",
        "text": "this is a 2nd post text",
    },
    {
        "title": "3 post",
        "text": "this is a 3rd post text",
    },
]
test = [{"test": 123}]


def index(request):
    context = {"posts": posts, "test": test}
    return render(request, "tinder/index.html", context)


def account_profile(request, username=""):
    context = {
        "user": None,
    }
    if username:
        user = User.objects.get(username=username)
    else:
        user = request.user
    context["projects"] = user.projects.all()
    context["user"] = user
    return render(request, "tinder/profile.html", context)


def add_project(request):
    context = {"user": request.user}
    if request.method == "POST":
        context["form"] = ProjectForm(request.POST, request.FILES)
        if context["form"].is_valid():
            # todo: add proper validation
            project = Project()
            project.name = context["form"].cleaned_data.get("name")
            project.email = context["form"].cleaned_data.get("email")
            project.phone = context["form"].cleaned_data.get("phone")
            project.video = context["form"].cleaned_data.get("video")
            project.description = context["form"].cleaned_data.get("description")
            project.posted_by = request.user
            project.save()
    else:
        context["form"] = ProjectForm()

    return render(request, "tinder/project-add.html", context)