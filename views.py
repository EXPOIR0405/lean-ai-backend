
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import StoreInfo
from .serializers import StoreInfoSerializer

class StoreInfoViewSet(viewsets.ModelViewSet):
    queryset = StoreInfo.objects.all()
    serializer_class = StoreInfoSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_update(self, serializer):
        instance = self.get_object()
        if 'store_image' in self.request.data:
            instance.store_image.delete()
        serializer.save()