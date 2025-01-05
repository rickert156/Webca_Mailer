import csv, os, time

from module.send_message import SendMessage
from module.miniTools import recording_done_email, create_done_dir
from module.miniTools import path_done_file, path_base_file
from config import base


 
def main():
    global path_done_file, path_base_file

    create_done_dir()
    
    login = 'maksim@webcadev.ru'
    password = 'Eo~6HTLq9j3L'
    
    #SendMessage(login=login, password=password, recipient='maksimnegulyaev@gmail.com')
    #recording_done_email(login=login, recipient='maksimnegulyaev@gmail.com')
    
    with open(path_base_file, 'r') as file:
        number_email = 0
        for row in csv.DictReader(file):
            number_email+=1
            email = row['Email']
            print(f'[{number_email}] {email}')



main()
