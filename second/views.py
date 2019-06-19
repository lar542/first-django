from django.shortcuts import render
from second.models import Post
from . forms import PostForm
from django.http import HttpResponseRedirect

# Create your views here.
def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)


def create(request):
    form = PostForm()
    return render(request, 'second/create.html', { 'form': form })


def confirm(request):
    # POST로 넘어온 데이터를 바로 PostForm 클래스의 생성자에 전달한다.
    form = PostForm(request.POST)
    if form.is_valid(): # 정의한 validation 조건 통과
        return render(request, 'second/confirm.html', { "form": form })
    # 데이터가 유효하지 않으면 입력 폼으로 리다이렉트
    return HttpResponseRedirect('/second/create/')