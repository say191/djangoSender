from sender.models import Newsletter
from log.models import Log
from zoneinfo import ZoneInfo
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


def transform_time_in_min(timing: str):
    """
            Функция для преобразования времени в минуты, для удобства сравнивания времени,
            где в аргументе передаем время в формате (ЧЧ:ММ)
        """
    return int(timing.split(':')[0])*60 + int(timing.split(':')[1])


def send_newsletter():
    wrong_time_now = datetime.now() #записываем текущее время в переменную
    correct_time_now = wrong_time_now.astimezone(ZoneInfo(key='Europe/Moscow')).strftime('%H:%M')
    #преобразовываем в кореектное время, т к по умолчанию часовой пояс выставлен неверно
    password = os.getenv('PASSWORD_HOST')
    #записываем в переменную пароль от почты отправителя из переменной виртуального окружения
    email_sender = os.getenv('EMAIL_HOST')
    #записываем в переменную почту отправителя из переменной виртуального окружения
    for newsletter in Newsletter.objects.all(): #проходимся по всем рассылкам
        email_getter = [] #создаем пустой список, куда будем записывать почты адрессатов из рассылок
        for j in newsletter.clients.all(): #проходимся по всем клиентам каждой рассылки
            email_getter.append(j.email) #добавляем почты клиентов в список
        if (transform_time_in_min(newsletter.time_stop) > transform_time_in_min(correct_time_now) >=
                transform_time_in_min(newsletter.time_send)):
            #создаем условия, из которых видно, что сервис отправки будет отправлять письма
            #при условии, если текущее время меньше, чем время остановки рассылки и больше или
            #равно времени старта рассылки
            try:
                #используем конструкцию try/except, чтобы отлавливать исключения, при попытки отправки писем
                message = MIMEMultipart() #создаем сообщение
                message['Subject'] = newsletter.theme_message #присваиваем тему сообщению
                message.attach(MIMEText(newsletter.text_message, 'plain'))
                #текст сообщения достаем из объекта рассылки
                connection = smtplib.SMTP('smtp.gmail.com')
                #инициализируем соединение
                connection.starttls()
                connection.login(user=email_sender, password=password)
                #проходим авторизацию почтового сервиса
                connection.sendmail(from_addr=email_sender, to_addrs=email_getter, msg=message.as_string())
                #отправляем сообщение
                connection.close() #закрываем соединение
                log = Log.objects.create(
                    try_date=wrong_time_now.astimezone(ZoneInfo(key='Europe/Moscow')).strftime('%Y-%m-%d %H:%M'),
                    try_status='Finished',
                    try_response='OK',
                    email=', '.join(email_getter)
                )
                #создаем объект класса log и заполняем необходимые поля
                log.save() #сохраняем объект
            except smtplib.SMTPException: #отлавливаем исключения
                log = Log.objects.create(
                    try_date=wrong_time_now.astimezone(ZoneInfo(key='Europe/Moscow')).strftime('%Y-%m-%d %H:%M'),
                    try_status='Canceled',
                    try_response='ERROR',
                    email=', '.join(email_getter)
                )
                log.save()
                #создаем объект класса log и заполняем необходимые поля
