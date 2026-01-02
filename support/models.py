from django.db import models
from django.utils import timezone

# Create your models here.


class ContactMessage(models.Model):
    CATEGORY_CHOICES = [
        ("technical", "Technical Support"),
        ("billing", "Billing & Payments"),
        ("account", "Account Issues"),
        ("game", "Game Content"),
        ("refund", "Refund Request"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In Progress"),
        ("resolved", "Resolved"),
        ("closed", "Closed"),
    ]

    name = models.CharField(max_length=200)
    email = models.EmailField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="new"
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"{self.name} - {self.subject} ({self.get_status_display()})"
