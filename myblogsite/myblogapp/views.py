# Create your views here.
from django.shortcuts import render_to_response
from myblogapp.models import Post


def myview(request):
	posts = Post.objects.all()
	post_body_list = [post.body for post in posts]
	return render_to_response('mytemplate.html',{'post_list':post_body_list})


def frontpage(request):
    posts = Post.objects.all()
    return render_to_response("frontpage.html",{'post_list':posts})
