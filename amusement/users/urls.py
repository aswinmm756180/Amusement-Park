from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('viewpage/',views.viewpage,name="viewpage"),
    path('view_food/',views.view_food,name="view_food"),
    path('book/', views.book_room, name='book_room'),
    # path('booking_confirmation/', views.booking_confirmation, name='booking_confirmation'),
]