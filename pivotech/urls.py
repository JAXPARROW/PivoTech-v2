from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    #urls for the smart-select(third party app)
    re_path(r'^chaining/', include('smart_selects.urls')),

    #urls for the api v1 application
    path('api/v1/', include('api.urls')),
    
]
