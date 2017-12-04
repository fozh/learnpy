from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.

def home(request):
    return HttpResponse("hello world")

def detail(request, detail_args):
    post = Article.objects.all()[int(detail_args)]
    str = ('title = %s, category = %s, date_time = %s, content = %s' % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)
