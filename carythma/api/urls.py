from django.urls import path, include
from rest_framework import routers
from  .views import EcgViewset #, ClientViewset  #, UserViewset , UserLogout
from django.contrib import admin

router = routers.SimpleRouter()
#router.register('patient',  ClientViewset , basename='user')
router.register('ecg', EcgViewset, basename='iot')

# Ici nous créons notre routeur
#routerauth = routers.SimpleRouter(trailing_slash=False)
# Puis lui déclarons une url basée sur le mot clé ‘category’ et notre view
# afin que l’url générée soit celle que nous souhaitons ‘/api/article/’
#routerauth.register(r'users', UserViewset, basename='users'),


urlpatterns = [
    #path('api/login/', UserViewset.as_view({'post': 'login_user'}), name='user-login'), #{'post': 'login_user'}
    #path('api/logout/', UserLogout.as_view(), name='user-logout'),
    #path('api/', include(routerauth.urls)),
    path('apicarythma/appmobile/', EcgViewset.as_view({'post': 'list'}), name='user-login'), #{'post': 'login_user'}
    path('apicarythma/', include(router.urls)),
    #path('api-auth/login', include('rest_framework.urls'))
#path('login', views.UserLogin.as_view(), name='login'),
    #======================================================

]
