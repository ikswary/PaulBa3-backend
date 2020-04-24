from django.urls import path
from .views import MenuView

urlpatterns = [
    path('/<str:menu>/<str:category>', MenuView.as_view()),
    path('/<str:menu>', MenuView.as_view()),
]