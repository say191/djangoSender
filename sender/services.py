from sender.models import Newsletter
from log.models import Log
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.utils import timezone
from django.conf import settings


def send_newsletter():
    password = settings.PASSWORD_HOST
    email_sender = settings.EMAIL_HOST
    for newsletter in Newsletter.objects.all():
        if newsletter.is_active:
            email_getter = []
            for j in newsletter.clients.all():
                email_getter.append(j.email)
            if newsletter.stop_date > timezone.now() >= newsletter.next_date:
                owner = newsletter.owner
                try:
                    message = MIMEMultipart()
                    message['Subject'] = newsletter.theme_message
                    message.attach(MIMEText(newsletter.text_message, 'plain'))
                    connection = smtplib.SMTP('smtp.gmail.com')
                    connection.starttls()
                    connection.login(user=email_sender, password=password)
                    connection.sendmail(from_addr=email_sender, to_addrs=email_getter, msg=message.as_string())
                    connection.close()
                    log = Log.objects.create(
                        try_date=timezone.now(),
                        try_status='Success',
                        try_response='OK',
                        email=', '.join(email_getter),
                        owner=owner
                    )
                    log.save()
                except smtplib.SMTPException:
                    log = Log.objects.create(
                        try_date=timezone.now(),
                        try_status='Fail',
                        try_response='ERROR',
                        email=', '.join(email_getter),
                        owner=owner
                    )
                    log.save()
                if newsletter.periodicity == 'Once a day':
                    newsletter.next_date += timezone.timedelta(days=1)
                elif newsletter.periodicity == 'Once a week':
                    newsletter.next_date += timezone.timedelta(days=7)
                elif newsletter.periodicity == 'Once a month':
                    newsletter.next_date += timezone.timedelta(days=30)
                newsletter.status = 'Launched'
                newsletter.save()
            elif timezone.now() > newsletter.stop_date:
                newsletter.status = 'Finished'
                newsletter.save()
