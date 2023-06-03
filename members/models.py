from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class CustomUser(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    email = models.EmailField(max_length=79, unique=True)
    first_name = models.CharField(max_length=50, verbose_name='Prénom')
    last_name = models.CharField(max_length=50, verbose_name='Nom')
    is_staff = models.BooleanField(default=False)

# Create your models here.
