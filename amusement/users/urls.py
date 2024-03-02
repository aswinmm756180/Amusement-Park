from django.urls import path
from .import views
urlpatterns=[
    path('',views.index,name="index"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('viewpage/',views.viewpage,name="viewpage"),
    path('view_food/',views.view_food,name="view_food"),
    path('book_ticket',views.book_ticket,name='book_ticket'),
    path('ticket',views.ticket,name="ticket"),
    path('food',views.food,name='food'),
    
]