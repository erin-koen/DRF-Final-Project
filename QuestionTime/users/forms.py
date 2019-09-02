from django_registration.forms import RegistrationForm
from users.models import CustomUser
from crispy_forms.helper import FormHelper

# creates a custom user form by extending RegistrationForm and passing
# the custom User model to the Meta class


class CustomUserForm(RegistrationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
