from colorama import Fore, Style, init
# Colorama doesn't work without the init() method
# Імпортуємо наш модуль з командами
import hw_4_4_module as methods


def main():
    '''
    ТОЧКА ВХОДУ
    '''
    # Викликаємо метод init() бібліотеки colorama для коректної роботи
    init()
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        # Перевіряємо наявність вводу і, якщо нічого не введено, повторюємо запит
        try:
            command, *args = methods.parse_input(user_input)
        except Exception:
            continue
        # Обробка введеного запиту
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(methods.add_contact(args, contacts))
        elif command == "change":
            print(methods.change_contact(args, contacts))
        elif command == "phone":
            print(f"{Fore.LIGHTBLUE_EX}{methods.show_phone(args, contacts)}{Style.RESET_ALL}")
        elif command == "all":
            print(f"{Fore.LIGHTBLUE_EX}{methods.show_all(contacts)}{Style.RESET_ALL}")
        else:
            print(f"{Fore.LIGHTRED_EX}Invalid command.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()