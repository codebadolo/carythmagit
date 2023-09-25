from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager



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

    #phone = models.CharField(max_length=15, unique=True, verbose_name='Téléphone')
    #date_naissance = models.DateField(null=True, blank=True, verbose_name='Date de naissance')

    SEX_CHOICES = [
        ('Homme', 'Homme'),
        ('Femme', 'Femme'),
        ('Non binaire', 'Non binaire'),
    ]
    sex = models.CharField(max_length=11, choices=SEX_CHOICES, verbose_name='Sexe')

    #numero_medecin = models.CharField(  verbose_name= 'numero medecine'  ,null= False  , max_length= 16 , db_column ='numer_medecin')

    numero_medecin = models.CharField(null= False  , max_length= 16 ,  blank =  False , verbose_name= 'numero medecine' , default=  '+226' )

    username = None

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = ClientManager()  # Utilisation du gestionnaire d'utilisateurs personnalisé

    def __str__(self):
        return self.phone


#ceci  marque la  fin du model  patient danss  notre cas

class   DonneeECG(models.Model):
    interval_pr  = models.IntegerField( default =1  )
    interval_qt  = models.IntegerField(null = False  )

    @property
    def ratioprqt(self):
        return self.interval_pr / self.interval_qt

    @property
    def rr_interval(self):
        interval_rr_moyen = (self.interval_pr + self.interval_qt) / 2
        court_interval_rr = interval_rr_moyen - (self.interval_qt / 2)
        long_interval_rr = interval_rr_moyen + (self.interval_qt / 2)
        return long_interval_rr - court_interval_rr

    @property
    def rythme_cardiaque(self):
        return 60000 / self.rr_interval

    @property
    def qtc(self):
        return self.interval_qt + 1.75 * (self.rythme_cardiaque - 60)

    sante_patient   = models.CharField(verbose_name="etat patient", max_length= 10 ,  editable=False, blank=True, null=True)
