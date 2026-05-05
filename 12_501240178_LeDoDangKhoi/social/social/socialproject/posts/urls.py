"""
URL configuration for socialproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.post_create, name='create'),
    path('delete/', views.post_delete, name='delete'),
    path('<int:pk>/like/', views.post_like, name='like'),
    path('<int:pk>/comment/', views.post_comment, name='comment'),
    path('<int:id>/', views.post_detail, name='detail'),
    path('<int:id>/edit/', views.post_edit, name='edit'),
    path('<int:id>/delete/', views.post_delete, name='delete'),
]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)