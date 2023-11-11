from abc import ABC, abstractmethod
import requests
from src2.class_Vacancy import Vacancy

class API(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancies_response(self):
        pass

class HeadHunterAPI(API):
    """класс для работы с API c hh.ru
     {
    "url": "https://api.hh.ru/areas/113",
    "id": "113",
    "name": "Россия"
     },"""

    def __init__(self, keyword=""):
        self.url = 'https://api.hh.ru/vacancies'
        self.params = {
            'text': str(keyword),
            'area': 113,
            'only_with_salary': True,
            'page': None,
            'per_page': 100,
            'search_field': 'name',
            'archived': False,
            'currency': 'RUR'
        }
    def get_vacancies_response(self):
        """Возвращает вакансии по заданным параметрам"""
        response = requests.get(self.url, params=self.params)
        if response.status_code !=200:
            raise ParsingError(f"Ошибка получения вакансий. Статус {response.status_code}")
        return response.json()['items']

    @staticmethod
    def get_from_hh(vacancies: list):
        """Инициализация вакансий с сайта hh.ru """
        vacancies_list = []
        for item in vacancies:
            if item['salary']['currency'] == 'RUR':
                vacancy = Vacancy(item['name'], item['snippet']['requirement'], item['salary']['from'],
                                      item['salary']['to'], item['employer']['name'], item['area']['name'],
                                      item['alternate_url'])
                vacancies_list.append(vacancy)
        return vacancies_list


class SuperJobAPI(API):
    """класс для работы с API c superjob.ru
              {
                "id":1,
                "title": "Россия"
            }"""

    def __init__(self, keyword=""):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.params = {
            'keyword': str(keyword),
            'countries': 1,
            'is_archive': False,
            'count': 100,
            'page': None,
            'currency': 'rub'
        }

        self.headers = {
            'X-Api-App-Id': 'v3.r.137937068.d919351ebbc03a81c068011cc4b1436ee1832ebd.d46f74cba24758dad25ef6280c233d86e008fe71'
        }

    def get_vacancies_response(self):
        """Возвращает вакансии по заданным параметрам"""
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code !=200:
            raise ParsingError(f"Ошибка получения вакансий. Статус {response.status_code}")
        return response.json()['objects']

    @staticmethod
    def get_from_sj(vacancies: list):
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


class ParsingError(Exception):
    pass