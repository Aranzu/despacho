from django.contrib import admin
from django.urls import path, re_path, include
from . import views
from ingreso_orden.views import (
	orden_detail_view
	)
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("OrdenRetiro",views.OrdenRetiroApi, basename="OrdenRetiro")

urlpatterns = [
    path('',include(router.urls)),
    path('orden', orden_detail_view, name= "orden"),
]
