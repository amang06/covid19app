from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='dashboard-home'),
    path('getstats',views.getstats, name="getstats"),
    path('home',views.home,name="home")
]