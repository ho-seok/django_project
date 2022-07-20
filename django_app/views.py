from django.shortcuts import render
from .models import Post
from .models import Blog


# Create your views here.

#urls.py에서 요청이 왔을때 호출되는 함수
def blog_list(request):

    # QuerySet, db로부터 모든 Blog 오브젝을 가져온다.
    qs = Blog.objects.all()
    
    return render(request,'django_app/post_list.html',{
        #blog_list라는 목록을 넘겨준다.
        'blog_list': qs,
    })