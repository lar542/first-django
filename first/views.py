from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.shortcuts import render
import random

# Create your views here.
def index(request):
    template = loader.get_template('first/index.html') # html 파일을 로딩
    now = datetime.now()
    context = {
        'current_date': now
    } # 템플릿에 전달할 데이터를 세팅할 수 있는 오브젝트
    return HttpResponse(template.render(context, request))


def select(request):
    context = {}
    return render(request, 'first/select.html', context)


def result(request):
    # 요청 데이터가 딕셔너리 형태 담긴다
    # get이나 post로 넘어온 데이터는 문자열 형태가 된다.
    chosen = int(request.GET['number'])
    result = []
    if chosen >= 1 and chosen <= 45:
        result.append(chosen)

    box = [] # 입력하지 않은 숫자
    for i in range(0, 45):
        if chosen != i+1:
            box.append(i+1)

    random.shuffle(box)

    while len(result) < 6:
        result.append((box.pop()))

    context = {
        'numbers': result
    }
    return render(request, 'first/result.html', context)


def calendar(request, year, month):
    message = str(year) + "년 " + str(month) + "월 입니다."
    return HttpResponse(message)


def year_archive(request, year):
    message = str(year) + "년 입니다!"
    return HttpResponse(message)