import sys
from pathlib import Path
from colorama import Fore, Back, Style, init
# Colorama doesn't work without the init() method


def get_dir_tree(path: Path, level:int = 1) -> None:  
    '''
    Рекурсивна функція обходу директорії із виведенням її дерева у консоль та записом до одноіменного файлу
    '''
    # Оголошуємо змінну file_tree у якості глобальної для звернення до неї 
    # при створенні та запису даних до файлу з інших методів скрипту
    global file_tree
    # Визначаємо відступи для більшої читабельності дерева в залежності від глибини занурення
    indentation = "  " * level
    # Проходимо по структурі дерева та у разі. якщо натрапляємо на директорію, викликаємо рекурсивно функцію.
    # Результати виводимо в консоль та записуємо до одноіменного файлу
    for dir in path.iterdir():
        if dir.is_dir():
            print(indentation + f"{Fore.LIGHTYELLOW_EX + Back.BLUE + dir.name + Style.RESET_ALL}")
            file_tree.write(f"{indentation}<<{dir.name}>>\n")        
            get_dir_tree(dir, level + 1)
        else:
            print(indentation + f"{Fore.LIGHTGREEN_EX + dir.name + Style.RESET_ALL}")
            file_tree.write(f"{indentation}  {dir.name}\n")
    
def read_command(command: list) -> None:
    '''
    Функція обробляє аргументи командної строки
    '''
    # Оголошуємо змінну file_tree у якості глобальної для звернення до неї 
    # при створенні та запису даних до файлу з інших методів скрипту
    global file_tree
    user_dir = Path(command).absolute()
    # Створюємо файл, який в своїй назві містить назву нашої директорії,
    # та в який буде записана інформація про структуру директорії
    # за умови, що директорія існує
    if user_dir.exists():
        file_tree = open(f"{user_dir}_dir_tree.txt", "w+")
        # У якості заголовка дерева визначаємо назву нашої директорії
        print(Fore.LIGHTYELLOW_EX + Back.BLUE + user_dir.name + Style.RESET_ALL)
        file_tree.write(f"<<{user_dir.name}>>\n")
    else:
        print("Невірно передано шлях до директорії!!!")
    # Викликаємо рекурсивну функцію обробки директорії
    get_dir_tree(user_dir)

def main() -> None:
    '''
    ТОЧКА ВХОДУ
    '''
    # Викликаємо метод init() бібліотеки colorama для коректної роботи
    init()
    # Оголошуємо змінну file_tree у якості глобальної для звернення до неї 
    # при створенні та запису даних до файлу з інших методів скрипту
    global file_tree
    # Якщо в користувач не буде вводити назву директорії для обробки скриптом, 
    # буде оброблена робоча директорія із файлом скрипта
    if len(sys.argv) > 1: 
        read_command(sys.argv[1])
    else:
        read_command(sys.argv[0])
    # Закриваємо наш файл
    file_tree.close()


if __name__ == "__main__":
    main()