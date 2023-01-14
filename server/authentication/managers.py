from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, activity_role, password = None):
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            activity_role = activity_role,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, first_name, activity_role, password):
        user = self.create_user(
            email = email,
            first_name = first_name,
            activity_role = activity_role,
            password = password,
        )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user