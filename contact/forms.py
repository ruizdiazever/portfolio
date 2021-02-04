from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Please write your name'
        }
    ), min_length=2, max_length=100)


    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'Please write your email'
        }
    ), min_length=2, max_length=100)

    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'Please write your message',
            'rows':5
        }
    ), min_length=2, max_length=100)