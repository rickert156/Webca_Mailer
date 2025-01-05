#!/usr/bin/bash

mkdir base
echo "Создана директория base, в нее нужно добавить базы. В базе должна быть колонка Email"

touch config.py
echo "base: str = ''" >> config.py
echo "LIMIT_MESSAGE: int = 50" >> config.py
echo "Добавлен файл конфигурации, нужно вписать актуальную базу для рассылки"

mkdir data
echo "login,password" > data/account.csv
echo "Добавь логины с паролями от почтовых акков"
