from rest_framework import viewsets
from .models import Client
from .serializers import ClientSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ClientSerializer
from .models import Client
from rest_framework import viewsets


class ClientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def retrieve(self, request, card_number=None, *args, **kwargs):
        query_params = request.query_params
        if 'card_number' in query_params:
            queryset = Client.objects.all()
            client = get_object_or_404(queryset, card_number=query_params['card_number'][:-1])
            serializer_context = {'request': request,}
            serializer = ClientSerializer(client, context=serializer_context)
            return Response(serializer.data)
