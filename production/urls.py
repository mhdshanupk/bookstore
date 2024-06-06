from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('add_book/',views.add_book,name='add_book'),
    path('bookview/<int:id>/',views.book_view,name='bookview'),
    path('bookedit/<int:id>/',views.book_edit,name='book_edit'),
    path('bookdelete/<int:id>/',views.book_delete,name='book_delete'),
    path('register/',views.user_register,name='register' ),
    path('',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('user_home/<int:id>/',views.user_home,name='user_home'),
    path('review_edit/<int:id>/',views.review_edit,name='review_edit'),
    path('review_delete/<int:id>/',views.review_delete,name='review_delete'),
    path('publish/<int:id>/',views.publish,name='publish')
    
]
