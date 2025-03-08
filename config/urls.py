from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.corrosion.urls')),  # Include the corrosion app's URLs
]
