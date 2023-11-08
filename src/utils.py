from src.class_JSONSaver import JSONSaver
from src.class_API import HeadHunterAPI, SuperJobAPI
from src.class_Vacancy import Vacancy
from pprint import pprint

def choice_HeadHunter():
        print("""Введите число для продолжения работы:
    1 - Выборка вакансий будет выполнена по желаемой зарплате (большей или равной)
    2 - Выборка вакансий будет выполнена по ключевому слову(профессии)
    0 - Выход""")
        user_choice = input("Ввод пользователя: ")

        if user_choice == "1":
            choice_salary()

        elif user_choice == "2":
            choice_keyword_hh()

        elif user_choice == "0":
            exit()

        else:
            print("Ой, что-то пошло не так. Выход программы.")
            exit()


def choice_salary():
    salary_dream = int(input("Введите желаемую зарплату в рублях числом. Например, 50000. Ввод:"))
    top_list_count = int(input("Введите число для создания N-топ по ЗП. От 1 до 20. Ввод: "))
    if salary_dream > 0 and 0 < top_list_count < 21:
        data_salary = []
        hh_api = HeadHunterAPI()
        hh_data = hh_api.get_vacancies_response()
        vacancies = get_from_hh(hh_data)
        form_list = []
        for vacancy in vacancies:
            new_vacancy = {
            'name': vacancy.name,
            'requirement': vacancy.requirement,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'currency': 'RUR',
            'employer': vacancy.employer,
            'area': vacancy.area,
            'url': vacancy.url
            }
            form_list.append(new_vacancy)
        # saver = JSONSaver()
        # saver.save_to_json(form_list)
        # form_list_json = saver.load_file()
        a=1
        i=1
        while a <= top_list_count:
            for item in form_list:
                i+=1
                if type(item['salary_from']) == int or type (item['salary_to']) == int:
                    if (item['salary_from'] >= salary_dream) or (item['salary_to']>= salary_dream):
                        data_salary.append(item)
                        if i == len(form_list):
                            break
        if len(data_salary)==0:
            print("Вакансий не найдено по такой зарплате. Выход")
            exit()
        elif 1<=len(data_salary)<=top_list_count:
            print(f"Получен список из {len(data_salary)} желаемых зарплат")
            print()
            for item in data_salary:
                print()
                pprint(item, sort_dicts=False)
            print()
            print("""Отсортировать данные перед сохранением списка вакансий?
                     Выберите число:
                     1 - да
                     2 - нет
                     0 - выход""")
            user_choice = input("Ввод пользователя: ")
            if user_choice == "1":
                user_sort(data_salary)

            elif user_choice == "2":
                saver = JSONSaver()
                saver.save_to_json(data_salary)
                print("Файл сохранен")

            elif user_choice == "0":
                exit()

            else:
                print("Ой, что-то пошло не так. Выход программы.")
                exit()
        else:
            print("Ой, что-то пошло не так. Выход программы.")
            exit()

def choice_keyword_hh():
    print("Введите ключевое слово для поиска. Например, python.")
    keyword = str(input("Ввод пользователя: "))
    hh_api = HeadHunterAPI(keyword)
    hh_data = hh_api.get_vacancies_response()
    vacancies = get_from_hh(hh_data)
    form_list = []
    for vacancy in vacancies:
        new_vacancy = {
            'name': vacancy.name,
            'requirement': vacancy.requirement,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'currency': 'RUR',
            'employer': vacancy.employer,
            'area': vacancy.area,
            'url': vacancy.url
        }
        form_list.append(new_vacancy)
    for item in form_list:
        print()
        pprint(item, sort_dicts=False)
    print()
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

def get_from_hh(vacancies: list):
    """Инициализация вакансий с сайта hh.ru """
    vacancies_list = []
    for item in vacancies:
        if item['salary']['from']:
            if item['salary']['currency'] == 'RUR':
                vacancy = Vacancy(item['name'], item['snippet']['requirement'], item['salary']['from'],
                                  item['salary']['to'], item['employer']['name'], item['area']['name'],
                                  item['alternate_url'])
                vacancies_list.append(vacancy)
    return vacancies_list

def user_sort(list_):
    """для hh"""
    print("""Введите число для нужной сортировки:
                  1 - по названию вакансии
                  2 - по названию города
                  3 - по возрастанию зарплаты
                  0 - выход""")
    user_choice = input("Ввод пользователя: ")
    if user_choice == "1":
        sorted_list = sorted(list_, key=lambda x: x['name'])
        saver = JSONSaver()
        saver.save_to_json(sorted_list)
        print("Файл сохранен")

    elif user_choice == "2":
        sorted_list = sorted(list_, key=lambda x: x['area'])
        saver = JSONSaver()
        saver.save_to_json(sorted_list)
        print("Файл сохранен")

    elif user_choice == "3":
        print("Сортировка идет по зарплате 'от'")
        sorted_list = sorted(list_, key=lambda x: x['salary_from'])
        saver = JSONSaver()
        saver.save_to_json(sorted_list)
        print("Файл сохранен")

    elif user_choice == "0":
        exit()
    else:
        print("Ой, что-то пошло не так. Выход программы.")
        exit()


def choice_SuperJob():
    """Дописать по аналогии с hh"""
    pass

def  get_from_sj(vacancies: list):
    """инициализация c sj"""
    vacancies_list = []
    for item in vacancies:
        if item['candidat']:
            if item['payment_to']:
                if item['currency'] == 'rub':
                    vacancy = Vacancy(item['profession'], item["candidat"], item["payment_from"],
                                  item["payment_to"], item["client"]["title"], item["town"]["title"],
                                  item["link"])
                    vacancies_list.append(vacancy)
    return vacancies_list


def choice_json_file():
    json_saver = JSONSaver()
    return json_saver.load_file()