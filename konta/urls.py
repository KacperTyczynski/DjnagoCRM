from django.urls import path
from . import views

urlpatterns = [

    path('rejestracja/', views.rejestracja, name="rejestracja"),
	path('logowanie/', views.logowanie, name="logowanie"),  
	path('logout/', views.wylogowanie, name="logout"),


    path('', views.home, name = "home"),
    path('produkty/', views.produkty, name = "Produkty"),
    path('produkt/<str:pk>/', views.produkt, name = "produkt"),
    path('klient/<str:pk_test>', views.klient, name = "Klient"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.aktualizujZamowienie, name="update_order"),
    path('delete_order/<str:pk>', views.usunZamowienie, name="delete_order"),

]
