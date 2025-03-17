'''
Модуль, який містить всі наші методи для бота
'''
from colorama import Fore, Style


def parse_input(user_input: str) -> list:
    '''
    Парсер команд
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: list, contacts: dict) -> str:
    '''
    Команда додання імені та номеру до списку контактів 
    '''
    try:
        name, phone = args
        contacts[name.capitalize()] = phone
        return f"{Fore.LIGHTGREEN_EX}Contact added.{Style.RESET_ALL}"
    except Exception:
        return f"{Fore.LIGHTRED_EX}Invalid command.{Style.RESET_ALL}"

def change_contact(args: list, contacts: dict) -> str:
    '''
    Команда зсіни номеру телефону за ім'ям контакту, у разі його наявності 
    '''
    try:
        name, phone = args
        if name.capitalize() in contacts.keys():
            contacts[name.capitalize()] = phone
            return f"{Fore.LIGHTGREEN_EX}Contact updated.{Style.RESET_ALL}"
        else:
            return f"{Fore.LIGHTRED_EX}There is no such contact!{Style.RESET_ALL}" 
    except Exception:
        return f"{Fore.LIGHTRED_EX}Invalid command.{Style.RESET_ALL}"

def show_phone(name: list, contacts: dict) -> str:
    '''
    Команда, що виводить номер телефону за за ім'ям контакту, у разі його наявності
    '''
    name = name[0]
    if name.capitalize() in contacts.keys():
        return contacts[name.capitalize()]
    else:
        return f"{Fore.LIGHTRED_EX}There is no such contact!{Style.RESET_ALL}" 

def show_all(contacts: dict) -> dict:
    '''
    Команда виводу всього списку контактів
    '''
    if contacts:
        return contacts
    else:
        return f"{Fore.LIGHTRED_EX}Contact list is empty!{Style.RESET_ALL}"