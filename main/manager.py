from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self,user_id, password = None, **extra_fields):
        if not user_id:
            raise ValueError('User Id is required')
        # extra_fields['email'] = self.normalize_email(extra_fields['email'])
        user = self.model(user_id=user_id,**extra_fields)
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self,user_id,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(user_id,password,**extra_fields)