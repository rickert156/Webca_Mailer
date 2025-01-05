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
    
    #Директория и файл для хранения аккаунтов рассылки
    account_dir, account_file = 'data', 'account.csv'

    path_account_file = f'{account_dir}/{account_file}'

    
    
    
    with open(path_account_file, 'r') as file_account:
        number_account = 0
        for row in csv.DictReader(file_account):
            number_account+=1
            login = row['login']
            password = row['password']

            with open(path_base_file, 'r') as file:
                number_email = 0
                for row in csv.DictReader(file):
                    email = row['Email']
            
                    check_email_list_done()
                    if email not in SET_DONE_EMAIL:
                        number_email+=1
                        
                        #Отправляем письмо
                        SendMessage(login=login, password=password, recipient=email)
                        
                        #Записываем 
                        recording_done_email(login=login, recipient=email)
                        
                        print(f'[{number_account}] {login} | {password} \t[{number_email}] {email}')
                        time.sleep(10)


                    if number_email == LIMIT_MESSAGE:
                        break




main()
