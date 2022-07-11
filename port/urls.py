from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='port'

urlpatterns = [
    path('', views.index, name="index"),
    path('index_cargo', views.index_cargo, name="index_cargo"),
    path('index_order', views.index_order, name="index_order"),
    path('index_ship', views.index_ship, name="index_ship"),
  # path('<int:port_id>/', views.detail, name='detail'),
  #  path('parameter', views.get_post, name='parameter'),
    path('list', views.port_ship_list, name='views.port_ship_list'),

]