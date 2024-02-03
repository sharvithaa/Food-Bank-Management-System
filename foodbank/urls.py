"""
URL configuration for foodbank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    #path('app/', include('foodbank.urls', namespace='app')),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login_view,name='login'),
    path('donate/',views.food_donation_form,name='donation'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('donate/donate/',views.donatesuccess,name='donatesuccess'),
    path('donate/donate/homepage',views.home,name='home'),
    path('order/',views.order_page,name='order'),
    path('post/',views.food_items,name='items'),
    path('deliverlogin',views.delivery,name='delivery'),
    path('dashboard/',views.dashboard,name='dashborad'),
    path('accept_order/', views.accept_order, name='accept_order'),
    path('login/signup',views.signup,name='signup')
]
