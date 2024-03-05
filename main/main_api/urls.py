from django.urls import path
from main.main_api.views import main_home_view, main_contact_view

app_name = 'main_api'

urlpatterns = [
    path('main-home/', main_home_view, name='main-home'),
    path('main-contact/', main_contact_view, name='main-contact')
]