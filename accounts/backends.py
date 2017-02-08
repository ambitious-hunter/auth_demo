from models import User


class EmailAuth(object):
    """
    Get and instance of User using the supplied email and check it's password
    """
    def authenticate(selfself, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        """
        Used by the django authentication system to retrieve to retrieve an instance of User
        """

        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None