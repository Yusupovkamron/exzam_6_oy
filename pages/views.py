from django.shortcuts import render
from django.views import View
from .models import Shop_Detail
class Shop_Detail_View(View):
    def get(self, request):
        shop_detail = Shop_Detail.objects.all()
        contex = {
            "shop_detail": shop_detail
        }
        return render(request,"main/shop-detail.html", contex)