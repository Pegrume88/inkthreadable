from django.shortcuts import render

from django.views import generic


class ContactUS(generic.TemplateView):
    """This view is used to display the contact page"""
    template_name = "contact/contact.html"
   
    
class AboutUS(generic.TemplateView):
    """This view is used to display the about us page"""
    template_name = "contact/about.html"

