from datetime import datetime
from bottle import post, request, redirect
import re
import pdb
import json

@post('/home', method='post')
def my_form():
    question = {}
    mail = request.forms.get('ADRESS')
    name = request.forms.get('USERNAME')
    quest = request.forms.get('QUEST')  
    question[mail] = [name, quest]
    # pdb.set_trace()

    reg = r'^[a-zA-Z0-9]{2,}@[a-z]{2,}\.[a-z]{2,}$'

    error = ""

    if len(quest) < 1 or len(mail) < 1 or len(name) < 1:
        error += "All fields must be filled in. "

    if len(quest) < 4 or quest.isdigit():
        error += "The question is incorrect. "

    if (len(mail) < 8 or len(mail) > 255 or not re.match(reg, mail)) and len(mail) > 0: 
        error += "Mail entered incorrectly. "

    if not re.match(r'^[a-zA-Z]+$', name) and len(name) > 0:
        error += "Name entered incorrectly. "

    if len(error) > 0:
        return error
    else:
        try:
            flag = 0
            # Открываем файл для чтения
            with open('static/json/questions.json', 'r') as file:
                questions_from_file = json.load(file)
                for q in question.keys(): # Проходимся по всем ключам из словаря (почтам)
                    for q_f in questions_from_file.keys():
                        if q == q_f: # Ищем совпадения
                            flag = 1
                            if questions_from_file[q][1] != question[q][1]:
                                questions_from_file[q].append(question[q][1])
                            else:
                                return "Thanks, %s! Unfortunately, You've already asked this question. Access Date: %s" % (name, datetime.now().strftime("%d-%m-%Y"))
            
            if flag == 0:
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