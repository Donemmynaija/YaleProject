from django.core.mail import send_mail
from django.conf import settings

def send_email(username, email,):
    subject = "Welcome to Donemmynaija!"
    body = f'''
            Hello {username}! Welcome to Donemmynaija. We're excited to have you on board.
            Feel free to explore and connect with others.
            Best regards,
            The Donemmynaija Team
    '''
    send_mail(
    subject,
    body,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)