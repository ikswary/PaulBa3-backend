from django.urls import path, include

urlpatterns = [
    path('menu', include('product.urls')),
    path('branch', include('branch.urls')),
    path('', include('member.urls')),
]
