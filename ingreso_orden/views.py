from django.shortcuts import render
import requests
from rest_framework.response import Response
from .models import OrdenRetiro
from .serializers import OrdenRetiroSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic import ListView, TemplateView
from django.http import HttpResponseRedirect
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
)
# Create your views here.
class OrdenRetiroApi(viewsets.ModelViewSet):
    queryset = OrdenRetiro.objects.all()
    serializer_class = OrdenRetiroSerializer

@api_view(['POST'])
def orden_detail_view(request):
    serializer = OrdenRetiroSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)

    return Response(serializer.data)

@api_view(['GET'])
def orden_detail_view2(request,pk=None):
	if request.method == 'GET':
		ordenRetiro = OrdenRetiro.objects.filter(rut=pk).first()
		if ordenRetiro == None:
			return Response("No existe la orden de retiro ingresada.")
		else:
			ordenRetiro_serializer= OrdenRetiroSerializer(ordenRetiro)
			return Response(ordenRetiro_serializer.data)