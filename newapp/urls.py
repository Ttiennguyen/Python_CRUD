from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.add,name="add"),
    path("addrec/",views.addrec,name="addrec"),
    path('delete/<int:id>/',views.delete,name="delete"),
    path('update/<int:id>/',views.update,name="update"),
    path('update/uprec/<int:id>/',views.uprec,name="uprec"),

    path('indexlogin/',views.indexlogin,name="indexlogin"),
    path('addlogin/',views.addlogin, name = "addlogin"),
    path('addreclogin/',views.addreclogin,name="addreclogin"),
    path('loginview/',views.loginview,name="login"),
    path('logincheck/',views.logincheck,name="logincheck"),
    path('indexlogin/deleteacc/<int:id>/',views.deleteacc, name="deleteacc")
]