import email
from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth, Group
from django.contrib.auth import authenticate
from django.contrib import messages
from accounts.decorators import unauthenticated_user,allowed_users, admin_only
from django.contrib.auth.decorators import login_required
from myapp.models import *
from myapp.forms import *

# Create your views here.

def index (request):
    products = Product.objects.all
    cat= Category.objects.all
    attribute = ProductAttribute.objects.all
    
    catid=request.GET.get ('category')
    if catid:
        products = Product.objects.filter(category=catid)

    else:

        products = Product.objects.all

    context = {
            'products' :products,
            'cat' :cat,
            'attribute':attribute
        }
    return render (request,'myapp/index.html',context)

def attribute (request):
    attribute = ProductAttribute.objects.all
    p_color = Color.objects.all
    p_size = Size.objects.all

    if request.method =="POST":
        color = Color.objects.get(id =request.POST ['color'])
        size = Size.objects.get(id =request.POST ['size'])
        quantity = request.POST ['quantity']
        price = request.GET ['price']
        data = ProductAttribute(color = color, size = size, quantity = quantity, price = price)
        data.save()
        return redirect ('cart/')
    else:
        context = {
            'attribute': attribute,
            'p_color': p_color,
            'p_size': p_size

        }
        return render ('myapp/index.html', context)



@login_required (login_url= 'login')
def about (request):
    return render (request,'myapp/about.html')

@login_required (login_url= 'login')
def cart (request):
    return render (request,'myapp/cart.html')

@login_required (login_url= 'login')
def checkout (request):
    return render (request, 'myapp/checkout.html')
    
@login_required (login_url= 'login')
def Contact (request):
    if request.method =='POST':
        full_name = request.POST['full_name']
        phone_num= request.POST['phone_num']
        email= request.POST['email']
        message=request.POST['message']
        contacts=contact (full_name = full_name, phone_num = phone_num, email = email,message = message)
        contacts.save()
        #messages.info(request,'Queries Added.')
        return redirect('contact/')
    else:  
        return render(request, 'myapp/contact.html')

@login_required (login_url= 'login')
@allowed_users
def admin (request):
    use = User.objects.all
    categories= Category.objects.all
    products = Product.objects.all
    category_count =Category.objects.count()
    product_count =Product.objects.count()
    user_count =User.objects.count()
    context = {
            'categories' :categories,
            'category_count' :category_count,
            'products':products,
            'product_count' :product_count, 
            'use':use,
            'user_count' :user_count,      
            }
    return render(request,'admin/admin-panel.html',context)

#admin
@login_required (login_url= 'login')
@admin_only
def dashboard(request):
    use = User.objects.all
    products = Product.objects.all
    order = Order.objects.all
    product_count =Product.objects.count()
    user_count =User.objects.count()
    order_count = Order.objects.count()

    context = {
            'order': order ,
            'order_count': order_count,      
            'products':products,
            'product_count' :product_count, 
            'use':use,
            'user_count' :user_count,      
            }

    return render(request,'admin/admin-panel.html',context)


#category
#@login_required (login_url= 'login')
#@admin_only
#def category(request):
    #categories= category.objects.all
    #return render (request,'admin/category.html',{'categories': categories})

@login_required (login_url= 'login')
@admin_only
def addcategory(request):
    if request.method == 'POST':
        category_name = request.POST['category_name']
        categor=Category (category_name = category_name)
        categor.save()
        messages.info(request,'CATEGORY ADDED SUCCESSFULLY.')
        return redirect('category')
    else:  
        return render(request, 'admin/add-category.html')

@login_required (login_url= 'login')
@admin_only
def edit_category (request,id):
    categories =Category.objects.get(id = id)
    context = {'categories':categories}
    return render (request,'admin/edit-category.html',context)

@login_required (login_url= 'login')
@admin_only
def update_category (request,id):
    categor =Category.objects.get(id = id)
    categor.category_name = request.POST['category_name']
    categor.save()
    messages.info(request,'SAVE CHANGES')
    return redirect ('/category')

