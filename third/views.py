from django.shortcuts import render, get_object_or_404
from . models import Restaurant
from django.core.paginator import Paginator
from . forms import RestaurantForm
from django.http import HttpResponseRedirect


# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all()
    page = request.GET.get('page')  # 파라미터로 넘어온 현재 페이지 값
    paginator = Paginator(restaurants, 5) # 한 페이지에 5개씩 표시
    items = paginator.get_page(page) # 해당 페이지에 맞는 리스트로 필터링
    context = {
        "restaurants": items
    }
    return render(request, 'third/list.html', context)


def create(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('/third/list/')
    form = RestaurantForm()
    return render(request, 'third/create.html', {'form': form})


def update(request):
    if request.method == 'POST' and 'id' in request.POST:
        # 선택한 id에 해당하는 데이터 조회
        # item = Restaurant.objects.get(pk=request.POST.get('id'))
        # 404 처리
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        # 폼에서 입력한 데이터를 RestaurantForm으로 담고 수정할 대상을 instance 인자로 넘긴다
        form = RestaurantForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save() # 유효하면 update
    elif request.method == 'GET':
        # item = Restaurant.objects.get(pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item) # 조회한 데이터를 RestaurantForm으로 담는다.
        return render(request, 'third/update.html', {'form': form})
    return HttpResponseRedirect('/third/list/')


def detail(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        return render(request, 'third/detail.html', {'item': item})
    return HttpResponseRedirect('/third/list/')


def delete(request):
    if 'id' in request.GET:
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item.delete()
    return HttpResponseRedirect('/third/list/')