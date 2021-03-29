from django.urls import path,include
from kafkaDemo import urls
from . import views


urlpatterns = [
    path('', views.hello, name="hello"),
]
