from django.urls import path

from .views import home_screen_view, page_not_found_handler, service_list

urlpatterns = [
    path('', home_screen_view, name='home'),
    path('services/', service_list, name=''),
    path('services/<int:id>/edit', edit_service, name='edit_service'),
    path('services/create', create_service, name='create_service'),
    path('services/<int:id>/delete', delete_service, name='delete_service')
    # path('<path:path>', page_not_found_handler, name='handler404')
]
