from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('select/', views.select, name="select"),
    path('result/', views.result, name="result"),

    path('calendar/<int:year>/<int:month>', views.calendar, name="calendar"),
    re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive, name="year_archive")
]
