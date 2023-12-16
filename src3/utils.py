from pprint import pprint

from src3.class_API import HeadHunterAPI, SuperJobAPI
from src3.class_JSONSaver import JSONSaver

def choice_keyword_HeadHunter():
    keyword = input("Введите ключевое слово для поиска. Например, python. Ввод пользователя: ")
    hh_api = HeadHunterAPI(keyword)
    json_saver = JSONSaver()
    hh_vacancies = hh_api.get_vacancies_response()
    vacancies_list = hh_api.get_from_hh(hh_vacancies)
    vacancies_ = json_saver.add_vacancies(vacancies_list)
    top_n_edit =get_top_n(vacancies_)

    for item in top_n_edit:
        print()
        pprint(item, sort_dicts=False)
    print()

    interface_sort(top_n_edit)

def choice_keyword_SuperJob():
    keyword = input("Введите ключевое слово для поиска. Например, python. Ввод пользователя: ")
    superjob_api = SuperJobAPI(keyword)
    json_saver = JSONSaver()
    superjob_vacancies = superjob_api.get_vacancies_response()
    vacancies_list = superjob_api.get_from_sj(superjob_vacancies)
    vacancies_ = json_saver.add_vacancies(vacancies_list)
    top_n_edit = get_top_n(vacancies_)

    for item in top_n_edit:
        print()
        pprint(item, sort_dicts=False)
    print()

    interface_sort(top_n_edit)

def choice_json_file():
    json_saver = JSONSaver()
    return json_saver.load_file()

def get_top_n(vacancies_):
    top_n = int(input("Введите количество вакансий для вывода в топ N (N принимает значения от 1 до 30): "))
    salary_top_n = int(input("Введите зарплату для вывода в топ N: "))

    if 0 < top_n < 31 and salary_top_n > 0:
        i = 1
        data_salary = []
        for item in vacancies_:
            if (item['salary_from'] > salary_top_n) or (item['salary_to'] > salary_top_n):
                data_salary.append(item)
                i += 1
        if 0 < len(data_salary) < top_n:
            print(f"Вакансий получилось меньше требуемого: {len(data_salary)}")

        elif len(data_salary) == 0:
            print("Вакансии не найдены")

        elif len(data_salary) > top_n:
            data_salary = data_salary[:top_n]

    else:
        print("Ой, что-то пошло не так. Выход программы.")
        exit()

    return data_salary

def interface_sort(form_list):
    """интерфейс сохранения полученных данных(с сортировкой или без) и удаления"""
    print("""Поредактируем данные (сортировка, удаление) перед сохранением списка вакансий?
                 Выберите число:
                 1 - да
                 2 - нет
                 0 - выход""")
    user_choice = input("Ввод пользователя: ")
    if user_choice == "1":
        user_sort(form_list)

    elif user_choice == "2":
        saver = JSONSaver()
        saver.save_to_json(form_list)
        print("Файл сохранен")

    elif user_choice == "0":
        exit()

    else:
        print("Ой, что-то пошло не так. Выход программы.")
        exit()


def user_sort(form_list):
    """Сортировки на выбор: для hh и sj"""
    print("""Введите число для нужной нужной операции с данными:
                      1 - сортировка по названию вакансии
                      2 - сортировка по названию города
                      3 - сортировка по возрастанию зарплаты (по значению: от)
                      4 - удаление вакансии из списка по url             
                      0 - выход""")
    user_choice = input("Ввод пользователя: ")
    if user_choice == "1":
        sorted_list = sorted(form_list, key=lambda x: x['name'])
        saver = JSONSaver()
        saver.save_to_json(sorted_list)
        print("Файл сохранен")

    elif user_choice == "2":
        sorted_list = sorted(form_list, key=lambda x: x['area'])
        saver = JSONSaver()
        saver.save_to_json(sorted_list)
        print("Файл сохранен")

    elif user_choice == "3":
        print("Сортировка идет по зарплате 'от'")
        sorted_list = sorted(form_list, key=lambda x: x['salary_from'])
        saver = JSONSaver()
        saver.save_to_json(sorted_list)
        print("Файл сохранен")

    elif user_choice == "4":
        url_vacancy_delete = input("Введите url из списка для удаления позиции: ")
        json_saver = JSONSaver()
        del_data=json_saver.delete_vacancy(url_vacancy_delete,form_list)
        json_saver.save_to_json(del_data)
        print("Файл сохранен")

    elif user_choice == "0":
        exit()
    else:
        print("Ой, что-то пошло не так. Выход программы.")
        exit()

