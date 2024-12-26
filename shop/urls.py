from django.urls import path
from .views import *

urlpatterns= [
    path('',home,name="home"),
    path('register/',register,name="register"),
    path('login',login_page,name="login"),
    path('logout',logout_page,name="logout"),
    path('cart',cart_page,name="cart"),
    path('fav',fav_page,name="fav"),
    path('favviewpage',favviewpage,name="favviewpage"),
    path('remove_fav/<str:fid>',remove_fav,name="remove_fav"),
    path('remove_cart/<str:cid>',remove_cart,name="remove_cart"),
    path('collections',collections,name="collections"),
    path('collections/<str:name>',collectionsview,name="collections"),
    path('collections/<str:cname>/<str:pname>',product_details,name="product_details"),
    path('addtocart',add_to_cart,name="addtocart"),
    path('payment/',payment_page, name='payment'),
    path('make_payment/',make_payment_page, name='make_payment'),
]
 