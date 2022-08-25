from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name ='index'),
    path('delete/<int:post_id>/',views.delete, name ='delete'),
]