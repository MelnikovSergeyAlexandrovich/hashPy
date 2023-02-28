import os
import csv
import hashlib
import uuid
from tabulate import tabulate
file_name2 = "hashpy.csv"

def input_op() -> None:
    while True:
        print("\n===================================================")
        func = input_int("Выберете действие.\n"
            "1. Войти в аккаунт.\n"
            "У вас до сих пор нет аккаунта?\n"
            "2. Зарегистрироваться\n"
            "3. Выйти\n","Ошибка. Введенно не целое число или же такой операции не существует")
        if func == 1:
            autorization(file_name2)
        elif func == 2:
            registration()
        if func == 3:
            return

def input_pos(prompt, error_message) -> str:
    """
    Функция, которая выводит сообщение о ошибке, если неправильно введенна строка(позиция). В другом случае возвращает введенную строку
    :param prompt:
    :param error_message:
    :return:
    """
    while True:
        _str = input(prompt)
        if str.isalpha(_str):
            return _str
        print(error_message)

def input_str(prompt, error_message):
    """
    Функция, которая выводит сообщение о ошибке, если неправильно введенна строка - ее длина меньше 3 и больше 21. В другом случае возвращает введенную строку
    :param prompt:
    :param error_message:
    :return:
    """
    while True:
        _str = input(prompt)
        str = len(_str)
        if str > 3 and str < 21:
            return _str
        print(error_message)

def input_ustr(prompt, error_message):
    """
    Функция, которая выводит сообщение о ошибке, если неправильно введенна строка. В другом случае возвращает введенную строку
    :param prompt:
    :param error_message:
    :return:
    """
    while True:
        try:
            _str = input(prompt)
            return _str
        except:
            print(error_message)

def input_float(prompt, error_message) -> float:
    """
    Функция, которая выводит сообщение о ошибке, если неправильно введенно число с плавающей запятой. В другом случае возвращает введенное число
    :param prompt:
    :param error_message:
    :return:
    """
    while True:
        try:
            return float(input(prompt))
        except:
            print(error_message)

def input_int(prompt, error_message) -> int:
    """
        Функция, которая выводит сообщение о ошибке, если неправильно введенно целое число. В другом случае возвращает введеное число
        :param prompt:
        :param error_message:
        :return:
        """
    while True:
        try:
            return int(input(prompt))
        except:
            print(error_message)

def interface_for_admin() -> None:
    global new_text
    print("Выберете действие:")
    op = int(input("1. Вывести всех пользователей\n2. Изменить пароль\n"))
    if op == 1:
        with open(file_name2) as f:
            reader = csv.DictReader(f, delimiter=',')
            sorted_dict = sorted(list(reader), key=lambda k: k['login'])
            print(tabulate(sorted_dict,headers="keys",tablefmt = 'grid'))
    elif op == 2:
        with open(file_name2, newline ='') as in_file:
            with open(r"C:\Users\User\Desktop\dublicateHash.csv", 'w',newline='',) as out_file:
                writerr = csv.writer(out_file)
                for row in csv.reader(in_file):
                    if row:
                        writerr.writerow(row)

        pos = input_int("Введите индекс пароля: ", "Индекс пароля введен неправильно.")
        r = csv.reader(open(r"C:\Users\User\Desktop\dublicateHash.csv"))
        lines = [l for l in r]
        list(r)
        salt = uuid.uuid4().hex
        writer = csv.writer(open(file_name2, 'w'))
        new_text = str(input("Введите новый пароль: "))
        new_text =  hashlib.sha256((new_text.encode() + salt.encode())).hexdigest()
        lines[pos][1] = new_text
        lines[pos][2] = salt
        writer.writerows(lines)

        with open(file_name2, newline ='') as in_file:
            with open(r"C:\Users\User\Desktop\dublicateHash.csv",'w', newline='') as out_file:
                writerr = csv.writer(out_file)
                for row in csv.reader(in_file):
                    if row:
                        writerr.writerow(row)

def interface_for_user() -> None:
    print("Скоро здесь появится интерфейс для обычного пользователя...")

def interface_for_seller() -> None:
    print("Скоро здесь появится интерфейс для продавца...")

def autorization(file_name2) -> None:
    global users
    print("==============================================")
    print("Войдите в аккаунт.")
    loginnn = input_str("Введите логин:\n","Недопустимый логин")
    passworddd = input_str("Введите пароль:\n","Недопустимый пароль")
    with open(file_name2) as f:
        reader = csv.DictReader(f, delimiter=',')
        sorted_dict = sorted(reader, key=lambda k: k['login'])
        for row in sorted_dict:
            login,password,salt,role = row
            if row["login"] == loginnn:
                csv_password = hashlib.sha256(passworddd.encode() + row["salt"].encode())
                csv_password = csv_password.hexdigest()
                if row["password"] != csv_password:
                    continue
                else:
                    print("Вы вошли!")
                    if row["role"] == "admin":
                        interface_for_admin()
                    elif row["role"] == "user":
                        interface_for_user()
                    elif row["role"] == "seller":
                        interface_for_seller()

def registration() -> None:
    global salt, csv_password
    print("==============================================")
    loginnn = input_str("Придумайте логин:\n", "Логин должен содержать от 4 до 20 символов")
    passworddd = input_str("Придумайте пароль:\n", "Пароль должен содержать от 4 до 20 символов")
    confirmed_passworddd = input_str("Подтвердите пароль:\n", "Пароль должен содержать от 4 до 20 символов")
    print("Выберете роль.")
    rolee = int(input("1. Обычный пользователь. \t2. Администратор\t3. Продавец\n"))
    if 1 > rolee > 4:
        print("Ошибка. Такой роли не существует")
    elif rolee == 1:
        rolee = "user"
        print(f"Ваша роль {rolee}")
    elif rolee == 2:
        rolee = "admin"
        print(f"Ваша роль {rolee}")
    else:
        rolee = "seller"
        print(f"Ваша роль {rolee}")
    saltt = uuid.uuid4().hex
    csv_password = hashlib.sha256((confirmed_passworddd.encode() + saltt.encode())).hexdigest()
    if passworddd == confirmed_passworddd:
        with open(file_name2) as f:
            reader = csv.DictReader(f, delimiter=',')
            sorted_dict = sorted(reader, key=lambda k: k['login'])
            print("Регистрация прошла успешно!")
            for row in sorted_dict:
                login, password, salt, role = row

        with open(file_name2, 'a') as f:
            f.write(f"\n{loginnn},{csv_password},{saltt},{rolee}")
            return

def main() -> None:
    if not os.path.exists(file_name2):
        with open(file_name2, 'w') as f:
            f.write("login,password,salt,role")
    if not os.path.exists("dublicateHash.cvs"):
        with open("dublicateHash.cvs", 'w') as f:
            f.write("login,password,salt,role")
input_op()

if __name__ == "__main__":
    main()
