import traceback

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import ContactMessage

# Create your views here.


def privacy_policy(request):
    return render(request, "support/privacy_policy.html")


def about(request):
    return render(request, "support/about.html")


def contact(request):
    if request.method == "POST":
        # Extract form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        category = request.POST.get("category")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to database
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            category=category,
            subject=subject,
            message=message,
        )

        # Get category display name
        category_display = dict(ContactMessage.CATEGORY_CHOICES).get(
            category, category
        )

        # Prepare email context
        context = {
            "name": name,
            "email": email,
            "category": category,
            "category_display": category_display,
            "subject": subject,
            "message": message,
            "reference_id": contact_message.id,
            "timestamp": contact_message.created_at.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "site_url": request.build_absolute_uri("/").rstrip("/"),
            "admin_url": (
                f"{settings.SITE_URL.rstrip('/')}/admin/support/"
                f"contactmessage/{contact_message.id}/change/"
            ),
        }

        print("=" * 50)
        print("ATTEMPTING TO SEND EMAILS")
        print(f"User email: {email}")
        print(f"DEFAULT_FROM_EMAIL: {settings.DEFAULT_FROM_EMAIL}")
        print(f"EMAIL_HOST_USER: {settings.EMAIL_HOST_USER}")
        print(f"EMAIL_HOST: {settings.EMAIL_HOST}")

        try:
            # Send HTML email to user
            user_subject = render_to_string(
                "support/confirmation_emails/contact_confirmation_subject.txt",
                context,
            ).strip()

            user_html_message = render_to_string(
                "support/confirmation_emails/contact_confirmation_email.html",
                context,
            )
            user_plain_message = strip_tags(user_html_message)

            print(f"\nSending user confirmation to: {email}")
            print(f"Subject: {user_subject}")

            user_email = EmailMultiAlternatives(
                subject=user_subject,
                body=user_plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[email],
            )
            user_email.attach_alternative(user_html_message, "text/html")
            user_email.send(fail_silently=False)

            print("✓ User email sent successfully")

            # Send HTML email to admins
            admin_subject = render_to_string(
                "support/confirmation_emails/admin_notification_subject.txt",
                context,
            ).strip()

            admin_html_message = render_to_string(
                "support/confirmation_emails/admin_notification_email.html",
                context,
            )
            admin_plain_message = strip_tags(admin_html_message)

            # Send to admins
            admin_emails = []
            if hasattr(settings, "ADMINS") and settings.ADMINS:
                admin_emails = [admin[1] for admin in settings.ADMINS]

            # Fallback: send to EMAIL_HOST_USER if no ADMINS configured
            if not admin_emails and settings.EMAIL_HOST_USER:
                admin_emails = [settings.EMAIL_HOST_USER]

            if admin_emails:
                print(f"\nSending admin notification to: {admin_emails}")
                print(f"Subject: {admin_subject}")

                admin_email = EmailMultiAlternatives(
                    subject=admin_subject,
                    body=admin_plain_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=admin_emails,
                )
                admin_email.attach_alternative(admin_html_message, "text/html")
                admin_email.send(fail_silently=False)

                print("Admin email sent successfully")
            else:
                print("No admin emails configured")

            print("=" * 50)

        except Exception as e:
            print(f"\n ERROR sending email: {e}")
            print(traceback.format_exc())
            print("=" * 50)

        # Redirect to confirmation page
        return redirect("support:contact_confirmation")

    return render(request, "support/contact.html")


def contact_confirmation(request):
    return render(request, "support/contact_confirmation.html")


def terms_and_conditions(request):
    return render(request, "support/terms_and_conditions.html")


def faqs(request):
    return render(request, "support/faqs.html")
