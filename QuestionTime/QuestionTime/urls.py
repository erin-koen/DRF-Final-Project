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
# re_path allows us to redirect based on regex -
# we want to redirect every request to index template view.
from django.urls import include, path, re_path
# one_step.views eliminates email verification. To learn more:
# django-registration.readthedocs.io/en/3.0/activation-workflow.html
from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [
    # admin login
    path('admin/', admin.site.urls),

    # registration via browser
    path("accounts/register/", RegistrationView.as_view(
        form_class=CustomUserForm, success_url="/",),
        name="django_registration_register"),

    # login via browser, redundancies
    path("accounts/", include("django_registration.backends.one_step.urls")),

    # login via browser, redundancies
    path("accounts/", include("django.contrib.auth.urls")),

    # access views within User Api
    path("api/", include("users.api.urls")),

    # login via browsable API
    path("api-auth/", include("rest_framework.urls")),

    # login via REST
    path("api/rest-auth/", include("rest_auth.urls")),

    # registration via REST
    path("api/rest-auth/registration/",
         include("rest_auth.registration.urls")),

    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")

]
