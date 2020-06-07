from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import (PermissionsMixin, BaseUserManager, AbstractBaseUser)
from django.utils.translation import ugettext_lazy as _



class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,

        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
        
    def create_student(self, email, password=None):
        """
        Creates and saves a student with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_student = True
        user.save(using=self._db)
        return user

    def create_teacher(self, email, password=None):
        """
        Creates and saves a teacher with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_teacher = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),db_index=True, unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_verified = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
   
    objects = UserManager()

    USERNAME_FIELD = ('email')

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)




        