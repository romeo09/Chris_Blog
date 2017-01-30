from django.shortcuts import render, redirect
from django.contrib import messages
from models import Blog, Comment

# Create your views here.
def index(request):
    context = {
        'blogs': Blog.objects.all(),
        "comments": Comment.objects.all(),
    }
    return render(request, 'chris.html', context)

def blogs(request):
    Blog.objects.create(blog = request.POST['blog'], title = request.POST['title'], author = request.POST['author'])
    return redirect('main_page')

def comments(request):
    Comment.objects.create(comment = request.POST['comment'], name = request.POST['name'])
    return redirect('main_page')
