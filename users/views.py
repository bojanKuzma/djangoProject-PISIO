from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import RegisterForm
from users.models import CustomUser


class RegisterView(CreateView):  # CreateView je jedan od defaultnih ClassBasedView-ova
    template_name = 'users/register.html'  # nas template koji koristi forma
    form_class = RegisterForm  # forma koju koristimo
    model = CustomUser  # Model na koji se odnosi create
    success_url = reverse_lazy('login')  # reverse lazy metoda nam omogucava da nakon uspjesnog registrovanog korisnika
    # nas redirektuje (success_url) na login tj name atribut od path-a.
