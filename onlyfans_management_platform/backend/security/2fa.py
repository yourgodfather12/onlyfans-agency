
from django.contrib.auth.models import User
from django.core.mail import send_mail
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename='logs/backend/security.log',
                    format='%(asctime)s %(levelname)s:%(message)s')

def send_verification_code(user_email):
    code = random.randint(100000, 999999)
    send_mail(
        'Your Verification Code',
        f'Your verification code is {code}',
        'admin@yourdomain.com',
        [user_email],
        fail_silently=False,
    )
    logging.info(f"Verification code sent to {user_email}")
    return code
