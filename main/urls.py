from django.urls import path, include
from .views import (
    home_view,
    contact_view,
    category_view,
)

app_name = 'main'

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('category/', category_view, name='category'),
    path('main-api/', include('main.main_api.urls', namespace='main-api'))
]