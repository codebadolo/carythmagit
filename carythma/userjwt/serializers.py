from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import   Client
class SignUpSerializer(serializers.ModelSerializer):
    '''
    phone = serializers.CharField(max_length=15)
    password =  serializers.CharField(max_length = 10)
    #email = serializers.EmailField()
    first_name = serializers.CharField(max_length = 20)
    password =  serializers.CharField(max_length = 10)
    last_name =  serializers.CharField(max_length = 10)

    date_naissance =  serializers.CharField(  max_length= 34 )
    SEX_CHOICES = [
            ('Homme', 'Homme'),
            ('Femme', 'Femme'),
            ('Non binaire', 'Non binaire'),
    ]
    sex =  serializers.CharField(max_length=11)
    numero_medecin =  serializers.CharField( max_length= 16  , default=  '+226' )
    '''



    class Meta:
        model = Client
        fields = ['id', 'phone', 'password', 'first_name','last_name', 'date_naissance' , 'sex', 'numero_medecin']

    def create(self,validated_data):
        #del validated_data['confirm_password']
        user = Client.objects.create_user(**validated_data)
        return user
    '''
    #def validate(self,value):

        if value.get('password') : # != value.get('confirm_password'):
            raise serializers.ValidationError('Both the passwords does not match')
        return value
    '''
'''
{

            "phone": "075155689",
            "password": "4ser1@1111",
            "first_name": "ba3ooo",
            "last_name": "asake",
            "date_naissance": "2023-07-34",
            "sex": "Femme",
            "numero_medecin": "+22677797378"
        }

'''
