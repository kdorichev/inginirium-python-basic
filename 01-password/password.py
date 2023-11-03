"""Задача 7. Напишите программу, которая создает случайный пароль 
из букв верхнего и нижнего регистра, а также цифр. 
Длина пароля должна быть случайной и варьироваться от 8 до 12 символов.
"""
import random

def generate_passwd():
    """Return a string of random symbols from the `alphabet` with length 8..12"""
    
    letters = "abcdefghijklmnopqrstuvwxyz"
    alphabet = letters + letters.upper() + "0123456789"
    alphabet_len = len(alphabet)
    passwd_len = random.randint(8,12)

    passwd = []
    
    for i in range(passwd_len):
        passwd.append(alphabet[random.randint(0, alphabet_len-1)])
    return "".join(passwd)


if __name__ == '__main__':
    print(generate_passwd())
