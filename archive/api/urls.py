from django.urls import path
from .views import article_list_view, article_detail_view

app_name = 'api'

urlpatterns = [
    path('api-list/', article_list_view, name='api-list'),
    path('api-detail/', article_detail_view, name='api-detail')
]