from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lot/<int:lot_id>/', views.slot_list, name='slot_list'),
    path('book/<int:slot_id>/', views.book_slot, name='book_slot'),
]