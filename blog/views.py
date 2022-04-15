from django.shortcuts import render
from .models import Post
from events.models import Event

# Create your views here.
def showblog(request):
    posts = Post.objects
    events = Event.objects
    return render(request, 'blog/blog.html',{'posts': posts,'events':events})