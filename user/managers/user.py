from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    def normalize_national_code(self, national_code):
        """
        normalize national_code
        """
        # TODO
        # normalize_national_code
        return national_code

    def normalize_phone_number(self, phone_number):
        """
        normalize phone_number
        """
        # TODO
        # phone_number
        return phone_number

    def create_user(self, national_code, phone_number, password):
        """
        Creates and saves a User with the given national_code and password.
        """
        if not national_code:
            raise ValueError('Users must have an national_code')

        if not phone_number:
            raise ValueError('Users must have an phone_number')

        if not password:
            raise ValueError('Users must have an password')

        user = self.model(
            national_code=self.normalize_national_code(national_code),
            phone_number=self.normalize_phone_number(phone_number),
        )

        user.set_password(password)
        user.is_active = False
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)

        return user

    def create_superuser(self, national_code, phone_number, password):
        """
        Creates and saves a superuser with the given national_code and password.
        """
        user = self.create_user(
            national_code,
            password=password,
            phone_number=phone_number,
        )
        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user
