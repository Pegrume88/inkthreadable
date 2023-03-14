from django.shortcuts import render

from django.shortcuts import render
from .models import Contact

def contact(request):
    if request.method == 'POST':
        # Save the contact form data to the database
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
        return render(request, 'contact_thankyou.html')
    else:
        return render(request, 'contact_form.html')


