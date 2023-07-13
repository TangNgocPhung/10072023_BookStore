from django.shortcuts import render, redirect
from bookstore.models import Product, Review
from homepage.models import UserID,Permission
# Create your views here.
def ViewBook(request, id, username, gmail):
    product = Product.objects.get(id = id)
    reviews = Review.objects.filter(product = product)
    user = UserID.objects.get(gmail = gmail)
    context = {
       'product': product,
       'reviews': reviews,
       'name' : user.username,
       'gmail': gmail,
    }
    return render(request, 'bookstore/ViewBook.html', context)
 
def AddReview(request, id, user, gmail):
   #print(id)
   #print(user)
   if request.method == 'POST':
      review = request.POST.get('review')
      product = Product.objects.get(id=id)
      user = UserID.objects.get(gmail = gmail)
      review_user = Review(user = user, product =  product, review = review)
      review_user.save()
      return redirect('bookstore:ViewBook', id, user, gmail)
   return redirect('bookstore:ViewBook', id, user, gmail)

def DeleteReview(request, id, idpro, user, gmail):
   review_user = Review.objects.get(id=id)
   review_user.delete()
   user = UserID.objects.get(gmail=gmail)
   per = Permission.objects.get(id=1)
   # print(user)
   # print(user.IDpermission)
   if user.IDpermission == per:
          print('YES')
          return redirect ('homeadmin:view_book_admin',idpro,  gmail)
   else:
      return redirect('bookstore:ViewBook', idpro, user, gmail)


def EditReview(request, id, idpro , user, gmail):
   review_user = Review.objects.get(id=id)
   if request.method == 'POST':
      review = request.POST.get('review')
      product = Product.objects.get(id=idpro)
      user = UserID.objects.get(gmail = gmail)
      
      review_user.user =  user
      review_user.product =  product
      review_user.review = review
      
      review_user.save()
      return redirect('bookstore:ViewBook', idpro, user, gmail)
   return redirect('bookstore:ViewBook', idpro, user, gmail)

def  ShowReview(request, id, idpro, user, gmail):
   review_show = Review.objects.get(id=id)
   context = {
      
     'review_show': review_show,
     'id':  idpro,
     'user': user,
     'gmail': gmail,
   }
   return redirect('bookstore:ViewBook', idpro, user, gmail)