from django.urls import path
from . import views

app_name = 'wiki'

urlpatterns = [
    # 词条相关URL
    path('', views.entry_list, name='entry_list'),
    path('entries/', views.entry_list, name='entry_list'),
    path('entries/create/', views.entry_create, name='entry_create'),
    path('entries/<int:entry_id>/', views.entry_detail, name='entry_detail'),
    path('entries/<int:entry_id>/edit/', views.entry_edit, name='entry_edit'),
    path('entries/<int:entry_id>/delete/', views.entry_delete, name='entry_delete'),
    
    # 分类相关URL
    path('categories/', views.category_list, name='category_list'),
    path('categories/<int:category_id>/entries/', views.category_entries, name='category_entries'),
]