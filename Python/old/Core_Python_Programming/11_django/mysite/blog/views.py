from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import BlogPost

from datetime import datetime
# Create your views here.


# def archive(request):
#     post = BlogPost(title='mocktitle', body='mockbody', timestamp=datetime.now())
#     return render_to_response('archive.html', {'posts': [post]})

def archive(request):
    posts = BlogPost.objects.all()
    c = {'posts': posts}
    return render(request, 'archive.html', c)


def create_blogpost(request):
    if request.method == 'POST':
        BlogPost(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            timestamp=datetime.now()).save()
        return HttpResponseRedirect('/blog/')
