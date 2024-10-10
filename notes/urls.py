from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('', views.home, name='home'),
    path('note/<note_slug>/', views.note_detail, name='note_detail'),
]
