from django.shortcuts import render
from django.views import View
from .models import Shops
class Shops_View(View):
    def get(self, request):
        shops_view = Shops.objects.all()
        contex = {
            "shops_view": shops_view,
        }
        return render(request,"main/shop.html", contex)