from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),
	path('', views.landingpage, name = "landing"),
    path('home/', views.home, name = "home"),
    path('user/', views.userPage, name = "user-page"),
	path('forecasting/', views.forecasting, name="forecasting"),
	path('create_customer/', views.create_customer, name="create_customer"),
	path('create_product/', views.create_product, name="create_product"),
    path('customer/<str:pk_test>/', views.customer, name = "customer"),
    path('products/', views.products, name = "products"),

    path('create_order/<str:pk>/', views.createOrder , name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]
