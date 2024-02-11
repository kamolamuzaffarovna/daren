from django.urls import path
from .views import archive_view, detail_view

app_name = 'archive'

urlpatterns = [
    path('', archive_view, name='list'),
    path('detail/<slug:slug>/', detail_view, name='detail'),
]