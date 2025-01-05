import smtplib, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from module.template_message import Message


def SendMessage(login: str = None, password: str = None, recipient: str = None):

    #Авторизационные данные
   
    #Получение письма и его темы
    message, theme = Message()    

    try:
        #Инициализация сервера smtp
        server = smtplib.SMTP_SSL(host='mail.webcadev.ru', port=465)
        server.login(login, password)

        msg = MIMEMultipart()
        #Кому, от кого, тема письма
        msg['From'] = login
        msg['To'] = recipient
        msg['Subject'] = theme
        
        #Добавление тела письма
        msg.attach(MIMEText(message, 'plain'))
        
        #Отправка письма 
        server.sendmail(login, recipient, msg.as_string())

    except Exception as err:print(f'[x] Отправка не удалась: {err}')
    else:print(f'[+] {login} -> {recipient}')
    finally:server.quit()



