from django.shortcuts import render
from django.http import HttpResponse
from blog import models


def hello_world(request):
    return HttpResponse('Hallo meine Freunde!')


def blog_all(request):
    post = models.Post.objects.all()
    return render(request, 'post_list.html', {'post': post})
