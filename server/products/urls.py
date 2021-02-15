from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductDetail, ProductList

urlpatterns = [
    path('api/products/', ProductList.as_view()),
    path('api/products/<int:pk>/', ProductDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)