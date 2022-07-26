from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from . import models
import json

def index(req: HttpRequest) -> HttpResponse:
    return HttpResponse('blog')

def post_list(req):
    posts = models.Post.objects.all()
    return render(req, 'blog/post_list.html', {"post_list": posts})

def post_detail(req, pk):
    post = models.Post.objects.get(pk=pk)
    return render(req, 'blog/post_detail.html', {"post": post})

def post_create(req):
    if req.method == "POST":
        post = models.Post(title=req.POST["title"], content=req.POST['content'])
        post.save()
        return redirect("/blog/post_list/")
    return render(req, 'blog/post_create.html')


def api_post_list(req):
    if req.method =='GET':
        posts = models.Post.objects.all()
        return JsonResponse({"results": list(posts.values())})
    else :
        return HttpResponse(status=405)

from django.forms.models import model_to_dict
def api_post(req, pk):
    if req.method =='GET':
        post =models.Post.objects.get(pk=pk)
        return JsonResponse({"results": model_to_dict(post)})
    else :
        return HttpResponse(status=405)