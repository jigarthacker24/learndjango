
from django.contrib import admin
from django.urls import path
from .views import adminloginview,adminhomepageview,authenticateadmin, logoutadmin, addpizza,deletepizza

urlpatterns = [
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthenticate/',authenticateadmin),
    path('admin/homepage/',adminhomepageview,name='adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('addpizza/',addpizza),
    path('deletepizza/<int:pizzapk>/',deletepizza)
]