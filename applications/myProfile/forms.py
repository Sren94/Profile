from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Juan Perez',
            'class': 'form-control'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'ejemplo@email.com',
            'class': 'form-control' 
        })
    )
    message = forms.CharField(
        label="Mensaje",
        widget=forms.Textarea(attrs={
            'placeholder': 'Escribe tu mensaje',
            'class': 'form-control',
            'rows': 4,
            'style': 'resize:none;'
        })
    )
