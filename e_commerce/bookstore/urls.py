from django.urls import path    
from bookstore import views  

app_name = 'bookstore'
urlpatterns = [
    path('ViewBook/<int:id>/<str:username>/<str:gmail>', views.ViewBook, name = 'ViewBook'),
    path('AddReview/<int:id>/<str:user>/<str:gmail>', views.AddReview, name = 'AddReview'),
    path('DeleteReview/<int:id>/<int:idpro>/<str:user>/<str:gmail>', views.DeleteReview, name = 'DeleteReview'),
    path('EditReview/<int:id>/<int:idpro>/<str:user>/<str:gmail>', views.EditReview, name = 'EditReview'),
    path('ShowReview/<int:id>/<int:idpro>/<str:user>/<str:gmail>', views.ShowReview, name = 'ShowReview'),
]
