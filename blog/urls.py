from django.urls import path
from . import  views

app_name = 'blog'

urlpatterns = [
    path('', views.login, name = 'login'),
    path('list/', views.post_list, name='post_list'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('list/<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]