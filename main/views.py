from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Category, Product, Enquiry

def about(request):
    return render(request, 'main/about.html')
def contact(request):
    return render(request, 'main/contact.html')
def categories(request):
    categories = Category.objects.all().order_by('name')

    return render(
        request,
        'main/categories.html',
        {
            'categories': categories
        }
    )

def home(request):
    categories = Category.objects.all().order_by('name')

    return render(
        request,
        'main/home.html',
        {
            'categories': categories
        }
    )

def products(request):
    search_query = request.GET.get('search', '')
    category_id = request.GET.get('category')

    products = Product.objects.filter(
    available=True
).order_by('name')

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(product_type__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(specifications__icontains=search_query)
        )

    if category_id:
        products = products.filter(
            category_id=category_id
        )

    categories = Category.objects.all().order_by('name')

    return render(
        request,
        'main/products.html',
        {
            'products': products,
            'categories': categories,
            'search_query': search_query,
            'selected_category': category_id,
        }
    )

def product_detail(request, product_id):
    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        'main/product_detail.html',
        {'product': product}
    )


# =========================
# ADD TO CART
# =========================

def add_to_cart(request, product_id):

    cart = request.session.get('cart', {})

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return redirect('cart')


# =========================
# VIEW CART
# =========================

def cart(request):

    cart_data = request.session.get(
        'cart',
        {}
    )

    cart_products = []
    total = 0

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        cart_products.append({
            'product': product,
            'quantity': quantity
        })

        if product.price:
            total += product.price * quantity

    return render(
        request,
        'main/cart.html',
        {
            'cart_products': cart_products,
            'total': total
        }
    )


# =========================
# REMOVE FROM CART
# =========================

def remove_from_cart(request, product_id):

    cart = request.session.get(
        'cart',
        {}
    )

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


# =========================
# INCREASE QUANTITY
# =========================

def increase_quantity(request, product_id):

    cart = request.session.get(
        'cart',
        {}
    )

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1

    request.session['cart'] = cart

    return redirect('cart')


# =========================
# DECREASE QUANTITY
# =========================

def decrease_quantity(request, product_id):

    cart = request.session.get(
        'cart',
        {}
    )

    product_id = str(product_id)

    if product_id in cart:

        cart[product_id] -= 1

        if cart[product_id] <= 0:
            del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


# =========================
# REQUEST ENQUIRY
# =========================

def enquiry(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        company = request.POST.get('company')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        location = request.POST.get('location')
        message = request.POST.get('message')

        enquiry_obj = Enquiry.objects.create(
            name=name,
            company=company,
            phone=phone,
            email=email,
            location=location,
            message=message
        )

        cart_data = request.session.get('cart', {})

        whatsapp_products = []

        for product_id, quantity in cart_data.items():

            product = get_object_or_404(
                Product,
                id=product_id
            )

            enquiry_obj.products.add(product)

            whatsapp_products.append(
                f"{product.name} - Qty: {quantity}"
            )

        product_text = "\n".join(whatsapp_products)

        whatsapp_message = f"""
Hello 3D Tech Trading Company,

I would like to request a quotation.

Customer: {name}
Company: {company}
Mobile: {phone}
Email: {email}
Location: {location}

Products:
{product_text}

Requirement:
{message}

Thank you.
"""

        import urllib.parse

        whatsapp_url = (
            "https://wa.me/917411837088?text="
            + urllib.parse.quote(whatsapp_message)
        )

        request.session['cart'] = {}

        return render(
            request,
            'main/enquiry_success.html',
            {
                'whatsapp_url': whatsapp_url
            }
        )

    return render(
        request,
        'main/enquiry.html'
    )