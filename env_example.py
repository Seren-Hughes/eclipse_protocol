# env_example.py
# ===========================================
# ECLIPSE PROTOCOL ENVIRONMENT VARIABLES EXAMPLE
# ===========================================
# Copy this file to env.py and fill in your actual values
# Never commit the env.py file to version control
# Add env.py to your .gitignore file

import os

# Django Configuration
os.environ.setdefault("SECRET_KEY", "your-50-character-secret-key-here")
os.environ.setdefault("DEBUG", "True")  # Set to False for production

# PostgreSQL Database Configuration
os.environ.setdefault("DATABASE_URL", "postgresql://username:password@host:port/database_name")

# AWS S3 Storage Configuration
os.environ.setdefault("AWS_ACCESS_KEY_ID", "your-aws-access-key-id")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "your-aws-secret-access-key")
os.environ.setdefault("AWS_STORAGE_BUCKET_NAME", "your-s3-bucket-name")

# Email Configuration (Gmail SMTP)
os.environ.setdefault("EMAIL_HOST_USER", "your-store@gmail.com")
os.environ.setdefault("EMAIL_HOST_PASSWORD", "your-16-character-gmail-app-password")

# Stripe Payment Processing - TEST mode keys only for dev 
# (keys should start with pk and sk. replace with live keys for real live production)
os.environ.setdefault("STRIPE_PUBLIC_KEY", "pk_test_your_stripe_public_key")
os.environ.setdefault("STRIPE_SECRET_KEY", "sk_test_your_stripe_secret_key")
os.environ.setdefault("STRIPE_WH_SECRET", "whsec_your_webhook_signing_secret")

# Production Deployment Settings
os.environ.setdefault("ALLOWED_HOSTS", "localhost,127.0.0.1,your-app.herokuapp.com")