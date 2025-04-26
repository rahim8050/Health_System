from django.urls import path
from . import views

app_name = 'health'  # Namespace for your app

urlpatterns = [
    path('programs/', views.program_list, name='program_list'),
    path('programs/<int:id>/<slug:slug>/', views.program_detail,name='detail'),
]