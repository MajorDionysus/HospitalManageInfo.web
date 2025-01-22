from django.contrib import admin
from django.urls import path, include
from hospital_app import views  # Import the views from your app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page
    path('', views.list_items, name='home'),  # Root URL mapped to list_items view (or you can create a home view)
    path('list-items/', views.list_items, name='list_items'),
]
