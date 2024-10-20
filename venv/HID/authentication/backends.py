from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class HidPinBackend(BaseBackend):
    def authenticate(self, request, hid=None, pin=None, **kwargs):
        try:
            profile = Profile.objects.get(hid=hid)
            if profile.pin == pin:
                return profile.user
        except ObjectDoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None