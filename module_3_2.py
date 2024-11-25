def send_email(message, recipient, sender = 'university.help@gmail.com'):
    if '@' not in (recipient or sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif ('.com' or '.ru' or '.net') not in (recipient and sender):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == 'university.help@gmail.com' and ('.com' or '.ru' or '.net') not in recipient:
        print(f'Письмо {message} успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо {message} отправлено с адреса {sender} на адрес {recipient}')

send_email('<Это сообщение для проверки связи>', 'julia12@.ru')
send_email('<Вы видите это сообщение как лучший студент курса!>', 'urban.fan@mail.net', sender= 'urban.info@gmail.com')
send_email('Пожалуйста, исправте задание', 'urban.student@mail.ru', sender= 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'juli@mail.ru', sender= 'juli@mail.ru')
