from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='ship'

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:ship_name>/', views.detail, name='detail'),

]