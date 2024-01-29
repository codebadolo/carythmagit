from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import os
from twilio.rest import Client


class ClientManager(BaseUserManager): # ceci est  le manager des patient
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('The Phone field must be set')

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone, password, **extra_fields)






class Client(AbstractUser):
    phone = models.CharField(max_length=15 , unique=True, verbose_name='Téléphone')
    date_naissance = models.CharField( blank=False, max_length= 34 ,   verbose_name='Date de naissance')
    SEX_CHOICES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Non binaire', 'Non binaire'),
    ]
    sex = models.CharField(max_length=11, choices=SEX_CHOICES, verbose_name='Sexe')
    numero_medecin = models.CharField(null= False  , max_length= 16 ,  blank =  False , verbose_name= 'numero medecine' , default=  '+226' )
    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = ClientManager()  # Utilisation du gestionnaire d'utilisateurs personnalisé
    #etat_patient  = models.ForeignKey(DonneeECG, on_delete=models.CASCADE)
    def __str__(self):
        return self.phone

class   DonneeECG(models.Model):
    interval_pr  = models.IntegerField( default =1  )
    interval_qt  = models.IntegerField(null = False  )

    @property
    def ratioprqt(self):
        return self.interval_pr / self.interval_qt

    @property
    def rr_interval(self):
        '''interval_rr_moyen = (self.interval_pr + self.interval_qt) / 2
        court_interval_rr = interval_rr_moyen - (self.interval_qt / 2)
        long_interval_rr = interval_rr_moyen + (self.interval_qt / 2)
        return long_interval_rr - court_interval_rr'''
        return  self.interval_pr + self.interval_qt

    @property
    def frequence_cardiaque(self):
        return 60000 / self.rr_interval

    @property
    def qtc(self):
        return self.interval_qt + 1.75 * (self.frequence_cardiaque - 60)

    sante_patient   = models.CharField( verbose_name="etat patient", max_length= 50 ,  editable=False, blank=True, null=True)

    '''
    def save(self, *args, **kwargs):
         if self.sante_patient ==  "['Normale']":
            #twilio code

            account_sid = 'AC4f4516dd1894fa8d162842e79ae660d1'
            auth_token = '72017c407c0c855f9d7cdc7377f7528f'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
              from_='+16187871636',
              body='la sante de  votre pastient est  normal ',
              to='+22677797813'
            )
            return super().save(*args, **kwargs)

    '''

