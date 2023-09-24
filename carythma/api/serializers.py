from rest_framework.serializers import ModelSerializer , ReadOnlyField
from .models import  DonneeECG , Client



class  DonneEcgSerializer(ModelSerializer):

    rythme_cardiaque =  ReadOnlyField()
    ratioprqt =  ReadOnlyField()
    rr_interval = ReadOnlyField()
    qtc =  ReadOnlyField()
    class Meta:
        model = DonneeECG
        fields = [
        'id',
        'interval_pr' ,
        'interval_qt',
        'rythme_cardiaque',
        'rr_interval',
        'qtc',
        'ratioprqt',
        'sante_patient'
        ]

class  LoginSerializer(ModelSerializer):
    class Meta:
        model  =  Client
        fields = ['id' , "phone" , 'password']


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'phone', 'password', 'first_name','last_name', 'date_naissance' , 'sex', 'numero_medecin']
