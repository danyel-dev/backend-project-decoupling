from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ListSerializer, ItemSerializer
from .models import List, Item


class ListViewSet(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        return List.objects.filter(user=self.request.user)


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.order_by('-id')
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]


@api_view()
def testeAPI(request):
    return Response('ok')
