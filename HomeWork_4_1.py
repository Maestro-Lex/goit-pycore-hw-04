def total_salary(path: str) -> tuple:
    '''
        Функція, яка аналізує цей файл і повертає загальну та середню 
        суму заробітної плати всіх розробників.
    '''
    with open(path, 'r') as salary_file:
        total_salary = 0
        average_salary = 0
        lines_counter = 0
        for line in salary_file:
            lines_counter += 1
            try:
                total_salary += float(line.strip().split(",")[1].strip())
            except Exception:
                print(f"{lines_counter}-й рядок файлу містить некоректні дані!")
            
        average_salary = total_salary/lines_counter
    return (total_salary, average_salary)


if __name__ == "__main__":
    try:
        total, average = total_salary('HomeWork_4_1.txt')
        print(f"Загальна сума заробітної плати: {total:.2f} грн, Середня заробітна плата: {average:.2f} грн")
    except FileNotFoundError:
        print("Такий файл не знайдено! Перевірте правільність назви файлу!")