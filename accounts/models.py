from django.contrib.auth.models import User
from django.db import models
from django.db.models import *


# Create your models here.
class Profile(Model):
    # OneToOneField inseamna un singur profil pentru un singur user, si invers
    # on_delete=CASCADE inseamna ca atunci cand se sterge un User
    # sa va sterge automat si obiectul de profil asociat
    user = OneToOneField(User, on_delete=CASCADE)

    biography = TextField()

    def __str__(self):
        return f'Profile for {self.user.username}'