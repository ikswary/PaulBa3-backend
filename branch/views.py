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
                'services': [service['service'] for service in branch.branchservice_set.values('service')]
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
            return JsonResponse({'branches': result}, status=200)

        except ObjectDoesNotExist:
            return HttpResponse(status=404)
