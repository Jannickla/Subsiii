from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('webshop.urls')),
    path('profile/', include('dashboard.urls')),
    path('', include('users.urls')),
]