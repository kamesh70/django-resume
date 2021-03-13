from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name='home'),
]