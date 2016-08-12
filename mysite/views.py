from django.shortcuts import render
from django.utils import timezone
from django.db import models
#from .models import Post

# Create your views here.
def base(request):
   context = {}
   return render(request,'base.html', context)

def inicio(request):
   context = {}
   return render(request,'inicio.html', context)

def post_list(request):
 posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
 return render(request, 'post_list.html', {'posts': posts})                                                              
