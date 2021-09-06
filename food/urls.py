from django.urls import path
from .views import DishList,DishDetail

urlpatterns = [
    path('', DishList.as_view(), name='dishes_api'), 
    path('/<int:pk>', DishDetail.as_view(),name='dishes_details_api'),  
]