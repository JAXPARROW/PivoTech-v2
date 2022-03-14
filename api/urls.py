from django import views
from django.urls import path
from api import views


urlpatterns = [
    path('clusters/',views.ClusterList.as_view()),
    path('sites/', views.SiteList.as_view()),
    path('fuelstations/', views.FuelStationList.as_view()),
    path('fieldengineers/', views.FieldEngineerList.as_view()),
    # path('users/', views.UserList.as_view()),
    # path('groups/',views.GroupList.as_view()),
]