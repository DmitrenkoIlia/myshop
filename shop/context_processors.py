from .models import Category, Brand, Country, Universe, Character, Size, Material

def categories(request):
    return {'categories': Category.objects.all()}

def brands(request):
    return {'brands': Brand.objects.all()}

def countries(request):
    return {'countries': Country.objects.all()}

def universes(request):
    return {'universes': Universe.objects.all()}

def characters(request):
    return {'characters': Character.objects.all()}

def sizes(request):
    return {'sizes': Size.objects.all()}

def materials(request):
    return {'materials': Material.objects.all()}

def wishlist_context(request):
    """
    Добавляет количество товаров в избранном в контекст для всех страниц.
    """
    if request.user.is_authenticated:
        # Считаем товары в избранном у профиля пользователя
        count = request.user.profile.wishlist.count()
    else:
        count = 0
    return {'wishlist_count': count}