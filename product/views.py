from django.http import JsonResponse, HttpResponse
from django.views import View

from product.models import Menu, Category

def get_products_in_json(target):
    return [{
        'name_kor': product.name_kor,
        'name_eng': product.name_eng,
        'images': [image.url for image in product.image_set.all()],
        'is_new': product.is_new,
        'is_best': product.is_best,
    } for product in target.product_set.all()]

class MenuView(View):
    def get(self, request, menu, category=None):
        try:
            target = Menu.objects.prefetch_related('category_set__product_set__image_set').get(name=menu)
            if category:
                result_list = get_products_in_json(target.category_set.get(id=category))
                return JsonResponse({'products': result_list}, status=200, json_dumps_params={'ensure_ascii': False})

            result_list = get_products_in_json(target)
            return JsonResponse({'products': result_list}, status=200, json_dumps_params={'ensure_ascii': False})

        except KeyError:
            return HttpResponse(status=404)

        except Menu.DoesNotExist:
            return HttpResponse(status=404)
