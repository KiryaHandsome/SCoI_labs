from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('repair_service.urls')),
    path('register/', include('account.urls'))
]
