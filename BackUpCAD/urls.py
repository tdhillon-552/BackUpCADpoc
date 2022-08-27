from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    path('', include('BackUpDispatch.urls'), name='auth_app'),
    path('admin/', admin.site.urls),

]
