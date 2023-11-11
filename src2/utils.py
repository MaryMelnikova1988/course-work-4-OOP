from pprint import pprint
from src2.class_Vacancy import Vacancy
from src2.class_API import HeadHunterAPI, SuperJobAPI

from src2.class_JSONSaver import *

def choice_keyword_HeadHunter():
    """для hh"""
    print("Введите ключевое слово для поиска. Например, python.")
    keyword = str(input("Ввод пользователя: "))
    hh_api = HeadHunterAPI(keyword)
    hh_data = hh_api.get_vacancies_response()
    vacancies = hh_api.get_from_hh(hh_data)
    saver = JSONSaver()
    form_list = saver.add_vacancies(vacancies)

    for item in form_list:
        print()
        pprint(item, sort_dicts=False)
    print()
    interface_sort(form_list)

def choice_keyword_SuperJob():
    """для sj"""
    print("Введите ключевое слово для поиска. Например, python.")
    keyword = str(input("Ввод пользователя: "))
    sj_api = SuperJobAPI(keyword)
    sj_data = sj_api.get_vacancies_response()
    vacancies = sj_api.get_from_sj(sj_data)
    saver = JSONSaver()
    form_list = saver.add_vacancies(vacancies)
    for item in form_list:
        print()
        pprint(item, sort_dicts=False)
    print()
    interface_sort(form_list)

def interface_sort(form_list):
    """интерфейс сохранения полученных данных(с сортировкой или без)"""
    print("""Отсортировать данные перед сохранением списка вакансий?
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
    print("""Введите число для нужной сортировки:
                      1 - по названию вакансии
                      2 - по названию города
                      3 - по возрастанию зарплаты
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

    elif user_choice == "0":
        exit()
    else:
        print("Ой, что-то пошло не так. Выход программы.")
        exit()

def choice_json_file():
    json_saver = JSONSaver()
    return json_saver.load_file()

#  НЕ ПОЛУЧАЕТСЯИ НЕ РАБОТАЕТ, ВСЕ ПЕРЕБРОВАЛА, НЕ ЗНАЮ, ГДЕ ЭТА ОШИБКА
# def choice_json_file():
    #
    # filename = "search_by_vacancies.json"
    # with open(filename, 'r', encoding='utf-8') as f:
    #     data = json.load(f)
    # pprint(data)
    # for item in load_file:
    #     print()
    #     pprint(item, sort_dicts=False)
    # print()
    # print("Редактируем?")
    # print("""Выберите число:
    # 1 - Сортировка по зп,
    # 2 - Удаление вакансии, выберите url
    # 0 - выход""")
    # user_choice = input("Ввод пользователя: ")
    # if user_choice == "1":
    #     ffff = json_saver.sort_vacancy()
    #     json_saver.save_to_json(ffff)
    #     print("Файл перезаписан")
    # elif user_choice == "2":
    #     vacancy_remove_url = input("Ввод пользователя: ")
    #     ffff = json_saver.delete_vacancy(vacancy_remove_url)
    #     json_saver.save_to_json(ffff)
    #     print("Файл перезаписан")

    # elif user_choice == "0":
    #     exit()
    # else:
    #     print("Ой, что-то пошло не так. Выход программы.")
    #     exit()
    #
    # print("Файл перезаписан")