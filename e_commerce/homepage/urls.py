from django.urls import path  
from homepage import views 

app_name = 'homepage'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup/', views.MyRegister, name = 'signup'),
    path('login/', views.MyLogin, name = 'login'),
    path('home/<str:name>/<str:gmail>', views.home, name = 'home'),
    path('logout/', views.MyLogout, name = 'logout'),
    path('SearchBookUser/<str:username>/<str:gmail>', views.SearchBook, name = 'search_book_user'),
    path('Cart/<str:gmail>', views.cart, name = 'cart'),
    path('AddQuantityBook/<int:idproduct>/<str:name>/<str:gmail>', views.AddQuantityBook, name = 'add_quantity_book'),
]
