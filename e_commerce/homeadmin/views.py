from django.shortcuts import render, redirect
from homepage.models import UserID, Permission
from bookstore.models import Product, Review
from django.core.files.storage import FileSystemStorage
from django.conf import settings
# Create your views here.
def HomeAdmin(request, gmail):
    user = UserID.objects.get(gmail = gmail)
    per = Permission.objects.get(id = 2)
    product_list = Product.objects.all()
    context = { 
        'product_list': product_list,
        'username': user.username,     
        'gmail': user.gmail,      
    }
    if user.IDpermission == per:
        return render(request, 'homepage/home.html', context)
    else:
        return render(request, 'homeadmin/homeadmin.html', context)
    
def DeleteBook(request, ID, gmail):
    book = Product.objects.get(id = ID)
    book.delete()
    return redirect('homeadmin:homeadmin', gmail)


def AddBook(request, gmail):
    if request.method  == 'POST' and request.FILES['image']:
        name = request.POST.get('namebook')
        author = request.POST.get('authorbook')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES['image']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT+'/images')
        filename = fs.save(image.name, image)
        filename = 'images/' + filename
        uploaded_file_url = fs.url
        pdf = request.POST.get('pdf')
        physical = request.POST.get('physical') 
        ebook = request.POST.get('ebook')
        # print(image)
        # print(filename)
        # print(uploaded_file_url)
        Book = Product(name = name, author = author, description = description, price = price, image = filename,is_pdf = pdf, is_physical = physical, is_ebook = ebook)
        print(Book)
        Book.save()
        return redirect('homeadmin:homeadmin', gmail)
    return render(request,'homeadmin/AddBook.html', {'gmail': gmail})

def ShowBook(request, id, gmail):
    product = Product.objects.get(id=id)
    context = {'product': product, 'gmail': gmail}
    return render(request,'homeadmin/EditBook.html', context)

def EditBook(request,id, gmail):
    product = Product.objects.get(id=id)
    if request.method == 'POST' and request.FILES['image']:
        name = request.POST.get('namebook')
        author = request.POST.get('authorbook')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES['image']
        fs = FileSystemStorage(location=settings.MEDIA_ROOT+'/images')
        filename = fs.save(image.name, image)
        filename = 'images/' + filename
        uploaded_file_url = fs.url  
        pdf = request.POST.get('pdf')
        physical = request.POST.get('physical') 
        ebook = request.POST.get('ebook')   
       
        product.name = name
        product.author = author
        product.description = description
        product.price = price
        product.image = image
        product.is_pdf = pdf
        product.is_physical = physical
        product.is_ebook =ebook
        product.save()
        return redirect('homeadmin:homeadmin', gmail)
    
    
def SearchBook(request, gmail):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        User = UserID.objects.get(gmail = gmail)
        items = Product.objects.filter(name__icontains=search_query)
        context = {
            'items': items,
            'gmail': gmail,
            'username': User.username
        }
        return render(request, 'homeadmin/SearchBook.html', context)
    return render(request,'homeadmin/homeadmin.html')

def ViewBookAdmin(request, id, gmail):
    product = Product.objects.get(id = id)
    reviews = Review.objects.filter(product = product)
    User = UserID.objects.get(gmail = gmail)
    context = {
    'product': product,
    'reviews': reviews,
    'name' : User.username,
    'gmail': gmail,
    }
    return render(request, 'homeadmin/ViewBookAdmin.html', context )