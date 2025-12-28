from django.shortcuts import render

# Create your views here.

def privacy_policy(request):
    return render(request, 'support/privacy_policy.html')

def about(request):
    return render(request, 'support/about.html')

def contact(request):
    return render(request, 'support/contact.html')

def contact_confirmation(request):
    return render(request, 'support/contact_confirmation.html')

def terms_and_conditions(request):
    return render(request, 'support/terms_and_conditions.html')

def faqs(request):
    return render(request, 'support/faqs.html')