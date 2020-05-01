from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.views import View

from branch.models import Area, Region, Branch


class BranchView(View):
    RESPONSE_ALL = '00'

    def each_branch_data(self, branches):
        return [
            {
                'shop_name': branch.shop_name,
                'address': branch.address,
                'tel': branch.tel,
                'latitude': branch.latitude,
                'longitude': branch.longitude,
                'services': list(branch.branchservice_set.values_list('service', flat=True))
            } for branch in branches
        ]

    def get(self, request, target_code=''):
        try:
            region_code = target_code[:1]
            area_code = target_code[1:]

            if not target_code:
                branches = Branch.objects.prefetch_related('branchservice_set')
            if area_code == self.RESPONSE_ALL:
                region = Region.objects.prefetch_related('branch_set__branchservice_set').get(code=region_code)
                branches = region.branch_set.all()
            if area_code != self.RESPONSE_ALL and area_code != '':
                area = Area.objects.prefetch_related('branch_set__branchservice_set').get(code=target_code)
                branches = area.branch_set.all()

            result = self.each_branch_data(branches)
            return JsonResponse({'branches': result}, status=200, json_dumps_params={'ensure_ascii': False})

        except ObjectDoesNotExist:
            return HttpResponse(status=404)

class AreaView(View):
    def get(self, request, target_code=''):
        try:
            region = Region.objects.prefetch_related('area_set__branch_set').get(code=target_code)

            area_info = [
                {
                    "area_name": area.name.strip(),
                    "area_code": area.code,
                    "clickable": area.branch_set.exists()
                } for area in region.area_set.all()
            ]
            area_info.insert(0, {"area_name": "전체", "area_code": target_code+"00", "clickable": True})

            return JsonResponse({"area_info": area_info}, status=200)
        except Region.DoesNotExist:
            return HttpResponse(status=404)
