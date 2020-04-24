from django.http import JsonResponse, HttpResponse
from django.views import View

from product.models import Product

class DetailView(View):
    def get(self, request):
        try:
            target = request.GET.get('product', None)
            info = dict()
            product = Product.objects.prefetch_related('nutrient_set__size',
                                                       'productallergycauses_set__allergy_causes',
                                                       'milkselection_set__milk').get(name_eng=target)

            menu = {
                'name_kor': product.name_kor,
                'name_eng': product.name_eng,
                'description': product.description,
            }

            if product.temperature:
                info['sort'] = product.temperature
            if len(product.milkselection_set.all()) > 0:
                info['milks'] = list()
                for milk in product.milkselection_set.all():
                    info['milks'].append(milk.milk.name)
            if len(product.productallergycauses_set.all()) > 0:
                info['allergy'] = list()
                for allergy_id in product.productallergycauses_set.all():
                    info['allergy'].append(allergy_id.allergy_causes.name)
            if len(product.nutrient_set.all()) > 0:
                info['sizes'] = list()
                for size_id in product.nutrient_set.all():
                    info['sizes'].append(size_id.size.name)

            nutrient_list = []
            for nutrient in product.nutrient_set.all():
                keys = list(nutrient.__dict__.keys())
                values = list(nutrient.__dict__.values())
                nutrients = dict()
                for i in range(4, len(keys) - 1):
                    nutrients[keys[i]] = values[i]
                nutrient_list.append(nutrients)

            return JsonResponse({'menu': menu, 'info': info, 'nutrient': nutrient_list})

        except Product.DoesNotExist:
            return HttpResponse(status=404)

