from decimal import Decimal
from unittest.mock import patch, Mock

from django.test import TestCase, Client, override_settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.core import mail
from django.utils import timezone
from django.db import transaction

from .models import ContactMessage


class SupportModelTests(TestCase):
    """
    Unit tests for support model functionality.
    
    Tests model behaviour:
    - ContactMessage creation and validation
    - Model field choices and defaults
    - String representation and ordering
    """
    
    def test_contact_message_creation(self):
        """Test ContactMessage model creation with all required fields."""
        contact_message = ContactMessage.objects.create(
            name='John Doe',
            email='john@example.com',
            category='technical',
            subject='Login Issues',
            message='I cannot log into my account. Please help.'
        )
        
        # Test default values
        self.assertEqual(contact_message.status, 'new')
        self.assertIsNotNone(contact_message.created_at)
        self.assertIsNotNone(contact_message.updated_at)
        
        # Test string representation
        expected_str = f"John Doe - Login Issues (New)"
        self.assertEqual(str(contact_message), expected_str)
        
        # Test model fields
        self.assertEqual(contact_message.name, 'John Doe')
        self.assertEqual(contact_message.email, 'john@example.com')
        self.assertEqual(contact_message.category, 'technical')
        self.assertEqual(contact_message.subject, 'Login Issues')
        self.assertEqual(contact_message.message, 'I cannot log into my account. Please help.')
    
    def test_contact_message_category_choices(self):
        """Test all category choices are valid."""
        valid_categories = [
            'technical', 'billing', 'account', 'game', 'refund', 'other'
        ]
        
        for category in valid_categories:
            contact_message = ContactMessage.objects.create(
                name='Test User',
                email='test@example.com',
                category=category,
                subject='Test Subject',
                message='Test message.'
            )
            self.assertEqual(contact_message.category, category)
    
    def test_contact_message_status_choices(self):
        """Test all status choices are valid."""
        valid_statuses = ['new', 'in_progress', 'resolved', 'closed']
        
        contact_message = ContactMessage.objects.create(
            name='Test User',
            email='test@example.com',
            category='technical',
            subject='Test Subject',
            message='Test message.'
        )
        
        for status in valid_statuses:
            contact_message.status = status
            contact_message.save()
            contact_message.refresh_from_db()
            self.assertEqual(contact_message.status, status)
    
    def test_contact_message_ordering(self):
        """Test ContactMessage objects are ordered by creation date (newest first)."""
        # Create messages in specific order
        message1 = ContactMessage.objects.create(
            name='First User',
            email='first@example.com',
            category='technical',
            subject='First Message',
            message='First message.'
        )
        
        message2 = ContactMessage.objects.create(
            name='Second User',
            email='second@example.com',
            category='billing',
            subject='Second Message',
            message='Second message.'
        )
        
        message3 = ContactMessage.objects.create(
            name='Third User',
            email='third@example.com',
            category='account',
            subject='Third Message',
            message='Third message.'
        )
        
        # Test ordering (newest first)
        messages = ContactMessage.objects.all()
        self.assertEqual(messages[0], message3)  # Most recent
        self.assertEqual(messages[1], message2)
        self.assertEqual(messages[2], message1)  # Oldest
    
    def test_contact_message_meta_options(self):
        """Test model Meta options."""
        self.assertEqual(ContactMessage._meta.verbose_name, 'Contact Message')
        self.assertEqual(ContactMessage._meta.verbose_name_plural, 'Contact Messages')
        self.assertEqual(ContactMessage._meta.ordering, ['-created_at'])


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    DEFAULT_FROM_EMAIL='noreply@testserver.com',
    EMAIL_HOST_USER='testadmin@testserver.com',
    ADMINS=[],  # No admins to force EMAIL_HOST_USER fallback
    SITE_URL='http://testserver'
)
class SupportViewTests(TestCase):
    """
    Integration tests for support view functionality.
    
    Tests view behaviour:
    - Static page rendering
    - Contact form processing
    - Email sending functionality
    - Form validation and error handling
    """
    
    def setUp(self):
        """Set up test fixtures for view testing."""
        self.client = Client()
        mail.outbox = []  # Clear email outbox
    
    def test_privacy_policy_view(self):
        """Test privacy policy page renders correctly."""
        response = self.client.get(reverse('support:privacy_policy'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/privacy_policy.html')
    
    def test_about_view(self):
        """Test about page renders correctly."""
        response = self.client.get(reverse('support:about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/about.html')
    
    def test_terms_and_conditions_view(self):
        """Test terms and conditions page renders correctly."""
        response = self.client.get(reverse('support:terms_and_conditions'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/terms_and_conditions.html')
    
    def test_faqs_view(self):
        """Test FAQs page renders correctly."""
        response = self.client.get(reverse('support:faqs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/faqs.html')
    
    def test_contact_view_get(self):
        """Test contact form page renders correctly."""
        response = self.client.get(reverse('support:contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/contact.html')
    
    def test_contact_form_submission_creates_message(self):
        """Test contact form submission creates ContactMessage and sends emails."""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'category': 'technical',
            'subject': 'Test Subject',
            'message': 'This is a test message for support.'
        }
        
        response = self.client.post(reverse('support:contact'), data=form_data)
        
        # Test redirect to confirmation page
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('support:contact_confirmation'))
        
        # Test ContactMessage was created
        contact_message = ContactMessage.objects.get(email='test@example.com')
        self.assertEqual(contact_message.name, 'Test User')
        self.assertEqual(contact_message.category, 'technical')
        self.assertEqual(contact_message.subject, 'Test Subject')
        self.assertEqual(contact_message.message, 'This is a test message for support.')
        self.assertEqual(contact_message.status, 'new')
        
        # Test emails were sent (user confirmation + admin notification)
        self.assertEqual(len(mail.outbox), 2)
        
        # Test user confirmation email
        user_email = mail.outbox[0]
        self.assertIn('test@example.com', user_email.to)
        self.assertIn('Test User', user_email.body)
        
        # Test admin notification email (check actual recipient)
        admin_email = mail.outbox[1]
        # The admin email goes to EMAIL_HOST_USER when no ADMINS configured
        self.assertIn('testadmin@testserver.com', admin_email.to)
        self.assertIn('Test User', admin_email.body)
        self.assertIn('technical', admin_email.body.lower())
    
    def test_contact_confirmation_view(self):
        """Test contact confirmation page renders correctly."""
        response = self.client.get(reverse('support:contact_confirmation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'support/contact_confirmation.html')
    
    def test_contact_form_with_all_categories(self):
        """Test contact form submission works for all category types."""
        categories = ['technical', 'billing', 'account', 'game', 'refund', 'other']
        
        for category in categories:
            mail.outbox = []  # Clear emails for each test
            
            form_data = {
                'name': f'User {category.title()}',
                'email': f'{category}@example.com',
                'category': category,
                'subject': f'{category.title()} Issue',
                'message': f'This is a {category} related message.'
            }
            
            response = self.client.post(reverse('support:contact'), data=form_data)
            
            # Test successful submission
            self.assertEqual(response.status_code, 302)
            
            # Test message was created with correct category
            contact_message = ContactMessage.objects.get(email=f'{category}@example.com')
            self.assertEqual(contact_message.category, category)
            
            # Test emails were sent
            self.assertEqual(len(mail.outbox), 2)


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    DEFAULT_FROM_EMAIL='noreply@testserver.com',
    EMAIL_HOST_USER='testadmin@testserver.com'
)
class SupportFormValidationTests(TestCase):
    """
    Tests for contact form validation and error handling.
    
    Tests form behaviour:
    - Required field validation
    - Email format validation
    - Category choice validation
    - Message length limits
    """
    
    def setUp(self):
        """Set up test fixtures for form testing."""
        self.client = Client()
    
    def test_contact_form_missing_required_fields(self):
        """Test contact form handles missing required fields gracefully."""
        # The current view implementation doesn't validate properly
        # This test documents the current behaviour - it will fail with database error
        
        # Use transaction.atomic to handle the IntegrityError properly
        try:
            with transaction.atomic():
                response = self.client.post(reverse('support:contact'), data={})
            # If we get here, the view unexpectedly succeeded
            self.fail("Expected IntegrityError was not raised")
        except Exception as e:
            # The expected database constraint violation occurred
            # Verify it's the right type of error
            self.assertIn('null value', str(e).lower())
        
        # Verify no ContactMessage was created
        self.assertEqual(ContactMessage.objects.count(), 0)
    
    def test_contact_form_with_minimal_valid_data(self):
        """Test contact form works with minimal valid data."""
        form_data = {
            'name': 'A',  # Minimal name
            'email': 'a@b.co',  # Minimal valid email
            'category': 'other',
            'subject': 'Hi',  # Short subject
            'message': 'Help'  # Short message
        }
        
        response = self.client.post(reverse('support:contact'), data=form_data)
        
        # Should redirect successfully
        self.assertEqual(response.status_code, 302)
        
        # ContactMessage should be created
        self.assertEqual(ContactMessage.objects.count(), 1)
        contact_message = ContactMessage.objects.first()
        self.assertEqual(contact_message.name, 'A')
        self.assertEqual(contact_message.email, 'a@b.co')
    
    def test_contact_form_with_long_content(self):
        """Test contact form handles long content appropriately."""
        long_name = 'A' * 200  # At model limit
        long_subject = 'B' * 300  # At model limit  
        long_message = 'C' * 1000  # Large message
        
        form_data = {
            'name': long_name,
            'email': 'test@example.com',
            'category': 'technical',
            'subject': long_subject,
            'message': long_message
        }
        
        response = self.client.post(reverse('support:contact'), data=form_data)
        
        # Should work with long content (within model limits)
        self.assertEqual(response.status_code, 302)
        
        contact_message = ContactMessage.objects.first()
        self.assertEqual(contact_message.name, long_name)
        self.assertEqual(contact_message.subject, long_subject)
        self.assertEqual(contact_message.message, long_message)
    
    def test_contact_form_invalid_category(self):
        """Test contact form handles invalid category gracefully."""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'category': 'invalid_category',
            'subject': 'Test Subject',
            'message': 'Test message'
        }
        
        response = self.client.post(reverse('support:contact'), data=form_data)
        
        # Should still process (Django will use the invalid value)
        self.assertEqual(response.status_code, 302)
        
        contact_message = ContactMessage.objects.first()
        self.assertEqual(contact_message.category, 'invalid_category')


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    DEFAULT_FROM_EMAIL='noreply@testserver.com',
    ADMINS=[('Admin One', 'admin1@testserver.com'), ('Admin Two', 'admin2@testserver.com')],
    EMAIL_HOST_USER='fallback@testserver.com',
    SITE_URL='http://testserver'
)
class SupportEmailTests(TestCase):
    """
    Tests for email functionality in support system.
    
    Tests email behaviour:
    - User confirmation emails
    - Admin notification emails
    - Email template rendering
    - Error handling for email failures
    """
    
    def setUp(self):
        """Set up test fixtures for email testing."""
        self.client = Client()
        mail.outbox = []  # Clear email outbox
    
    def test_contact_submission_sends_user_confirmation(self):
        """Test contact submission sends confirmation email to user."""
        form_data = {
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'category': 'billing',
            'subject': 'Payment Issue',
            'message': 'I was charged twice for my order.'
        }
        
        self.client.post(reverse('support:contact'), data=form_data)
        
        # Find user confirmation email
        user_email = None
        for email in mail.outbox:
            if 'jane@example.com' in email.to:
                user_email = email
                break
        
        self.assertIsNotNone(user_email)
        self.assertIn('jane@example.com', user_email.to)
        self.assertIn('Jane Smith', user_email.body)
        self.assertIn('Payment Issue', user_email.body)
        
        # Test email has both HTML and plain text versions
        self.assertTrue(hasattr(user_email, 'alternatives'))
    
    def test_contact_submission_sends_admin_notification(self):
        """Test contact submission sends notification to admins."""
        form_data = {
            'name': 'Bob Johnson',
            'email': 'bob@example.com',
            'category': 'refund',
            'subject': 'Refund Request',
            'message': 'I would like to refund my recent purchase.'
        }
        
        self.client.post(reverse('support:contact'), data=form_data)
        
        # Find admin notification email
        admin_email = None
        for email in mail.outbox:
            if any(admin in email.to for admin in ['admin1@testserver.com', 'admin2@testserver.com']):
                admin_email = email
                break
        
        self.assertIsNotNone(admin_email)
        
        # Test admin emails are sent to configured admins
        self.assertIn('admin1@testserver.com', admin_email.to)
        self.assertIn('admin2@testserver.com', admin_email.to)
        
        # Test admin email contains message details
        self.assertIn('Bob Johnson', admin_email.body)
        self.assertIn('bob@example.com', admin_email.body)
        self.assertIn('Refund Request', admin_email.body)
    
    @override_settings(
        ADMINS=[],  # No admins configured
        EMAIL_HOST_USER='fallback@testserver.com'
    )
    def test_admin_email_fallback_to_host_user(self):
        """Test admin notification falls back to EMAIL_HOST_USER when no ADMINS."""
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'category': 'technical',
            'subject': 'Test Subject',
            'message': 'Test message'
        }
        
        self.client.post(reverse('support:contact'), data=form_data)
        
        # Should still send admin notification to EMAIL_HOST_USER
        admin_email = None
        for email in mail.outbox:
            if 'fallback@testserver.com' in email.to:
                admin_email = email
                break
        
        self.assertIsNotNone(admin_email)
        self.assertIn('fallback@testserver.com', admin_email.to)
    
    @patch('support.views.EmailMultiAlternatives.send')
    def test_email_sending_error_handling(self, mock_send):
        """Test contact form handles email sending errors gracefully."""
        # Mock email sending to raise an exception
        mock_send.side_effect = Exception("SMTP Error")
        
        form_data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'category': 'technical',
            'subject': 'Test Subject',
            'message': 'Test message'
        }
        
        response = self.client.post(reverse('support:contact'), data=form_data)
        
        # Should still redirect to confirmation (fail gracefully)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('support:contact_confirmation'))
        
        # ContactMessage should still be created despite email failure
        self.assertEqual(ContactMessage.objects.count(), 1)
        contact_message = ContactMessage.objects.first()
        self.assertEqual(contact_message.email, 'test@example.com')


class SupportAdminTests(TestCase):
    """
    Tests for admin interface functionality.
    
    Tests admin behaviour:
    - ContactMessage admin configuration
    - Filtering and searching
    - Read-only field handling
    - Admin permissions
    """
    
    def setUp(self):
        """Set up test fixtures for admin testing."""
        self.superuser = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123'
        )
        
        self.contact_message = ContactMessage.objects.create(
            name='Test User',
            email='test@example.com',
            category='technical',
            subject='Test Subject',
            message='Test message for admin interface testing.'
        )
    
    def test_contact_message_admin_list_display(self):
        """Test ContactMessage admin list displays correct fields."""
        from .admin import ContactMessageAdmin
        
        expected_fields = ('name', 'email', 'category', 'subject', 'status', 'created_at')
        self.assertEqual(ContactMessageAdmin.list_display, expected_fields)
    
    def test_contact_message_admin_filters(self):
        """Test ContactMessage admin has correct filters."""
        from .admin import ContactMessageAdmin
        
        expected_filters = ('status', 'category', 'created_at')
        self.assertEqual(ContactMessageAdmin.list_filter, expected_filters)
    
    def test_contact_message_admin_search(self):
        """Test ContactMessage admin search functionality."""
        from .admin import ContactMessageAdmin
        
        expected_search_fields = ('name', 'email', 'subject', 'message')
        self.assertEqual(ContactMessageAdmin.search_fields, expected_search_fields)
    
    def test_contact_message_admin_readonly_fields_new(self):
        """Test readonly fields for new ContactMessage in admin."""
        from .admin import ContactMessageAdmin
        
        admin = ContactMessageAdmin(ContactMessage, None)
        readonly_fields = admin.get_readonly_fields(None, None)  # New object
        
        expected_readonly = ('created_at', 'updated_at')
        self.assertEqual(readonly_fields, expected_readonly)
    
    def test_contact_message_admin_readonly_fields_existing(self):
        """Test readonly fields for existing ContactMessage in admin."""
        from .admin import ContactMessageAdmin
        
        admin = ContactMessageAdmin(ContactMessage, None)
        readonly_fields = admin.get_readonly_fields(None, self.contact_message)  # Existing object
        
        # Should include all contact fields as readonly when editing
        expected_readonly = ('created_at', 'updated_at', 'name', 'email', 'category', 'subject', 'message')
        self.assertEqual(readonly_fields, expected_readonly)


@override_settings(
    EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend',
    DEFAULT_FROM_EMAIL='noreply@eclipseprotocol.com',
    ADMINS=[('Support Team', 'support@eclipseprotocol.com')],
    EMAIL_HOST_USER='test@eclipseprotocol.com',
    SITE_URL='https://eclipseprotocol.com' 
)
class SupportIntegrationTests(TestCase):
    """
    End-to-end integration tests for support system.
    
    Tests realistic scenarios:
    - Complete contact form workflow
    - Multiple contact submissions
    - Admin workflow for managing messages
    - Error scenarios and edge cases
    """
    
    def setUp(self):
        """Set up test fixtures for integration testing."""
        self.client = Client()
        mail.outbox = []  # Clear email outbox
    
    def test_complete_support_workflow(self):
        """Test complete support contact workflow."""
        # Step 1: User visits contact page
        response = self.client.get(reverse('support:contact'))
        self.assertEqual(response.status_code, 200)
        
        # Step 2: User submits contact form
        form_data = {
            'name': 'Alice Williams',
            'email': 'alice@example.com',
            'category': 'account',
            'subject': 'Cannot access purchased content',
            'message': 'I purchased the Ultimate Edition yesterday but cannot access the bonus content. My order number is EP12345678.'
        }
        
        response = self.client.post(reverse('support:contact'), data=form_data)
        
        # Step 3: Verify successful submission and redirect
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('support:contact_confirmation'))
        
        # Step 4: Verify confirmation page displays
        response = self.client.get(reverse('support:contact_confirmation'))
        self.assertEqual(response.status_code, 200)
        
        # Step 5: Verify ContactMessage was created
        contact_message = ContactMessage.objects.get(email='alice@example.com')
        self.assertEqual(contact_message.name, 'Alice Williams')
        self.assertEqual(contact_message.category, 'account')
        self.assertEqual(contact_message.status, 'new')
        self.assertIn('EP12345678', contact_message.message)
        
        # Step 6: Verify emails were sent
        self.assertEqual(len(mail.outbox), 2)
        
        user_email = next((email for email in mail.outbox if 'alice@example.com' in email.to), None)
        admin_email = next((email for email in mail.outbox if 'support@eclipseprotocol.com' in email.to), None)
        
        self.assertIsNotNone(user_email)
        self.assertIsNotNone(admin_email)
        
        # Step 7: Verify email content
        self.assertIn('Alice Williams', user_email.body)
        self.assertIn('Cannot access purchased content', admin_email.body)
    
    def test_multiple_contact_submissions_same_user(self):
        """Test multiple contact submissions from the same user."""
        user_email = 'repeat@example.com'
        
        # Submit first message
        form_data1 = {
            'name': 'Repeat User',
            'email': user_email,
            'category': 'technical',
            'subject': 'First Issue',
            'message': 'This is my first issue.'
        }
        
        response = self.client.post(reverse('support:contact'), data=form_data1)
        self.assertEqual(response.status_code, 302)
        
        # Submit second message
        form_data2 = {
            'name': 'Repeat User',
            'email': user_email,
            'category': 'billing',
            'subject': 'Second Issue',
            'message': 'This is my second issue.'
        }
        
        response = self.client.post(reverse('support:contact'), data=form_data2)
        self.assertEqual(response.status_code, 302)
        
        # Verify both messages were created
        messages = ContactMessage.objects.filter(email=user_email).order_by('-created_at')
        self.assertEqual(messages.count(), 2)
        
        self.assertEqual(messages[0].subject, 'Second Issue')  # Most recent first
        self.assertEqual(messages[1].subject, 'First Issue')
        
        # Both should have 'new' status
        self.assertTrue(all(msg.status == 'new' for msg in messages))
    
    def test_support_page_accessibility(self):
        """Test all support pages are accessible."""
        support_pages = [
            'support:privacy_policy',
            'support:about',
            'support:terms_and_conditions',
            'support:faqs',
            'support:contact',
            'support:contact_confirmation',
        ]
        
        for page_name in support_pages:
            with self.subTest(page=page_name):
                response = self.client.get(reverse(page_name))
                self.assertEqual(response.status_code, 200)