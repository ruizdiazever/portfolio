from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')

            email = EmailMessage(
                'PORTFOLIO: nuevo mensaje.',
                '{} <{}> escribio: \n\n{}'.format(name, email, content),
                'no-contestar@inbox.mailtrao.io',
                ['ruizdiaz.oe@gmail.com'],
                reply_to=[email],
            )

            try:
                email.send()
                return redirect(reverse('contact',)+'?ok')
            except:
                return redirect(reverse('contact',)+'?fail')

    return render(request, "contact/contact.html", {'formulario':contact_form})