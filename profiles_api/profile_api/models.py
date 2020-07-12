from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """manager for user profiles"""
    
    def create_user(self,email,name,password=None):
        """Create new users"""
        if not email:
            raise ValueError("User must have a valid email")
        email = self.normalize_email(email)
        user = self.model(email=email,password=password)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
        
    def create_superuser(self,email,name,password):
        """Create suprt user"""
        user = self.create_user(email,name,password)
        print(user)
        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)
        
        return user

class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for user in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    
    
    object = UserProfileManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']
    
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    def __str__(self):
        return self.email

# Create your models here.
