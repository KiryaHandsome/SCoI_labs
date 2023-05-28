from django.conf.urls.static import static
from django.urls import path

from lab4 import settings
from .views import (
    home_screen_view,
    create_service,
    delete_service,
    service_list,
    edit_service,
)

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('services/', service_list, name='service_list'),
    path('services/<int:id>/edit', edit_service, name='edit_service'),
    path('services/create', create_service, name='create_service'),
    path('services/<int:id>/delete', delete_service, name='delete_service')
    # path('<path:path>', page_not_found_handler, name='handler404')
]
