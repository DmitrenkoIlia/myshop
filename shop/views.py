from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Brand, Country, Universe, Character, Size, Material
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def product_list(request, category_slug=None, brand_slug=None, country_slug=None, 
                 universe_slug=None, character_slug=None, size_slug=None, material_slug=None):
    category = None
    brand = None
    country = None
    universe = None
    character = None
    size = None
    material = None
    
    categories = Category.objects.all()
    brands = Brand.objects.all()
    countries = Country.objects.all()
    universes = Universe.objects.all()
    characters = Character.objects.all()
    sizes = Size.objects.all()
    materials = Material.objects.all()
    
    products = Product.objects.filter(available=True)
    
    # Фильтрация по категории
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Фильтрация по бренду
    if brand_slug:
        brand = get_object_or_404(Brand, slug=brand_slug)
        products = products.filter(brand=brand)
    
    # Фильтрация по стране
    if country_slug:
        country = get_object_or_404(Country, slug=country_slug)
        products = products.filter(country=country)
    
    # Фильтрация по вселенной (ManyToMany поле)
    if universe_slug:
        universe = get_object_or_404(Universe, slug=universe_slug)
        products = products.filter(universe=universe)
    
    # Фильтрация по персонажу (ManyToMany поле)
    if character_slug:
        character = get_object_or_404(Character, slug=character_slug)
        products = products.filter(character=character)
    
    # Фильтрация по размеру (ManyToMany поле)
    if size_slug:
        size = get_object_or_404(Size, slug=size_slug)
        products = products.filter(size=size)
    
    # Фильтрация по материалу (ManyToMany поле)
    if material_slug:
        material = get_object_or_404(Material, slug=material_slug)
        products = products.filter(material=material)
    
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'brand': brand,
                   'brands': brands,
                   'country': country,
                   'countries': countries,
                   'universe': universe,
                   'universes': universes,
                   'character': character,
                   'characters': characters,
                   'size': size,
                   'sizes': sizes,
                   'material': material,
                   'materials': materials,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart = Cart(request)
    in_cart = str(product.id) in cart.cart
    cart_product_form = CartAddProductForm(product=product)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'in_cart': in_cart,
                   })



@login_required
@require_POST
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    profile = request.user.profile

    if product in profile.wishlist.all():
        profile.wishlist.remove(product)
        action = 'removed'
    else:
        profile.wishlist.add(product)
        action = 'added'

    return JsonResponse({
        'status': 'ok',
        'action': action,
        'wishlist_count': profile.wishlist.count()
    })

@login_required
def wishlist_view(request):
    wishlist_products = request.user.profile.wishlist.all()
    return render(request, 'shop/wishlist.html', {'wishlist_products': wishlist_products})