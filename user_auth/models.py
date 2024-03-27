from django.db import models
import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, firstname, lastname, username, password, is_staff, is_superuser):
        if not username:
            raise ValueError('Users must have an email address')
        username = self.normalize_email(username)
        user = self.model(
            firstname=firstname,
            lastname=lastname,
            username=username,
            account_created = models.DateTimeField(auto_now_add=True),
            account_updated = models.DateTimeField(auto_now=True),
            is_staff=is_staff, 
            is_active=True,
            is_superuser=is_superuser, 
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, firstname, lastname , username, password):
        return self._create_user(firstname, lastname, username, password, False, False)

    def create_superuser(self, firstname, lastname , username, password):
        user=self._create_user(self, firstname, lastname , username, password)
        return user

class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.EmailField(max_length=254, unique=True)
    firstname = models.CharField(max_length=254)
    lastname = models.CharField(max_length=254)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    account_created = models.DateTimeField(auto_now_add=True)
    account_updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class UserEmailVerificationTrack(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.email
