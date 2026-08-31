from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main import views

from main.views import (
    home,
    products,
    product_detail,
    add_to_cart,
    cart,
    remove_from_cart,
    enquiry,
    increase_quantity,
    decrease_quantity
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('products/', products, name='products'),

    path(
        'product/<int:product_id>/',
        product_detail,
        name='product_detail'
    ),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('categories/', views.categories, name='categories'),
    path('cart/', cart, name='cart'),

    path(
        'cart/add/<int:product_id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/remove/<int:product_id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),
    path('enquiry/', enquiry, name='enquiry'),
    path(
        'cart/increase/<int:product_id>/',
        increase_quantity,
        name='increase_quantity'
    ),

    path(
        'cart/decrease/<int:product_id>/',
        decrease_quantity,
        name='decrease_quantity'
    ),
    
    
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
from main.views import (
    home,
    products,
    product_detail,
    add_to_cart,
    cart,
    remove_from_cart,
    enquiry
)    