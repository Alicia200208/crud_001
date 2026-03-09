from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('add/', views.AddUser, name='add_user'),
    path('edit/<int:id>/', views.EditUser, name='edit_user'),
    path('delete/<int:eid>/', views.DeleteUser, name='delete_user'),
    path('view/<int:eid>/', views.ViewUser, name='view_user'),
]