from django.shortcuts import render, redirect
from homepage.models import Permission, UserID
from bookstore.models import  Product, Review, Order, OrderItem
from django.contrib.auth import  logout

# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')

def home(request, name, gmail):
    product_list = Product.objects.all()
    context = {'product_list': product_list, 'username': name, 'gmail': gmail}
    return render(request, 'homepage/home.html', context)

def MyRegister(request):
    if request.method == 'POST':
        gmail = request.POST.get('gmail')
        username  = request.POST.get('username')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        id = Permission.objects.get(id = 2)
        user = UserID(gmail = gmail, username = username, password = password, IDpermission= id) 
        user.save() 
        return redirect('homepage:home', username)
    return render(request, 'homepage/register.html')

def MyLogin(request):
    if request.method == 'POST':
        gmail = request.POST.get('gmail')
        password = request.POST.get('password')
        user = UserID.objects.get(gmail = gmail)
        per = Permission.objects.get(id = 2)
        if user.password == password:
            if user.IDpermission == per:
                return redirect('homepage:home', user.username, gmail)
            else: 
                print(user.gmail)
                return redirect('homeadmin:homeadmin', user.gmail)
    return render(request, 'homepage/login.html') 

def MyLogout(request):
    return render(request,'homepage/index.html')

def SearchBook(request, username, gmail):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        items = Product.objects.filter(name__icontains=search_query)
        context = {
            'items': items,
            'username': username,
            'gmail': gmail,
        }
        return render(request, 'homepage/SearchBookUser.html', context)
    return render(request,'homepage/home.html')

def cart(request, gmail):
    user = UserID.objects.get(gmail = gmail)
    order, created = Order.objects.get_or_create(customer=user, complete = False)
    items = order.orderitem_set.all()
    context = {
        "items": items,
        'order': order,
        'username': user.username,
        'gmail' : gmail,
    }
    return render(request, 'homepage/cart.html', context)

def AddQuantityBook(request, idproduct, name, gmail):
    product = Product.objects.get(id = idproduct)
    user = UserID.objects.get(gmail = gmail)
    order = Order.objects.get(complete = False, customer = user)
    print('Order',order)
    #order = Order.objects.get(customer = user)
    order_items = OrderItem.objects.filter(order = order)
    print(order_items.count())
    print('Product', product)
    flag = False
    for item in order_items:
        print('item', item)
        if item.product == product:         
            item.quantity +=1
            item.save()
            print(item.quantity)
            flag = True
    if flag == False:
        order_item = OrderItem(product = product, order = order, quantity = 1)
        order_item.save()
    return redirect('homepage:home', name, gmail)

def UpdateStatusPayment(request, idOrder):
    order = Order.objects.get(id = idOrder)
    order.complete = True
    order.save()
    context = { 'username' : order.customer.username, 'gmail': order.customer.gmail }
    return redirect('homepage:home', order.customer.username, order.customer.gmail)
    #return redirect('homepage:home', idOrder)
    
def OrderHistory(request, idOrders, gmail):
    user = UserID.objects.get(gmail = gmail)
    orders = Order.objects.filter(customer = user, complete = True)
    #order = Order.objects.get(complete = True)
    #print(items)
    for order in orders:
        item = order.orderitem_set.all()
    username = UserID.objects.get(gmail = gmail)
    context = {
        'order': order,
        'items': items,
        'gmail' : gmail,
        'username': username.username,
    }
    return render(request, 'homepage/HistoryOrder.html', context)