
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Dish
from .serializers import DishSerializer
# Create your views here.


class DishList(ListCreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class DishDetail(RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer