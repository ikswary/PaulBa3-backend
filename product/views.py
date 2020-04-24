from django.http import JsonResponse, HttpResponse
from django.views import View

from product.models import Menu, Category

category_map = {
    'c1': 'Coffee',
    'c2': 'Latte',
    'c3': 'Espresso',
    'c4': 'Cold Brew',
    'c5': 'Single Origin',
    'b1': 'Frappe',
    'b2': 'Tea Latte',
    'b3': 'Ade · Juice',
    'b4': 'Tea',
    'b5': 'Chocolate',
    'b6': 'Yogurt',
    'i1': 'Milk Ice-Cream',
    'i2': 'Season Ice-Cream',
    'f1': 'Bakery',
    'f2': 'Morning foods',
    'f3': 'Nata',
    'f4': 'Cake · Dessert',
    'p1': 'Barista Pouch',
    'p2': 'Whole Bean',
    'p3': 'Tumbler',
    'p4': 'Mug',
    'p5': 'ETC'
}

def get_category_products(target):
    result_list = []
    for product in target.product_set.all():
        product_dict = {
            'name_kor': product.name_kor,
            'name_eng': product.name_eng,
            'images': [image.url for image in product.image_set.all()]
        }
        result_list.append(product_dict)
    return result_list

class MenuView(View):
    def get(self, request, menu, category=None):
        try:
            if category is not None:
                this_category = category_map[category]
                target = Category.objects.prefetch_related('product_set__image_set').get(name=this_category)
            if category is None:
                target = Menu.objects.prefetch_related('product_set__image_set').get(name=menu)

            result_list = get_category_products(target)
            return JsonResponse({'products': result_list}, status=200, json_dumps_params={'ensure_ascii': False})

        except KeyError:
            return HttpResponse(status=404)

        except Menu.DoesNotExist:
            return HttpResponse(status=404)
