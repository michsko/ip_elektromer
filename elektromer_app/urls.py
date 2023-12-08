from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
	
	
urlpatterns = [
    path('', views.home, name="home"),

    path('balance_main/<str:pk>', views.balance_main, name="balance_main"),
    path('balances_main', views.balances_main, name="balances_main"),
    path('balance_main_add', views.balance_main_add, name="balance_main_add"),
    path('balance_main_update/<str:pk>', views.balance_main_update, name="balance_main_update"),
    path('balance_main_delete/<str:pk>', views.balance_main_delete, name="balance_main_delete"),

    path('balance_sub/<str:pk>', views.balance_sub, name="balance_sub"),
    path('balances_sub', views.balances_sub, name="balances_sub"),
    path('balance_sub_add', views.balance_sub_add, name="balance_sub_add"),
    path('balance_sub_update/<str:pk>', views.balance_sub_update, name="balance_sub_update"),
    path('balance_sub_delete/<str:pk>', views.balance_sub_delete, name="balance_sub_delete"),

    path('balance_solar/<str:pk>', views.balance_solar, name="balance_solar"),
    path('balances_solar', views.balances_solar, name="balances_solar"),
    path('balance_solar_add', views.balance_solar_add, name="balance_solar_add"),
    path('balance_solar_update/<str:pk>', views.balance_solar_update, name="balance_solar_update"),
    path('balance_solar_delete/<str:pk>', views.balance_solar_delete, name="balance_solar_delete"),
    
    path('count', views.count, name="count"),

    path('customer/<str:pk>', views.customer, name="customer"),
    path('customers', views.customers, name="customers"),
    path('customer_add', views.customer_add, name="customer_add"),
    path('customer_update/<str:pk>', views.customer_update, name="customer_update"), 
    path('customer_delete/<str:pk>', views.customer_delete, name="customer_delete"),

    path('flat/<str:pk>', views.flat, name="flat"),
    path('flats', views.flats, name="flats"),
    path('flat_add', views.flat_add, name="flat_add"),
    path('flat_update/<str:pk>', views.flat_update, name="flat_update"),
    path('flat_delete/<str:pk>', views.flat_delete, name="flat_delete"),

    path('gsm_modul/<str:pk>', views.gsm_modul, name="gsm_modul"),
    path('gsm_moduls', views.gsm_moduls, name="gsm_moduls"),
    path('gsm_modul_add', views.gsm_modul_add, name="gsm_modul_add"),
    path('gsm_modul_update/<str:pk>', views.gsm_modul_update, name="gsm_modul_update"),
    path('gsm_modul_delete/<str:pk>', views.gsm_modul_delete, name="gsm_modul_delete"),

    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),

    path('main_electrometer/<str:pk>', views.main_electrometer, name="main_electrometer"),
    path('main_electrometers', views.main_electrometers, name="main_electrometers"),
    path('main_electrometer_add', views.main_electrometer_add, name="main_electrometer_add"),
    path('main_electrometer_update/<str:pk>', views.main_electrometer_update, name="main_electrometer_update"),
    path('main_electrometer_delete/<str:pk>', views.main_electrometer_delete, name="main_electrometer_delete"),
   
    #path('chairman', views.chairman, name="chairman"),
    #path('sub_chairman', views.sub_chairman, name="sub_chairman"),
    path('overview', views.overview, name="overview"),

    path('register', views.registerPage, name='register'),



    path('reset_password',auth_views.PasswordResetView.as_view(), 
        name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(),
        name="password_reset_done"),
    path('reset/<uidb64>/<token>',
        auth_views.PasswordResetConfirmView.as_view(), 
        name='password_reset_confirrm'),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete"),

   


    path('solar_electrometer/<str:pk>', views.solar_electrometer, name="solar_electrometer"),
    path('solar_electrometers', views.solar_electrometers, name="solar_electrometers"),
    path('solar_electrometer_add', views.solar_electrometer_add, name="solar_electrometer_add"),
    path('solar_electrometer_update/<str:pk>', views.solar_electrometer_update, name="solar_electrometer_update"),
    path('solar_electrometer_delete/<str:pk>', views.solar_electrometer_delete, name="solar_electrometer_delete"),

    path('sub_electrometer/<str:pk>', views.sub_electrometer, name="sub_electrometer"),
    path('sub_electrometers', views.sub_electrometers, name="sub_electrometers"),
    path('sub_electrometer_add', views.sub_electrometer_add, name="sub_electrometer_add"),
    path('sub_electrometer_update/<str:pk>', views.sub_electrometer_update, name="sub_electrometer_update"),
    path('sub_electrometer_delete/<str:pk>', views.sub_electrometer_delete, name="sub_electrometer_delete"),

    path('svj/<str:pk>', views.svj, name="svj"),
    path('svjs', views.svjs, name="svjs"),
    path('svj_add', views.svj_add, name="svj_add"),
    path('svj_update/<str:pk>', views.svj_update, name="svj_update"),
    path('svj_delete/<str:pk>', views.svj_delete, name="svj_delete"),

    path('user', views.userPage, name="user"), 
    


    ]