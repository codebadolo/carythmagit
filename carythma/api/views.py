import numpy as np
from django.http import HttpResponseRedirect
from .serializers import   DonneEcgSerializer  #,  DonneeECGLess #, ClientSerializer , LoginSerializer
from rest_framework.viewsets import ModelViewSet
from django.views import View
from django.http import JsonResponse
import pickle
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from  .models  import  DonneeECG , Client
import joblib
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import  login, logout, authenticate
from rest_framework import viewsets, permissions, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# view  ecg et prediction
from .filters  import  DonneeECGFilter
from django.db.models import Q
class EcgViewset(ModelViewSet):
    #queryset     =  DonneeECG.objects.all()
    serializer_class = DonneEcgSerializer
    #filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    #ordering_fields = '__all__'  # Fields you can order by
    #search_fields = ['field_name']  # Fields you can search by
    #filterset_fields = ['sante_patient','interval_pr', 'frequence_cardiaque' ]  # Fields you want to filter on
    #filterset_class = DonneeECGFilter  # Use the custom filter class

    def get_queryset(self):
        return DonneeECG.objects.all()#.filter('intevral_pr' , 'frequence_cardiaque' , 'sante_patient')

    def perform_create(self,serializer) :
        interval_pr  =  self.request.data.get("intevral_pr"  )
        interval_qt =self.request.data.get("interval_qt" )
        ratioprqt =  self.request.data.get("ratioprqt" )
        rr_interval  =self.request.data.get("rr_interval" )
        frequence_cardiaque = self.request.data.get("frequence_cardiaque"  )
        qtc = self.request.data.get("ratioprqt" )


        #transformer nos champs en  taableau
        X = np.array([
            rr_interval,
            interval_pr,
            interval_qt,
            frequence_cardiaque,
            ratioprqt,
            qtc

        ])
        #selected_features = ['Interval-RR', 'Interval-PR', 'Interval-QT', 'RYTHME CARDIAQUE', 'RatioPRQT', 'QTc']

        X = X.reshape(1 , -1)
        #def open_test_data():
            #return open('/home/codewithbadolo/apiosc23carythma/carythmaosc23/modelcarythmagd.joblib', 'rb')
        def open_test_data():
            return open('/home/codewithbadolo/osc/carythma/api/modelcarythma/modelcarythmagdpickle.pkl', 'rb')
        with open_test_data() as f:
            model = pickle.load(f)

        #with open_test_data() as f:
            #model   = joblib.load(f)
        #model = pickle.load('modelcarythma.pkl')
        #moddel loding process
        pred = model.predict(X)
        # model  pprediction

        #souvegarde de la serialisation et du resultat du model
        serializer.save(sante_patient = pred)

    '''def list(self, request, *args, **kwargs):
        queryset = DonneeECG.objects.all().only('interval_pr','frequence_cardiaque', 'sante_patient')
        serializer = DonneeECGLess(queryset, many=True)
        return Response(serializer.data)'''
'''

# debut de la vue du patient
class ClientViewset(ModelViewSet):
    serializer_class =   ClientSerializer
    permission_classes = (permissions.AllowAny,)
    queryset  = Client.objects.all()


class  UserViewset(ModelViewSet):
    serializer_class =   LoginSerializer
    #authentication_classes = [SessionAuthentication, TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    permission_classes = (permissions.AllowAny,)


    def get_queryset(self):
        return Client.objects.all()


    def login_user(self, request):
        phone = request.data.get("phone")
        password = request.data.get("password")


        phone =  validated_data.get('phone')
        password = validated_data.get('password')

        # Vérifiez les informations de connexion
        user = authenticate(request, phone= phone , password=password)

        if  user:
            login(request, user)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Connexion refusée veuillez verifer vos identifiants'}, status=status.HTTP_401_UNAUTHORIZED)


class UserLogout(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Déconnexion de l'utilisateur
        logout(request)
        return Response({"message": "Déconnexion réussie."}, status=status.HTTP_200_OK)



















'''






'''


class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		assert validate_phone(data)
		assert validate_password(data)
		serializer = LoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)

'''
