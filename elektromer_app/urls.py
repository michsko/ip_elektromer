from django.urls import path
from . import views
	
	
urlpatterns = [
    path('', views.home, name="home"),
    path('svj', views.svj, name="svj"),

    path('customer/<str:pk>', views.customer, name="customer"),
    path('customers', views.customers, name="customers"),
    path('customer_add', views.customer_add, name="customer_add"),
    path('customer_update/<str:pk>', views.customer_update, name="customer_update"), 
    path('customer_delete/<str:pk>', views.customer_delete, name="customer_delete"),

    #path('chairman', views.chairman, name="chairman"),
    #path('sub_chairman', views.sub_chairman, name="sub_chairman"),
    
    path('gsm_modul/<str:pk>', views.gsm_modul, name="gsm_modul"),
    path('gsm_moduls', views.gsm_moduls, name="gsm_moduls"),
    path('gsm_modul_add', views.gsm_modul_add, name="gsm_modul_add"),
    path('gsm_modul_update/<str:pk>', views.gsm_modul_update, name="gsm_modul_update"),
    path('gsm_modul_delete/<str:pk>', views.gsm_modul_delete, name="gsm_modul_delete"),

 
    path('flat', views.flat, name="flat"),

    path('main_electrometer/<str:pk>', views.main_electrometer, name="main_electrometer"),
    path('main_electrometers', views.main_electrometers, name="main_electrometers"),
    path('main_electrometer_add', views.main_electrometer_add, name="main_electrometer_add"),
    path('main_electrometer_update/<str:pk>', views.main_electrometer_update, name="main_electrometer_update"),
    path('main_electrometer_delete/<str:pk>', views.main_electrometer_delete, name="main_electrometer_delete"),

    path('sub_electrometer/<str:pk>', views.sub_electrometer, name="sub_electrometer"),
    path('sub_electrometers', views.sub_electrometers, name="sub_electrometers"),
    path('sub_electrometer_add', views.sub_electrometer_add, name="sub_electrometer_add"),
    path('sub_electrometer_update/<str:pk>', views.sub_electrometer_update, name="sub_electrometer_update"),
    path('sub_electrometer_delete/<str:pk>', views.sub_electrometer_delete, name="sub_electrometer_delete"),



    path('solar_electrometer/<str:pk>', views.solar_electrometer, name="solar_electrometer"),
    path('solar_electrometers', views.solar_electrometers, name="solar_electrometers"),
    path('solar_electrometer_add', views.solar_electrometer_add, name="solar_electrometer_add"),
    path('solar_electrometer_update/<str:pk>', views.solar_electrometer_update, name="solar_electrometer_update"),
    path('solar_electrometer_delete/<str:pk>', views.solar_electrometer_delete, name="solar_electrometer_delete"),

    #path('balance_main', views.balance_main, name="balance_main"),
    #path('balance_sub', views.balance_sub, name="balance_sub"),
    #path('balance_solar', views.balance_solar, name="balance_solar"),
    		
    	]
