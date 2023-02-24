from django.shortcuts import render

from django.views import generic, View


class ContactUs(View):
    """
    This view is used to display the contact page
    """

    def get(self, request):
        """
        Renders the contact page
        """

        return render(
            request,
            "contact/contact.html",
        )


