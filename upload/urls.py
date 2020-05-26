from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('teacher-admin/', views.teacher_admin, name="tcadmin"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
