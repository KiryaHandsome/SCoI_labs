from django.contrib import admin
from django.urls import path

from .views import home_screen_view, handler404

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('<path:path>', handler404, name='handler404')
]
