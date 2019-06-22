from django.shortcuts import render
from . models import Restaurant

# Create your views here.
def list(request):
    context = {
        "restaurants": Restaurant.objects.all()
    }
    return render(request, 'third/list.html', context)

