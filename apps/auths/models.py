"""MODELS AUTHS"""
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from game_characters.models import Character



class MyUserManager(BaseUserManager):
    """ClientManager."""

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'MyUser':

        if not email:
            raise ValidationError('Email required')

        custom_user: 'MyUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.is_active=True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
        return custom_user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'MyUser':

        custom_user: 'MyUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        custom_user.is_superuser = True
        custom_user.is_active = True
        custom_user.is_staff = True
        custom_user.set_password(password)
        custom_user.save(using=self._db)
    


class MyUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(
        verbose_name='почта',
        unique=True,
        max_length=200
    )
    username = models.CharField(
        verbose_name="никнейм",
        max_length=200
    )
    
    game_characters = models.ManyToManyField(
        verbose_name= 'ваши персонажи',
        to = Character ,
        blank=True,
        null=True
    )

    balance = models.DecimalField(
        verbose_name='баланс',
        max_digits=11,
        decimal_places=2,
        default=0,
        blank=True,
        null=True
    )

    
    is_staff = models.BooleanField(
        default=False
    )
    objects = MyUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'