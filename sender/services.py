from sender.models import Newsletter
from log.models import Log
from zoneinfo import ZoneInfo
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def transform_time_in_min(timing: str):
    return int(timing.split(':')[0])*60 + int(timing.split(':')[1])


def send_newsletter():
    wrong_time_now = datetime.now()
    correct_time_now = wrong_time_now.astimezone(ZoneInfo(key='Europe/Moscow')).strftime('%H:%M')
    password = os.getenv('PASSWORD_HOST')
    email_sender = os.getenv('EMAIL_HOST')
    for newsletter in Newsletter.objects.all():
        email_getter = []
        for j in newsletter.clients.all():
            email_getter.append(j.email)
        if (transform_time_in_min(newsletter.time_stop) > transform_time_in_min(correct_time_now) >=
                transform_time_in_min(newsletter.time_send)):
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
                    try_date=wrong_time_now.astimezone(ZoneInfo(key='Europe/Moscow')).strftime('%Y-%m-%d %H:%M'),
                    try_status='Finished',
                    try_response='OK',
                    email=', '.join(email_getter)
                )
                log.save()
            except smtplib.SMTPException:
                log = Log.objects.create(
                    try_date=wrong_time_now.astimezone(ZoneInfo(key='Europe/Moscow')).strftime('%Y-%m-%d %H:%M'),
                    try_status='Canceled',
                    try_response='ERROR',
                    email=', '.join(email_getter)
                )
                log.save()
