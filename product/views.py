from django.http import JsonResponse, HttpResponse
from django.views import View

from product.models import Product, Menu


class MenuView(View):
    def get_products_in_json(self, target):
        return [
            {
                'name_kor': product.name_kor,
                'name_eng': product.name_eng,
                'images': [image.url for image in product.image_set.all()],
                'is_new': product.is_new,
                'is_best': product.is_best,
            } for product in target.product_set.order_by('-is_new', '-is_best')
        ]

    def get(self, request, menu, category=None):
        try:
            target = Menu.objects.prefetch_related('category_set__product_set__image_set').get(name=menu)
            if category:
                result_list = self.get_products_in_json(target.category_set.get(id=category))
                return JsonResponse({'products': result_list}, status=200, json_dumps_params={'ensure_ascii': False})

            result_list = self.get_products_in_json(target)
            return JsonResponse({'products': result_list}, status=200, json_dumps_params={'ensure_ascii': False})

        except KeyError:
            return HttpResponse(status=404)

        except Menu.DoesNotExist:
            return HttpResponse(status=404)

class DetailView(View):
    def get_nutrient_list(self, product):
        nutrient_list = [
            {
                'kcal': nutrient.kcal,
                'protein': nutrient.protein,
                'sugar': nutrient.sugar,
                'sodium': nutrient.sodium,
                'fat': nutrient.fat,
                'caffeine': nutrient.caffeine,
                'serve': nutrient.serve,
                'serve_type': nutrient.serve_type
            } for nutrient in product.nutrient_set.all()
        ]

        return nutrient_list

    def get_product_info(self, product):
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
            info = DetailView.get_product_info(product)
            nutrient_list = DetailView.get_nutrient_list(product)

            return JsonResponse({'menu': menu, 'info': info, 'nutrients': nutrient_list})

        except Product.DoesNotExist:
            return HttpResponse(status=404)