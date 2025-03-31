from datetime import datetime
from bottle import post, request, redirect
import re
import pdb

@post('/home', method='post')
def my_form():
    questions = {}
    mail = request.forms.get('ADRESS')
    name = request.forms.get('USERNAME')
    quest = request.forms.get('QUEST')  
    questions[mail] = [name, quest]
    pdb.set_trace()

    reg = r'^[a-zA-Z0-9]{2,}@[a-z]{2,}\.[a-z]{2,}$'

    error = ""

    if len(quest) < 1 or len(mail) < 1 or len(name) < 1:
        error += "All fields must be filled in. "

    if (len(mail) < 8 or len(mail) > 255 or not re.match(reg, mail)) and len(mail) > 0: 
        error += "Mail entered incorrectly. "

    if not re.match(r'^[a-zA-Z]+$', name) and len(name) > 0:
        error += "Name entered incorrectly. "

    if len(error) > 0:
        return error

    return "Thanks, %s! The answer will be sent to the mail %s Access Date: %s" % (name, mail, datetime.now().strftime("%d-%m-%Y"))