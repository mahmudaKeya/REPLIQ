from django.urls import path
from .views import CompanyListView



urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company_list'),
    # add other URL patterns here
]
