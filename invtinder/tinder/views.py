from django.http import HttpResponse
from django.shortcuts import render


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
