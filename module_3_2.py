#Домашняя работа по уроку "Способы вызова функции"
def verification (email):#Функция проверки E-mail на корректность
    global recipient, sender
    if email.find('@')!=-1 and not (email[-4::] == '.com' or email[-4::] == '.net' or email[-3::] =='.ru'):
        return True
def send_email(message, recipient, sender = "university.help@gmail.com"):
    if verification(recipient):
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ',  recipient)
    elif verification(sender):
        print('Невозможно отправить письмо с адреса ', sender, ' на адрес ', recipient)
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса ', sender,' на адрес ', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса ', sender, ' на адрес ', recipient)

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
