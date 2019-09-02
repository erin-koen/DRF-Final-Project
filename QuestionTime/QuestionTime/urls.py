"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# one_step skips email verification. read docs below for details.
# https://django-registration.readthedocs.io/en/3.0/activation-workflow.html
from django_registration.backends.one_step.views import RegistrationView

from users.forms import CustomUserForm


urlpatterns = [
    path('admin/', admin.site.urls),

    # login via browser
    path("accounts/", include("django.contrib.auth.urls")),
    # this one is also login via browser but i'm not quite sure why
    path("accounts/", include("django_registration.backends.one_step.urls")),


    # register via browser - because we're using a custom user model, we nned
    # to build custom forms for the registration endpoint in forms.py
    path("accounts/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url='/'
         ), name="django_registration_register"),


    # login via browsable API
    path("api-auth", include("rest_framework.urls")),

    # login via rest
    path("api/rest-auth", include("rest_auth.urls")),

    # register acct via rest
    path("api/rest-auth/registration", include("rest_auth.registration.urls")),
]
