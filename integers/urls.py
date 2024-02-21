from django.urls import path, include
from .views import IntegerList, IntegerDetail
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = 'admin/logout/'

urlpatterns = [
    path("", IntegerList.as_view(), name="integer_list"),
    path("<int:pk>/", IntegerDetail.as_view(), name="integer_detail"),
]