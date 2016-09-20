from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.bookcase_list, name="index"),
]