def read_template_message():
    dir_module = 'module'
    template_txt = 'template_message.txt'
    with open(f'{dir_module}/{template_txt}', 'r') as file:
        message = file.read()
    return message

def Message() -> str:
    body_message_in_file = read_template_message()
    
    message_template = body_message_in_file
    
    theme_template = 'Давайте создадим ваш идеальный сайт вместе с Webca'

    return message_template, theme_template

