from django.urls import path
from newapp import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('register/',views.registration,name="register"),
    path('login/',views.login,name="login"),
    path('profile/',views.profile,name="profile"),
    path('edit/',views.edit_profile,name="edit_profile"),
    path('home/',views.home,name="home"),
    path('product_register/',views.product_register,name="product_register"),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('product_list/',views.product_list,name="product_list"),
    path('admin_dashboard/',views.admin_dashboard,name="admin_dashboard"),
    path('admin_product_list/',views.admin_product_list,name="admin_product_list"),
    path('edit_product/<int:id>/',views.edit_product,name="edit_product"),
    path('delete_product/<int:id>/',views.delete_product,name="delete_product"),
    path('admin-login/', views.admin_login, name='admin_login'),
    path('registor_list/', views.registor_list, name='registor_list'),
    path('delete_registor/<int:id>/', views.delete_registor, name='delete_registor'),
    path('add_to_cart/<int:id>/',views.add_to_cart,name="add_to_cart"),
    path('cart_list/',views.cart_list,name="cart_list"),

]