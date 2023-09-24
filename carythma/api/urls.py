from django.urls import path, include
from rest_framework import routers
from  .views import EcgViewset , ClientViewset

from django.contrib import admin

router = routers.SimpleRouter()
router.register('patient',  ClientViewset , basename='user')
router.register('ecg', EcgViewset, basename='iot')

urlpatterns = [
    path('apicarythma/', include(router.urls)),
]
