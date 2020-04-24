from django.http import JsonResponse, HttpResponse
from django.views import View

from product.models import Product

def get_nutrient_list(product):
    nutrient_list = []
    for nutrient in product.nutrient_set.all():
        keys = list(nutrient.__dict__.keys())
        values = list(nutrient.__dict__.values())
        nutrients = dict()
        for i in range(4, len(keys) - 1):
            nutrients[keys[i]] = values[i]
        nutrient_list.append(nutrients)
    return nutrient_list

def get_product_info(product):
    info = dict()
    if product.temperature:
        info['sort'] = product.temperature
    if len(product.milkselection_set.all()) > 0:
        info['milks'] = [milk.milk.name for milk in
                         product.milkselection_set.all()]
    if len(product.productallergycauses_set.all()) > 0:
        info['allergy'] = [allergy.allergy_causes.name
                           for allergy in product.productallergycauses_set.all()]
    if len(product.nutrient_set.all()) > 0:
        info['sizes'] = [size.size.name for size in product.nutrient_set.all()]

    return info

class DetailView(View):
    def get(self, request):
        try:
            target = request.GET.get('product', None)
            product = Product.objects.prefetch_related('nutrient_set__size',
                                                       'productallergycauses_set__allergy_causes',
                                                       'milkselection_set__milk').get(name_eng=target)

            menu = {
                'name_kor': product.name_kor,
                'name_eng': product.name_eng,
                'description': product.description,
            }
            info = get_product_info(product)
            nutrient_list = get_nutrient_list(product)

            return JsonResponse({'menu': menu, 'info': info, 'nutrients': nutrient_list})

        except Product.DoesNotExist:
            return HttpResponse(status=404)
