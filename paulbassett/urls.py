from django.urls import path, include

urlpatterns = [
    path('menu', include('product.urls')),
    path('', include('member.urls')),
]
