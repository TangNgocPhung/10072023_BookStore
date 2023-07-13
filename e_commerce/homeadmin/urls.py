from django.urls import path      
from homeadmin import views  

app_name = 'homeadmin'

urlpatterns = [
    path('HomeAdmin/<str:gmail>/', views.HomeAdmin, name = 'homeadmin'),
    path('DeleteBook/<int:ID>/<str:gmail>', views.DeleteBook, name = 'delete_book'),
    path('AddBook/<str:gmail>', views.AddBook, name = 'add_book'),
    path('ShowBook/<int:id>/<str:gmail>', views.ShowBook, name= 'show_book'),
    path('EditBook/<int:id>/<str:gmail>', views.EditBook, name= 'edit_book'),
    path('SearchBook/<str:gmail>', views.SearchBook, name= 'search_book'),
    path('ViewBookAdmin/<int:id>/<str:gmail>', views.ViewBookAdmin, name= 'view_book_admin'),
]
