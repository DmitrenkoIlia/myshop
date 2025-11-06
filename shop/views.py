from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Brand, Country, Universe, Character, Size, Material
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q


def product_list(request, category_slug=None):
    """
    Відображає список товарів з можливістю фільтрації за категорією
    та множинними GET-параметрами.
    """
    category = None
    products = Product.objects.filter(available=True)

    search_query = request.GET.get('q', '').strip()
    if search_query:
        products = products.filter(
            Q(name__iregex=search_query) |
            Q(description__iregex=search_query)
        )

    # 1. Фільтрація по категорії (якщо є в URL)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    # 2. Отримання параметрів фільтрації з URL
    # request.GET.get('brand') візьме значення ?brand=...
    filter_params = {
        'brand': request.GET.get('brand'),
        'country': request.GET.get('country'),
        'universe': request.GET.get('universe'),
        'character': request.GET.get('character'),
        'size': request.GET.get('size'),
        'material': request.GET.get('material'),
    }

    # 3. Застосування фільтрів до запиту
    if filter_params['brand']:
        slugs = filter_params['brand'].split(',')
        products = products.filter(brand__slug__in=slugs)

    if filter_params['country']:
        slugs = filter_params['country'].split(',')
        products = products.filter(country__slug__in=slugs)

    if filter_params['universe']:
        slugs = filter_params['universe'].split(',')
        products = products.filter(universe__slug__in=slugs)
    
    if filter_params['character']:
        slugs = filter_params['character'].split(',')
        products = products.filter(character__slug__in=slugs)

    if filter_params['size']:
        slugs = filter_params['size'].split(',')
        products = products.filter(size__slug__in=slugs)

    if filter_params['material']:
        slugs = filter_params['material'].split(',')
        products = products.filter(material__slug__in=slugs)

    # 4. Видалення дублікатів, що важливо для ManyToMany полів
    products = products.distinct()

    # 5. Підготовка контексту для передачі в шаблон
    context = {
        'category': category,
        'products': products,
        'search_query': search_query,
        
        # Списки для відображення всіх опцій у фільтрах
        'categories': Category.objects.all(),
        'brands': Brand.objects.all(),
        'countries': Country.objects.all(),
        'universes': Universe.objects.all(),
        'characters': Character.objects.all(),
        'sizes': Size.objects.all(),
        'materials': Material.objects.all(),
        
        # Списки обраних slug'ів для встановлення 'checked' у чекбоксах
        'selected_brands': filter_params['brand'].split(',') if filter_params['brand'] else [],
        'selected_countries': filter_params['country'].split(',') if filter_params['country'] else [],
        'selected_universes': filter_params['universe'].split(',') if filter_params['universe'] else [],
        'selected_characters': filter_params['character'].split(',') if filter_params['character'] else [],
        'selected_sizes': filter_params['size'].split(',') if filter_params['size'] else [],
        'selected_materials': filter_params['material'].split(',') if filter_params['material'] else [],
    }
    
    return render(request, 'shop/product/list.html', context)

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