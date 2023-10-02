from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from  api.models  import   Client

Client = get_user_model()

def custom_validation(data):
    #email = data['email'].strip()
    phone = data['phone'].strip()
    password = data['password'].strip()
    first_name = data['first_name'].strip()
    last_name = data['last_name'].strip()
    date_naissance = data['date_naissance'].strip()
    sex = data['sex'].strip()
    numero_medecin = data['numero_medecin'].strip()

#'first_name','last_name', 'date_naissance' , 'sex', 'numero_medecin']
    ##
    if not phone or Client.objects.filter(phone=phone).exists():
        raise ValidationError('choose another phone')
    ##
    if not password or len(password) < 8:
        raise ValidationError('choose another password, min 8 characters')
    ##
    if not first_name:
        raise ValidationError('choose another first_name')
    return data
    if not last_name:
        raise ValidationError('choose another last name')
    return data
    if not date_naissance:
        raise ValidationError('choose another  date of both ')
    return data

    if not sex:
        raise ValidationError('choose another username')
    return data




def validate_phone(data):
    phone = data['phone'].strip()
    if not phone:
        raise ValidationError('an email is needed')
    return True

def validate_sex(data):
    sex = data['sex'].strip()
    if not sex:
        raise ValidationError('an email is needed')
    return True

def validate_numero_medecin(data):
    numero_medecin = data['numero_medecin'].strip()
    if not numero_medecin:
        raise ValidationError('an email is needed')
    return True

def validate_first_name(data):
    first_name = data['first_name'].strip()
    if not first_name:
        raise ValidationError('an email is needed')
    return True

def validate_last_name(data):
    last_name = data['last_name'].strip()
    if not last_name:
        raise ValidationError('an email is needed')
    return True


def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True
def validate_date_naissance(data):
    date_naissance = data['date_naissance'].strip()
    if not date_naissance:
        raise ValidationError('a password is needed')
    return True
