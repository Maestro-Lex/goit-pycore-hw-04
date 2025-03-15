def get_cats_info(path: str) -> list:
    '''
        Функція, яка читає цей файл та повертає список словників з інформацією про кожного кота
    '''
    cats_info_list = []
    lines_counter = 0
    with open(path, 'r') as cats_info_file:
        for line in cats_info_file:
            lines_counter += 1
            try:
                cats_info_list.append({"id": line.strip().split(",")[0].strip(),
                                      "name": line.strip().split(",")[1].strip(),
                                      "age": int(line.strip().split(",")[2].strip()),})
            except Exception:
                print(f"{lines_counter}-й рядок файлу містить некоректні дані!")
    return cats_info_list


if __name__ == "__main__":
    try:
        print(get_cats_info('HomeWork_4_2.txt'))
    except FileNotFoundError:
        print("Такий файл не знайдено! Перевірте правільність назви файлу!")