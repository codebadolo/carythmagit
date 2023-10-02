from rest_framework.serializers import ModelSerializer , ReadOnlyField
from .models import  DonneeECG , Client
from django.contrib.auth import get_user_model, authenticate
Client =  get_user_model()
from rest_framework import serializers

class  DonneEcgSerializer(ModelSerializer):

    frequence_cardiaque =  ReadOnlyField()
    ratioprqt =  ReadOnlyField()
    rr_interval = ReadOnlyField()
    qtc =  ReadOnlyField()
    class Meta:
        model = DonneeECG
        fields = [
        'id',
        'rr_interval',
        'interval_pr' ,
        'interval_qt',
        'frequence_cardiaque',
        'qtc',
        'ratioprqt',
        'sante_patient'
        ]
'''
class DonneeECGLess(ModelSerializer):
    frequence_cardiaque =  ReadOnlyField()
    class Meta:
        model  =  DonneeECG
        fields = [
         'interval_pr',
         'frequence_cardiaque',
         'sante_patient'

        ]'''
#selected_features = [ 'Interval-RR', 'Interval-PR','Interval-QT','frequence cardiaque', 'RatioPRQT', 'QTc']


'''
class  LoginSerializer(ModelSerializer):
    class Meta:
        model  =  Client
        fields = ["phone" , 'password']



class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'phone', 'password', 'first_name','last_name', 'date_naissance' , 'sex', 'numero_medecin']



'''



    ##
    #def check_user(self, clean_data):
        #user = authenticate(phone=clean_data['phone'], password=clean_data['password'])
        #if not user:
            #raise ValidationError('user not found')
        #return user

'''    def create(self, validated_data):
        user_obj = Client.objects.create_user(
            phone=validated_data['phone'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_naissance=validated_data['date_naissance'],
            sex=validated_data['sex'],
            numero_medecin=validated_data['numero_medecin']
        )
        return user_obj

'''
