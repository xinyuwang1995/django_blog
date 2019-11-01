from django.shortcuts import render #通过template展示页面

from django.http import  HttpResponse
# Create your views here.

def index(request):
    post_list = [
        {
            'link':'/blog/1/',
            'title':'第一篇博客',
            'subtitle':'这是一个副标题',
            'author':'王新宇',
            'date':'2019.10.27',

        },
        {
            'link': '/blog/2/',
            'title': '第二篇博客',
            'subtitle': '这是一个副标题',
            'author': '王新宇',
            'date': '2019.10.27',
        },
    ]
    return render(request,'index.html',{'post_list':post_list}) #最后一个字典给模板传值
def blog_detail(request,blog_id):
    return HttpResponse("this is {} blog".format(blog_id))

def my_add(request,adds,added):
    result = adds + added
    return HttpResponse('the result is{}'.format(result))