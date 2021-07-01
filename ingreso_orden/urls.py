from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from ingreso_orden.views import (
	orden_detail_view, orden_detail_view2
	)
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("OrdenRetiro",views.OrdenRetiroApi, basename="OrdenRetiro")

urlpatterns = [
    path('',include(router.urls)),
    path('orden_p/<int:pk>/', orden_detail_view, name= "orden_p"),
    path('orden_g/<int:pk>/', orden_detail_view2, name= "orden_g"),
]