@login_required (login_url= 'login')
@admin_only
def delete_category(request,id):
    categor =Category.objects.get(id = id)
    categor.delete()
    messages.info(request,'CATEGORY DELETED SUCCESSFULLY.')
    return redirect ('/category')



#user
@login_required (login_url= 'login')
@admin_only
def user(request):
    users= User.objects.all
    return render (request,'admin/user.html',{'users': users})

@login_required (login_url= 'login')
@admin_only
def adduser (request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken')
                return redirect('adduser')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken')
                return redirect('adduser')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name = first_name,last_name=last_name,)
                user.save()
                messages.success(request, 'Account is successfully created for' + user)
                return redirect ('user')
        else:
            messages.warning(request, 'Password does not match')
            return redirect ('adduser')
    else:
        return render (request,'admin/add-user.html')

@login_required (login_url= 'login')
@admin_only
def edit_user (request,id):
    users =User.objects.get(id = id)
    context = {'users':users}
    return render (request,'admin/edit-user.html',context)

@login_required (login_url= 'login')
@admin_only
def update_user (request,id):
    user =User.objects.get(id = id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.username = request.POST['username']
    user.email = request.POST['email']
    user.save()
    messages.info(request,'SAVE CHANGES')
    return redirect ('/user')

@login_required (login_url= 'login')
@admin_only
def delete_user(request,id):
    user =User.objects.get(id = id)
    user.delete()
    messages.info(request,'PRODUCT DELETED SUCCESSFULLY.')
    return redirect ('/user')

@login_required (login_url= 'login')
@admin_only
def adminorder(request):
    return render(request,'admin/admin-orders.html')



@login_required (login_url= 'login')
@admin_only
def adminlogout(request):
    auth.logout(request)
    return redirect('/')
def admin(request):
    return render(request,'admin/admin-panel.html')

@login_required (login_url= 'login')
@admin_only
def addorder(request):
    return render(request, 'admin/add-order.html')



#product
@login_required (login_url= 'login')
@admin_only
def product(request):
    products = Product.objects.all
    
    context = {
        'products': products
    }
    return render(request,'admin/admin-products.html',context)

@login_required (login_url= 'login')
@admin_only
def addproduct(request):
    p_category = Category.objects.all
    
    if request.method == 'POST':
        product_image = request.POST['product_image']
        product_name = request.POST['product_name']
        product_description = request.POST['product_description']
        category = Category.object.get (id = request.POST ['category'])
        product_price = request.POST['product_price']
        product_quantity = request.POST['product_quantity']
        product_stat = request.POST['product_stat']
        products=Product(product_name = product_name, product_image = product_image, product_description = product_description, category = category ,product_quantity = product_quantity, product_stat = product_stat, product_price = product_price,)
        products.save()
        messages.info(request,'PRODUCT ADDED SUCCESSFULLY.')
        return redirect('product')
    else:  
        return render(request, 'admin/add-product.html',{'p_category': p_category})

@login_required (login_url= 'login')
@admin_only
def edit_product (request,id):
    products =Product.objects.get(id = id)
    context = {'products':products}
    return render (request,'admin/edit-product.html',context)

@login_required (login_url= 'login')
@admin_only
def update_product (request,id):
    product =Product.objects.get(id = id)
    product.product_image = request.POST['product_image']
    product.product_name = request.POST['product_name']
    product.product_description = request.POST['product_description']
    product.product_price = request.POST['product_price']
    product.product_quantity = request.POST['product_quantity']
    product.product_stat = request.POST['product_stat']
    product.save()
    messages.info(request,'SAVE CHANGES')
    return redirect ('/product')

@login_required (login_url= 'login')
@admin_only
def delete_product(request,id):
    product =Product.objects.get(id = id)
    product.delete()
    messages.info(request,'PRODUCT DELETED SUCCESSFULLY.')
    return redirect ('/product')
