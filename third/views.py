from django.shortcuts import render, get_object_or_404, redirect
from . models import Restaurant, Review
from django.core.paginator import Paginator
from . forms import RestaurantForm, ReviewForm, UpdateRestaurantForm
from django.http import HttpResponseRedirect
from django.db.models import Count, Avg


# Create your views here.
def list(request):
    restaurants = Restaurant.objects.all()\
        .annotate(reviews_count = Count('review'))\
        .annotate(average_point=Avg('review__point'))
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
        item = get_object_or_404(Restaurant, pk=request.POST.get('id'))
        password = request.POST.get('password', '') # 비밀번호 값이 있으면 해당 값을 가져오고 없으면 공백으로 가져옴
        form = UpdateRestaurantForm(request.POST, instance=item)
        if form.is_valid() and password == item.password: # 유효성 체크 및 비밀번호 검증
            item = form.save()
    elif request.method == 'GET':
        item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        form = RestaurantForm(instance=item)
        form.password = ""
        return render(request, 'third/update.html', {'form': form})
    return HttpResponseRedirect('/third/list/')


def detail(request, id): # path parameter로 선언하면 id를 받을 수 있음
    if 'id' is not None:
        # item = get_object_or_404(Restaurant, pk=request.GET.get('id'))
        item = get_object_or_404(Restaurant, pk=id)
        reviews = Review.objects.filter(restaurant=item).all() # 식당에 해당하는 리뷰을 조회
        return render(request, 'third/detail.html', {'item': item, 'reviews': reviews})
    return HttpResponseRedirect('/third/list/')


def delete(request, id):
    item = get_object_or_404(Restaurant, pk=id)
    if request.method == 'POST' and 'password' in request.POST:
        if item.password == request.POST.get('password'):
            item.delete()
            return redirect('list')
        return redirect('restaurant-detail', id=id)
    return render(request, 'third/delete.html', {'item': item})


def review_create(request, restaurant_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        # HttpResponseRedirect을 사용하면 url을 다 써주어야하고, 만약 url이 변경되었을 때 함께 수정해주어야 하는 번거로움이 있음
        # shortcuts의 redirct를 사용하면 url 기반이 아니라 urls.py에 정의한 view name 기반으로 움직이기 때문에
        # url이 변경되더라고 view name이 그대로라면 변경하지 않아도 된다.
        return redirect('restaurant-detail', id=restaurant_id)
    item = get_object_or_404(Restaurant, pk=restaurant_id)
    form = ReviewForm(initial={'restaurant': item})
    return render(request, 'third/review_create.html', {'form': form, 'item': item})


def review_delete(request, restaurant_id, review_id):
    item = get_object_or_404(Review, pk=review_id)
    item.delete()
    return redirect('restaurant-detail', id=restaurant_id)


def review_list(request):
    reviews = Review.objects.all().select_related().order_by('-created_at')
    paginator = Paginator(reviews, 10)  # 한 페이지에 10개씩 표시
    page = request.GET.get('page')  # query params에서 page 데이터를 가져옴
    items = paginator.get_page(page)  # 해당 페이지의 아이템으로 필터링
    context = {
        'reviews': items
    }
    return render(request, 'third/review_list.html', context)
