from django.urls import path, include
from rest_framework import routers
from  .views import EcgViewset , ClientViewset

from django.contrib import admin

router = routers.SimpleRouter(trailing_slash=False)
router.register('patient',  ClientViewset , basename='user')
router.register('ecg', EcgViewset, basename='iot')

urlpatterns = [
    path('apicarythma/login/', ClientViewset.as_view({'post': 'login_user'}), name='user-login'),
    path('apicarythma/', include(router.urls)),
]
