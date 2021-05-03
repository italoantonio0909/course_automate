from .decorators import process_async
from django.core.mail import EmailMultiAlternatives
from django.conf import settings


@process_async
def communication_send_mail(*, title: str, content: str, to=[]):
    """This function allow send email
    Parameters:
    title -- Title email
    content -- Content and body email
    to -- List users to send email
    """
    if not isinstance(to, list):
        to = list(to)

    message = EmailMultiAlternatives(
        title, content, settings.EMAIL_HOST_USER, to)
    message.attach_alternative(content, 'text/plain')
    message.send()
