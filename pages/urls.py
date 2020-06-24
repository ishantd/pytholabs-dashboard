from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('subindex/<str:pk>', views.subindex, name='subindex')
]