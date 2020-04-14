from django.conf import settings
from django.core import mail

from dadashop12.celery import app


@app.task
def send_active_email_async(email_address, v_url):
    subject = '达达商城激活邮件'
    html_message = '''
    <p>尊敬的用户您好</p>
    <p>请点击此链接激活您的账户(3天内有效):</p>
    <p><a href='%s' target='_blank'>点击激活</a></p>
    ''' % (v_url)
    mail.send_mail(subject, '', from_email=settings.EMAIL_HOST_USER, recipient_list=[email_address],
                   html_message=html_message)
