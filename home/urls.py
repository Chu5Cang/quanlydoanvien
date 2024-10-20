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
    # name='add_chidoan nay coi nhu la 1 bien dai dien cho url de có thể sử dụng trong html
    path('chidoan/<str:maCD>/delete/', views.delete_chidoan, name='delete_chidoan'),
    path('chidoan/edit/<str:maCD>/', views.edit_chidoan, name='edit_chidoan'),
    path('chidoan/export/', views.export_chidoan, name='export_chidoan'),
    path('chidoan/import/', views.import_chidoan, name='import_chidoan'),
    path('doanvien/', views.doanvien, name='doanvien'),
    path('doanvien/add/', views.add_doanvien, name='add_doanvien'),
    path('doanvien/<str:maDV>/delete/', views.delete_doanvien, name='delete_doanvien'),
    path('doanvien/edit/<str:maDV>/', views.edit_doanvien, name='edit_doanvien'),
    # name='add_doanvien nay coi nhu la 1 bien dai dien cho url de có thể sử dụng trong html
    path('doanvien/import/', views.import_doanvien, name='import_doanvien'),
    path('doanvien/export/', views.export_doanvien, name='export_doanvien'),

    path('hocky/add/', views.add_hocky, name='add_hocky'),
    path('doanphi/', views.doanphi, name='doanphi'),
    path('doanphi/add/', views.add_doanphi, name='add_doanphi'),
    path('doanphi/edit/<str:maDP>', views.edit_doanphi, name='edit_doanphi'),
]
