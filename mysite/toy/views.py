from django.http import HttpResponse, request
from django.shortcuts import render

def gugu(req, num):
    return render(req, 'toy/gugu.html', 
            {'mul_table': [f"{num} * {i} = {num * i}" for i in range(1, 10)]})

def naver(req):
    res = request.get("https://naver,com/")
    return HttpResponse(res.text)

