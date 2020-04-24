from django.urls import path, include

urlpatterns = [
    path('menu', include('product.urls'))
]
