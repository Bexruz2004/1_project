from django.urls import path
from .views import (
    home_view,
    contact_view,
)

app_name = 'main'

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),

]