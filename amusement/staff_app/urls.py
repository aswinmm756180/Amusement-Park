from django.urls import path
from .import views



urlpatterns=[
    path('Food_list',views.Food_list,name="Food_list"),
    path('add_food',views.add_food,name="add_food"),
    path('edit_food/<int:food_id>/', views.edit_food, name='edit_food'),
    path('deletefood/<int:pk>/', views.deletefood, name='deletefood'),
    path('staff_register',views.staff_register,name='staff_register'),


    path('viewuser/', views.viewusers, name='viewuser'),
    path('admin_dashboard/',views.admin_dashboard,name="admin_dashboard"),
]