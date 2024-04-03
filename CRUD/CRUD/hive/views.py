from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Hive
from .serializers import HiveSerializer


class ProductViewSet(viewsets.ViewSet):
    def get_all(self, request):
        hives = Hive.objects.all()
        serializer = HiveSerializer(hives, many=True)
        return Response(serializer.data)

    def save(self, request):
        serializer = HiveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, pk=None):
        hive = Hive.objects.get(id=pk)
        serializer = HiveSerializer(hive)
        return Response(serializer.data)

    def update(self, request, pk=None):
        hive = Hive.objects.get(id=pk)
        serializer = HiveSerializer(instance=hive, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, pk=None):
        hive = Hive.objects.get(id=pk)
        hive.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)