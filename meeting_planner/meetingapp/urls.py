from django.urls import path
from . import views
urlpatterns = [
 path('', views.index, name='index'),
 path('spotkanie/<int:id>', views.get_spotkanie, name='spotkanie'),
]