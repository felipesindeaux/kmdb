from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)

        user = self.model(email=email, is_staff=True, is_superuser=True, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)

        user = self.model(email=email, is_staff=True, is_superuser=False, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user
