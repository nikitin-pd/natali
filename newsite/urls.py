from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'newsite'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('reg_page/', views.reg_page, name='reg_page'),
    path('login_page/', views.login_page, name='login_page'),
    path('logout/', views.logout_page, name='logout_page'),
    path('add_service<int:service_id><int:project_id>/',
         views.add_service, name='add_service'),
    path('del_service<int:service_id>/', views.del_service, name='del_service'),
    path('contacts/', views.contacts, name='contacts'),
    path('profile/', views.profile, name='profile'),
    path('cart/', views.cart, name='cart'),
    path('create_order/', views.create_order, name='create_order')
]
