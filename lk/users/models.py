import uuid

from django.db import models

# Абстрактная модель пользователя
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    COMPANY = 'COMP'
    PRIVATE_PERSON = 'PRIV'
    COMPANY_PRIVATE = [
        (COMPANY, 'Компания'),
        (PRIVATE_PERSON, 'Частное лицо')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(verbose_name='Наименование полное', max_length=250,
                                 unique=True, null=True, blank=True)
    status = models.CharField(verbose_name="Юр/Физлицо", max_length=50, choices=COMPANY_PRIVATE,
                              default=COMPANY)
