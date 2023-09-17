from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('login_staff/', views.login_staff, name='login_staff'),
    path('user_home/', views.user_home, name='user_home'),
    path('ewallet/', views.ewallet, name='ewallet'),
    path('profile/', views.profile, name='profile'),
    path('order_history_student/', views.order_history_student, name='order_history_student'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('update_pass/', views.update_pass, name='update_pass'),
    path('process_image/', views.process_image, name='process_image'),
    path('index/', views.index, name='index'),
    path('reg/', views.reg, name='reg'),
    #path('login_view/', views.login_view, name='login_view'),
    #path('loginuser/', views.loginuser, name='loginuser'),
    path('add_to_cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('menushowstudent/', views.menushowstudent, name='menushowstudent'),
    path('add_fund/', views.add_fund, name='add_fund'),
    path('checkout/', views.checkout, name='checkout'),
    path('feedback/remove/<int:feedback_id>/', views.remove_feedback, name='remove_feedback'),
    path('receipt/<int:order_id>/', views.receipt, name='receipt'),
    path('viewcart/', views.viewcart, name='viewcart'),
    path('feedbackmenu/', views.feedbackmenu, name='feedbackmenu'),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    path('remove_item/<int:cart_id>/<str:item_number>/', views.remove_item_from_cart, name='remove_item_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

