from datetime import datetime
from bottle import post, request, redirect
import re
import pdb
import json

@post('/home', method='post')
def my_form():
    question = {}
    # pdb.set_trace()
    mail = request.forms.get('ADRESS')
    name = request.forms.get('USERNAME')
    quest = request.forms.get('QUEST')  
    question[mail] = [name, quest] # словарь с данными текущего пользователя
    # pdb.exit()

    reg = r'^(?=.{8,256}$)[a-zA-Z][a-zA-Z0-9]{1,63}@[a-z]{2,63}\.[a-z]{2,63}(?:\.[a-z]{2,63})?$' # Регулярное выражение для проверки почты

    error = "" # Переменная для записи сообщений об ошибке

    # Проверка заполненности полей
    if len(quest) < 1 or len(mail) < 1 or len(name) < 1:
        error += "All fields must be filled in. "

    # Проверка вопроса
    filtered_quest = ''.join(c for c in quest if c.isalnum())  # Только буквы и цифры

    if len(filtered_quest) < 4 or quest.strip() == "" or quest.isdigit():
        error += "The question is incorrect. "

    # Проверка почты
    if (len(mail) < 8 or len(mail) > 255 or not re.match(reg, mail)) and len(mail) > 0: 
        error += "Mail entered incorrectly. "

    # Проверка имени
    if not re.match(r'^[a-zA-Z]+$', name) and len(name) > 0:
        error += "Name entered incorrectly. "

    # При наличии ошибок, вывод информации о них и завершение программы
    if len(error) > 0:
        return error
    else:
        try:
            is_exist_u = 0 # Существует ли пользователь в словаре
            is_exist_q = 0 # Существуетли вопрос в словаре
            # Открываем файл для чтения
            with open('static/json/questions.json', 'r') as file:
                questions_from_file = json.load(file)
                for mail_from_file in questions_from_file.keys(): # Проходимся по всем ключам из словаря (почтам)
                    if mail == mail_from_file: # Ищем совпадения почты текущего пользователя и почты из файла
                        is_exist_u = 1
                        if questions_from_file[mail][0] != question[mail][0]: # Проверка сопадения имени пользователя
                            return "Thanks, %s! Unfortunately, this account has another name. Access Date: %s" % (name, datetime.now().strftime("%d-%m-%Y"))
                        else:
                            for user_questions in questions_from_file[mail]: # Цикл по всем вопросам текущего пользователя в файле
                                if user_questions == question[mail][1]: # Если текущий вопрос совпадает с тем что уже есть в списке - ошибка
                                    is_exist_q = 1
                                    return "Thanks, %s! Unfortunately, You've already asked this question. Access Date: %s" % (name, datetime.now().strftime("%d-%m-%Y"))
                         
            if is_exist_q == 0: # Если вопрос уникальный
                questions_from_file[mail].append(question[mail][1])

            if is_exist_u == 0: # Если пользователя такого еще нет в списке, то добавляется
                questions_from_file.update(question)

            # Открываем файл для записи
            with open('static/json/questions.json', 'w') as file:
                json.dump(questions_from_file, file, indent=4)

        except FileNotFoundError:
            print("Файл не найден")
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON")
        except PermissionError:
            print("Недостаточно прав для доступа к файлу")
        except Exception as e:
            print(f"Произошла непредвиденная ошибка: {e}")

        return "Thanks, %s! The answer will be sent to the mail %s. Access Date: %s" % (name, mail, datetime.now().strftime("%d-%m-%Y"))