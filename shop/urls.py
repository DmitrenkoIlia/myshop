from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('<slug:category_slug>/',
         views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<slug:slug>/',
         views.product_detail,
         name='product_detail'),
     path('brand/<slug:brand_slug>/',
           views.product_list,
           name='product_list_by_brand'),
     path('country/<slug:country_slug>/',
          views.product_list,
          name='product_list_by_country'),
     path('universe/<slug:universe_slug>/',
          views.product_list,
          name='product_list_by_universe'),
     path('character/<slug:character_slug>/',
          views.product_list,
          name='product_list_by_character'),
     path('size/<slug:size_slug>/',
          views.product_list,
          name='product_list_by_size'),
     path('material/<slug:material_slug>/',
          views.product_list,
          name='product_list_by_material'),

]