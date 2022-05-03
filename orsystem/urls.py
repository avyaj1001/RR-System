"""system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from myapp import views
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/',views.dashboard, name="dashboard"),
    path('accounts/', include('accounts.urls')),

    #ADMIN PANEL
    path('dashboard/',views.dashboard, name="dashboard"),
    path('logout/',views.adminlogout, name="adminlogout"),
    path('add-order/',views.addorder, name="addorder"),

    path('orders/',views.adminorder, name="adminorder"),

    #category
    #path('category/',views.category, name="category"),
    #path('add-category/',views.addcategory, name="addcategory"),
    #path('edit/<int:id>', views.edit_category, name="edit_category"),
    #path('update/<int:id>', views.update_category, name ="update_category"),   
    #path('delete/<int:id>', views.delete_category, name ="delete_category"), 

     #product
    path('add-product/',views.addproduct, name="addproduct"),
    path('product/',views.product, name="product"),
    path('edit/<int:id>', views.edit_product, name="edit_product"),
    path('update/<int:id>', views.update_product, name ="update_product"),   
    path('delete/<int:id>', views.delete_product, name ="delete_product"), 

    #user
    path('user/',views.user, name="user"),
    path('add-user/',views.adduser, name="adduser"),
    path('edit/<int:id>', views.edit_user, name="edit_user"),
    path('update/<int:id>', views.update_user, name ="update_user"),   
    path('delete/<int:id>', views.delete_user, name ="delete_user"), 


    #main
    path ('',views.index, name="index"),
    path ('about/',views.about, name="about"),
    path ('contact/',views.contact, name="contact"),
    path ('checkout/',views.checkout, name="checkout"),
    path ('cart/',views.cart, name="cart"),

] 
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


