from django.urls import path, include
from rest_framework import routers

from staff import views


app_name = 'staff'

routers = routers.DefaultRouter()
routers.register(r'fetchAll', views.ViewStaff)

urlpatterns = [
    path('fetchAll/', views.StaffList.as_view())
]