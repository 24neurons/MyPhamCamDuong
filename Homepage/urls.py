from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name = "index"),
    path("<str:productLine>/", views.ProductLine , name = "ProductLine" ) ,
    path("<str:productLine>/<str:productType>/" , views.ProductLine , name = "ProductType") ,
    path("<str:productLine>/<str:productType>/<str:productCode>/" , views.OneProduct , name = "OneProduct")
]