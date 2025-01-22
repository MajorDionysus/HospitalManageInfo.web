# In hospital_website/urls.py
from django.contrib import admin
from django.urls import path, include
from hospital_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_items, name='home'),  # 根路径指向 list_items 视图
    path('list-items/', views.list_items, name='list_items'),
]
