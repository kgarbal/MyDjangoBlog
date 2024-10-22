from django.urls import path
from . import views

urlpatterns = [
    path(str(), views.post_list, name='post_list')
]
