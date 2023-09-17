from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    
    path('indexstaff/', views.indexstaff, name='indexstaff'),
    path('menushow/', views.menushow, name='menushow'),
    path('addmenu/', views.addmenu, name='addmenu'),
    path('reviews/', views.reviews, name='reviews'),
    path('stat/', views.stat, name='stat'),
    path('order_staff/', views.order_staff, name='order_staff'),
    path('delete_menu/<int:menuid>/', views.delete_menu, name='delete_menu'),
    path('edit_menu/<int:menuid>/', views.edit_menu, name='edit_menu'),
    #path('check_face/', views.check_face, name='check_face'),
    path('order_history_staff/', views.order_history_staff, name='order_history_staff'),
    path('checkout_staff/', views.checkout_staff, name='checkout_staff'),
    path('receipt_staff/<int:orderid>/', views.receipt_staff, name='receipt_staff'),
    path('add_to_cart_staff/<int:item_id>/', views.add_to_cart_staff, name='add_to_cart_staff'),
    path('delete_cart_item/<int:cart_id>/<str:item_number>/', views.delete_cart_item, name='delete_cart_item'),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)