from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from  api.models  import Client
Client = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = ['id', 'phone', 'password', 'first_name','last_name', 'date_naissance' , 'sex', 'numero_medecin']
	'''def create(self, clean_data):
		user_obj = Client.objects.create_user(
            phone=clean_data['phone'],
            password=clean_data['password']
		)
		user_obj.first_name=clean_data['first_name']
		user_obj.last_name=clean_data['last_name']
		user_obj.date_naissance=clean_data['date_naissance']
		user_obj.sex=clean_data['sex']
		user_obj.numero_medecin=clean_data['numero_medecin']

		user_obj.save()
		return user_obj
	'''

class UserLoginSerializer(serializers.Serializer):
	phone = serializers.CharField()
	password = serializers.CharField()
	##
	def check_user(self, clean_data):
		user = authenticate(phone=clean_data['phone'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		#fields = ('email', 'username')
		fields = ['id', 'phone', 'password', 'first_name','last_name', 'date_naissance' , 'sex', 'numero_medecin']
