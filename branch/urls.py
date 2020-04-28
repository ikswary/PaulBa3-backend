from django.urls import path
from branch.views import BranchView

urlpatterns = [
    path('/detail', BranchView.as_view()),
    path('/detail/<str:target_code>', BranchView.as_view())
]
