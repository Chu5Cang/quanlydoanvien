from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('doanvien/', views.doanvien, name= 'doanvien'),
    path('doankhoa/', views.doankhoa, name='doankhoa'),
    path('doankhoa/add/', views.add_doankhoa, name='add_doankhoa'),
    path('doankhoa/<str:maDK>/delete/', views.delete_doankhoa, name='delete_doankhoa'),
    path('doankhoa/edit/<str:maDK>/', views.edit_doankhoa, name='edit_doankhoa'),
    path('doankhoa/export/', views.export_doankhoa, name='export_doankhoa'),
    path('doankhoa/import/', views.import_doankhoa, name='import_doankhoa'),
    path('chidoan/', views.chidoan, name='chidoan'),
    path('chidoan/add/', views.add_chidoan, name='add_chidoan'),
    path('chidoan/<str:maCD>/delete/', views.delete_chidoan, name='delete_chidoan'),
    path('chidoan/edit/<str:maCD>/', views.edit_chidoan, name='edit_chidoan'),
    path('chidoan/export/', views.export_chidoan, name='export_chidoan'),
    path('chidoan/import/', views.import_chidoan, name='import_chidoan'),
]
