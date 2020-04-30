from django.urls import path
from .views import MenuView, DetailView

urlpatterns = [
    path('/detail/<int:target>', DetailView.as_view()),
    path('/<str:menu>/<int:category>', MenuView.as_view()),
    path('/<str:menu>', MenuView.as_view()),
]