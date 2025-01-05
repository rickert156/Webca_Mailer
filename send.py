import csv, os, time

from module.send_message import SendMessage
from module.miniTools import recording_done_email, create_done_dir
from module.miniTools import path_done_file, path_base_file

#Файл конфигурации, в нем нужно добавить эти переменные base и LIMIT_MESSAGE
from config import base, LIMIT_MESSAGE


SET_DONE_EMAIL = set()

def check_email_list_done():
    global path_done_file, SET_DONE_EMAIL

    with open(path_done_file, 'r') as file:
        for row_email in csv.DictReader(file):
            email = row_email['Email']
            SET_DONE_EMAIL.add(email)
 

def main():
    global path_done_file, path_base_file, SET_DONE_EMAIL

    create_done_dir()
    
    #SendMessage(login=login, password=password, recipient='maksimnegulyaev@gmail.com')
    recording_done_email(login=login, recipient='maksimnegulyaev@gmail.com')
    
    with open(path_base_file, 'r') as file:
        number_email = 0
        for row in csv.DictReader(file):
            email = row['Email']
            
            check_email_list_done()
            if email not in SET_DONE_EMAIL:
                number_email+=1
                print(f'[{number_email}] {email}')
                
            if number_email == LIMIT_MESSAGE:
                break




main()
