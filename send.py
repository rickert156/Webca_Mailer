import csv, os, time

from module.send_message import SendMessage
from config import base

#Каталог и файл с базой, куда письма уже отправили
dir_done = 'done'
file_done = 'done.csv'
path_done_file = f'{dir_done}/{file_done}'

#Каталог База для рассылки
dir_base = 'base'
dir_base = base

def recording_done_email(login: str = None, recipient: str = None):
    global path_done_file

    send_time = time.strftime('%H:%M:%S')
    send_date = time.strftime('%d/%m/%y')
    
    with open(path_done_file, 'a+') as file:
        write = csv.writer(file)
        write.writerow([login, recipient, send_time, send_date])

def create_done_dir():
    global file_done, dir_done, path_done_file

    if not os.path.exists(dir_done):
        os.makedirs(dir_done)
        print(f'Create dir {dir_done}')

    if not os.path.exists(path_done_file):
        with open(path_done_file, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Webca Email', 'Email', 'Time', 'Date'])
            print(f'Create file {file_done}')


 
def main():
    global path_done_file

    create_done_dir()
    
    login = 'maksim@webcadev.ru'
    password = 'Eo~6HTLq9j3L'
    
    #SendMessage(login=login, password=password, recipient='maksimnegulyaev@gmail.com')
    recording_done_email(login=login, recipient='maksimnegulyaev@gmail.com')

main()
