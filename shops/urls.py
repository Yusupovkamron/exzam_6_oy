from django.urls import path
from .views import Shops_View

urlpatterns = [
     path("shops_view/", Shops_View.as_view(), name="shops_view"),
]