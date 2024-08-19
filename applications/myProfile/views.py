from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import ListView, TemplateView
from .models import Project

from .forms import ContactForm
from django.conf import settings

class ProjectNameList(ListView):
    model = Project
    template_name = "myProfile/myProfile.html"
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construir el mensaje completo incluyendo el correo de la persona que contacta
            full_message = f"Mensaje de {name} <{email}>:\n\n{message}"

            # Envía el correo electrónico
            send_mail(
                f'Mensaje de {name}',  # Asunto
                full_message,  # Cuerpo del mensaje
                settings.EMAIL_HOST_USER,  # De
                [settings.EMAIL_HOST_USER],  # A
                fail_silently=False,
            )
            return redirect('profile_app:contact_success')  # Redirige a una página de éxito
        return self.get(request, *args, **kwargs)



class ContactSuccessView(TemplateView):
    template_name = "myProfile/contact_success.html"
