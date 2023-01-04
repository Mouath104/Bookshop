
from turtle import update
from django.urls import path
from FSApp import views


app_name = 'FSApp'

urlpatterns = [

    path("",views.index, name='index'),
    path("add/",views.add,name='add'),
    path("add/addP/",views.addP,name='addP'),
    path("delete/<int:id>",views.delete),
    path("deleteItem/<int:id>", views.deleteItem),
    path("update/<int:id>",views.update),
    path("update/updaterow/<int:id>",views.updaterow),
    path('registerGet/',views.registerGet,name='registerGet'),
    path('registerPost/',views.registerPost,name='registerPost'),
    path('user_login/',views.user_login,name='user_login'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('cart/',views.cart,name='cart'),
    path('book_details/<int:id>', views.book_details,name='book_details'),
    path('CartBooksPost/<int:id>', views.CartBooksPost,name='CartBooksPost'),
    path('CartBooksPost_ToBD/<int:id>', views.CartBooksPost_ToBD,name='CartBooksPost_ToBD'),
    # path('profile/',views.profile_details,name='profile') 2b added later
]
