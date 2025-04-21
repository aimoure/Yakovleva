correct_mails = {
    "anna@gmail.com",
    "ann8@gmail.com",
    "Anna@gmail.com", 
    "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopas@gmail.com",
    "anna@qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopa.com",
    "anna@gmail.qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopa",
    "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopas@gmail.com.ru",
    "anna@qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopa.com.ru",
    "anna@gmail.qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopa.ru",
    "anna@gmail.com.qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopa",
    "an@gmail.com",
    "anna@gm.com",
    "anna@gmail.co", 
    "an@gmail.com.rus",
    "anna@gm.com.rus",
    "anna@gmail.co.rus",
    "anna@gmail.com.ru"
    }

uncorrect_mails = {
    "", # пустая строка
    "@.", # только @ и .
    "anna", # обычная строка
    "anna@", # только имя
    "@gmail", # нижний домен с @
    "@gmail." # нижний домен с @ b .
    "gmail.", # нижний домен с .
    ".com", # верхний домен с .
    "anna@gmail", # без верхнего домена
    "gmail.com", # без имени
    "anna@gmail.", # без верхнего домена с .
    "@gmail.com", # без имени с @,
    "anna@.com", # без нижнего домена
    "anna.gamil@com", # @ и . перепутаны местами
    "anna@gmail@com", # в обоих местах @
    "anna.gmail.com", # в обоих местах .
    "anna@gmail.com.", # . в конце
    "anna@@gmail.com", # лишняя @
    "anna@gmail..com", # лишняя .
    "annagmail.com", # нет @
    "anna@gmailcom", # нет .
    "a@gmail.com", # короткое имя
    "anna@g.com", # короткий нижний домен
    "anna@gamil.c", # короткий верхний домен
    "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm@gmail.com", # длинное имя
    "anna@qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm@gmail.com", # длинный нижний домен
    "anna@gamil.qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm@gmail", # длинный верхний домен
    "жnna@gmail.com", # русская буква в имени
    "anna@жmail.com", # русская буква в нижнем домене
    "anna@gmail.жom", # русская буква в верхнем домене
    "&nna@gmail.com", # некорректный символ в имени
    "anna@&mail.com", # некорректный символ в нижнем домене
    "anna@gmail.&om", # некорректный символ в нижнем домене
    "8nna@8mail.com", # цифра в начале имени
    "anna@8mail.com", # цифра в нижнем домене
    "anna@gmail.8om", # цифра в нижнем домене
    }