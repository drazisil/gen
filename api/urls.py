from django.urls import path

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.index, name='index'),
    path('pony/', views.pony, name='pony'),
    path('pony_lookup', views.pony_lookup, name='pony_lookup'),
    path('pony/<str:pony_id>', views.fetch_pony, name='fetch_pony'),
]
