from rest_framework import generics
from .models import Integer
from .serializers import IntegerSerializer
from .permissions import IsOwnerOrReadOnly


class IntegerList(generics.ListCreateAPIView):
    queryset = Integer.objects.all()
    serializer_class = IntegerSerializer

class IntegerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Integer.objects.all()
    serializer_class = IntegerSerializer
    permission_classes = (IsOwnerOrReadOnly,)