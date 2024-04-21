from django.urls import path
from .views import Shop_Detail_View
urlpatterns = [
     path("shop_detail/", Shop_Detail_View.as_view(), name="shop_detail"),
]