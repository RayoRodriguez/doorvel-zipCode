from django.urls import path
from .views import ZipCodeView

urlpatterns = [
    path('zipcode/', ZipCodeView.as_view(), name='settlements_list'),
    path('zipcode/<str:zip_code>', ZipCodeView.as_view(), name='settlements_process')
]