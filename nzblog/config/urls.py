from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('', views.post, name='post_list')
]
