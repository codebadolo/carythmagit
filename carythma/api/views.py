import numpy as np
from django.http import HttpResponseRedirect
from .serializers import   DonneEcgSerializer , ClientSerializer , LoginSerializer
from rest_framework.viewsets import ModelViewSet
from django.views import View
from django.http import JsonResponse
import pickle
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from  .models  import  DonneeECG , Client
import joblib
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import  login, logout, authenticate
from rest_framework import viewsets, permissions, status

# view  ecg et prediction

class EcgViewset(ModelViewSet):
    #queryset     =  DonneeECG.objects.all()
    serializer_class = DonneEcgSerializer
    def get_queryset():
        DonneeECG.objects.all()

    def perform_create(self,serializer) :
        interval_pr  =  self.request.data.get("intevral_pr"  )
        interval_qt =self.request.data.get("interval_qt" )
        ratioprqt =  self.request.data.get("ratioprqt" )
        rr_interval  =self.request.data.get("rr_interval" )
        rythme_cardiaque = self.request.data.get("rythme_cardiaque"  )
        qtc = self.request.data.get("ratioprqt" )


        #transformer nos champs en  taableau
        X = np.array([
            rr_interval,
            interval_pr,
            interval_qt,
            rythme_cardiaque,
            ratioprqt,
            qtc

        ])
        #selected_features = ['Interval-RR', 'Interval-PR', 'Interval-QT', 'RYTHME CARDIAQUE', 'RatioPRQT', 'QTc']

        X = X.reshape(1 , -1)
        def open_test_data():
            return open('/home/codewithbadolo/apiosc23carythma/carythmaosc23/modelcarythmagd.joblib', 'rb')

        with open_test_data() as f:
            model   = joblib.load(f)
        #model = pickle.load('modelcarythma.pkl')
        #moddel loding process
        pred = model.predict(X)
        # model  pprediction

        #souvegarde de la serialisation et du resultat du model
        serializer.save(sante_patient = pred)


# debut de la vue du patient



class ClientViewset(ModelViewSet):
    #queryset =   Client.objects.all()
    serializer_class =  ClientSerializer
    #permission_classes = (permissions.AllowAny,)
    queryset  = Client.objects.all()

    # Vue de connexion personnalisée

'''
    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data['phone']
            password = serializer.validated_data['password']

            # Authenticate the user
            user = Client.objects.filter(phone=phone, password=password).first()

            if user:
                # Successfully authenticated
                return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
            else:
                # Authentication failed
                return Response({'error': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Invalid data in the request
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
'''
class LoginView(APIView):
    serializer_class  = LoginSerializer

    def login_user(self, request):
        phone = request.data.get('phone')
        password = request.data.get('password')
        # Vérifiez les informations de connexion
        user = authenticate(request, phone=phone, password=password)

        if user:
            login(request, user)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'Connexion refusée veuillez verifer vos identifiants'}, status=status.HTTP_401_UNAUTHORIZED)
'''

'''
class UserLogout(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Déconnexion de l'utilisateur
        logout(request)
        return Response({"message": "Déconnexion réussie."}, status=status.HTTP_200_OK)
'''
