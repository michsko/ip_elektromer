from django.urls import path
from . import views
	
	
urlpatterns = [
    path('', views.home, name="home"),
    path('svj', views.svj, name="svj"),
    path('customer/<str:pk>', views.customer, name="customer"),
    path('customers', views.customers, name="customers"),

    #path('chairman', views.chairman, name="chairman"),
    #path('sub_chairman', views.sub_chairman, name="sub_chairman"),
    
    path('gsm_modul', views.gsm_modul, name="gsm_modul"),
    path('flat', views.flat, name="flat"),
    path('main_electrometer', views.main_electrometer, name="main_electrometer"),
    path('sub_electrometer', views.sub_electrometer, name="sub_electrometer"),
    path('solar_electrometer', views.solar_electrometer, name="solar_electrometer"),
    
    #path('balance_main', views.balance_main, name="balance_main"),
    #path('balance_sub', views.balance_sub, name="balance_sub"),
    #path('balance_solar', views.balance_solar, name="balance_solar"),
    		
    	]
