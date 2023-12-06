"""MODELS AUTHS"""
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from game_characters.models import Character
from PIL import Image


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
        'game_characters.Character',
        related_name='Персонажи',
        blank=True,  
    )

    balance = models.DecimalField(
        verbose_name='баланс',
        max_digits=11,
        decimal_places=2,
        default=0,
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        verbose_name='аватарка',
        upload_to='avatars/',  
        default='static/default_avatar.png',
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.avatar:
            img = Image.open(self.avatar.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.avatar.path)
    
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