from django.shortcuts import render

# Create your views here.

def privacy_policy(request):
    return render(request, 'support/privacy_policy.html')

def about(request):
    return render(request, 'support/about.html')

def contact(request):
    return render(request, 'support/contact.html')