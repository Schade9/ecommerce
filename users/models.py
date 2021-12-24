from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField

#pip install django-phonenumber-field[phonenumberslite]

# Create your models here.

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
    (2, 'not specified'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #phone_number = PhoneNumberField(unique=True, max_length=10, null=False, blank=False)
    gender = models.IntegerField(choices=GENDER_CHOICES, default=2)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

# to access phone number
# phonenumber = user.profile.phone_number.as_e164