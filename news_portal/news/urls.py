from django.urls import path
from .import views

urlpatterns = [
    path("ekn/", views.ekantipur_news, name="ek_news"),
    path('',views.index,name='home'),
    path('search/',views.search_results_list,name='search_results')

]
