# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
import time
 
 
#登录验证
def login(req):
    nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if req.method == 'GET':
        uf = UserForm()
        return render_to_response('login.html', RequestContext(req, {'uf': uf,'nowtime': nowtime }))
    else:
        uf = UserForm(req.POST)
        if uf.is_valid():
            username = req.POST.get('username', '')
            password = req.POST.get('password', '')
            user = auth.authenticate(username = username,password = password)
            if user is not None and user.is_active:
                auth.login(req,user)
                return render_to_response('index.html', RequestContext(req))
            else:
                return render_to_response('login.html', RequestContext(req, {'uf': uf,'nowtime': nowtime, 'password_is_wrong': True}))
        else:
            return render_to_response('login.html', RequestContext(req, {'uf': uf,'nowtime': nowtime }))

 
def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect('/dashboard/')
        else:
            return HttpResponse("login.html")
    else:
        t = loader.get_template("login.html")
        return HttpResponse(t.render())

def logout_view(request):
        logout(request)
        t = loader.get_template("login.html")
        return HttpResponse(t.render())

# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
