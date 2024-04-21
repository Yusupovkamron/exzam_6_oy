from django.shortcuts import render
from django.views import View
from users.models import Products,  Types, Discounts, Vegetables_new
from pages.models import Shop_Detail

class LandingPageView(View):
    def get(self, request):
        products = Products.objects.all(),
        types = Types.objects.all(),
        discounts = Discounts.objects.all(),
        vegetables_new = Vegetables_new.objects.all(),
        context = {
            'products': products,
            'types': types,
            'discounts': discounts,
            'vegetables_new': vegetables_new,
        }
        return render(request, "main/index.html", context)


