from django.contrib import admin
from django.urls import path, include
from BackUpDispatch import views
from BackUpDispatch.views import CFSCreateView, API_list_calls, CFSDetailView

urlpatterns = [

    path('', views.home, name='BackUpDispatch_home'),
    path('vuetest/', views.vuetest, name='vuetest'),
    path('enter/', CFSCreateView.as_view(), name='caseentry'),
    path('listcalls/', views.active_calls, name='listactivecalls'),
    path('listcallsxhr/', views.active_callsxhr, name='listactivecallsxhr'),
    path('view/<int:pk>', CFSDetailView.as_view(), name='CFSdetailview'),

    path('api/listcalls/', API_list_calls.as_view(), name='api_list_calls')
]
