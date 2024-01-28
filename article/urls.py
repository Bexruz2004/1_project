from django.urls import path
from .views import (
    article_list,
    article_detail
)

app_name = 'article'

urlpatterns = [
    path('articles/', article_list, name='list'),
    path('detail<slug:slug>/', article_detail, name='detail'),

]
