
from django.contrib import admin
from django.urls import path
from .views import acceptorder,declineorder,adminorders,adminloginview,adminhomepageview,authenticateadmin, logoutadmin, addpizza,deletepizza
from .views import userorders,logoutuser,customerpageview,homepageview,signupuser,userloginview,userauthenticate,placeorder
urlpatterns = [

    #admin urls
    path('admin/', adminloginview, name='adminloginpage'),
    path('adminauthenticate/',authenticateadmin),
    path('admin/homepage/',adminhomepageview,name='adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('addpizza/',addpizza),
    path('deletepizza/<int:pizzapk>/',deletepizza),
    path('adminorders/',adminorders),
    path('acceptorder/<int:orderpk>/',acceptorder),
    path('declineorder/<int:orderpk>/',declineorder),

    #user urls
    path('',homepageview,name='homepage'),
    path('usersignup/',signupuser),
    path('userloginpage/',userloginview,name='userloginpage'),
    path('userauthenticate/',userauthenticate),
    path('customer/welcome/',customerpageview, name='customerpage'),
    path('userlogout/',logoutuser),
    path('placeorder/',placeorder),
    path('userorders/',userorders)
]
