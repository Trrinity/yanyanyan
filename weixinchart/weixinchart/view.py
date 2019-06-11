from django.http import HttpResponse
from django import forms
from django.shortcuts import render_to_response
#from models import User
 
def hello1(request):
    return HttpResponse("Hello world ! ")

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

#创建表单
class UserForm(forms.Form):
    username=forms.CharField(label='用户名：',max_length=100)
    password=forms.CharField(label='密码：',widget=forms.PasswordInput())
    email=forms.EmailField(label='电子邮件：')

#Create your views here
def register(request):
    if request.method=='POST':
        uf=UserForm(request.POST)
        if uf.is_valid():
            #获取表单信息
            username=uf.cleaned_data['username']
            password=uf.cleaned_data['password']
            email=uf.cleaned_data['email']
            #将表单写入数据库
            user=User()
            user.username=username
            user.password=password
            user.email=email
            user.save()

            return render_to_response('success.html',{'username':username})
    else:
        uf=UserForm()
        return render_to_response('register.html',{'uf':uf})
