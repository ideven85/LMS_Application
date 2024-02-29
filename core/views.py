from django.shortcuts import render
from django.urls import path
from rest_framework_swagger.views import get_swagger_view


# Create your views here.
def get_client_ip_address(request):
    req_headers = request.META
    x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for_value:
        ip_addr = x_forwarded_for_value.split(',')[-1].strip()
    else:
        ip_addr = req_headers.get('REMOTE_ADDR')
    return ip_addr


schema_view = get_swagger_view(title='LMS API')

