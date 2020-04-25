from django.urls import path
from .views import MenuView, DetailView

urlpatterns = [
    path('/detail', DetailView.as_view()),
    path('/<str:menu>/<str:category>', MenuView.as_view()),
    path('/<str:menu>', MenuView.as_view()),
]