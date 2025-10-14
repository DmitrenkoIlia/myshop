from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    # Головна сторінка каталогу (всі товари)
    # Приклад: /
    path('', views.product_list, name='product_list'),

    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    # Сторінка каталогу для конкретної категорії
    # Приклад: /figures/
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    # Сторінка деталей товару (не змінюється)
    # Приклад: /1/funko-pop-iron-man/
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
    # Інші шляхи, як-от wishlist, залишаються без змін

]