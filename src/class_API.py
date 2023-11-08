from abc import ABC, abstractmethod
import requests
import json

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



class SuperJobAPI(API):
    """класс для работы с API c superjob.ru
              {
                "id":1,
                "title": "Россия"
            }"""

    def __init__(self, keyword: str):
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.params = {
            'keyword': keyword,
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

    def get_vacancies(self, pages_count=2):
        self.vacancies = []
        for page in range(pages_count):
            page_vacancies = []
            self.params['page'] = page
            print(f"({self.__class__.__name})Парсинг страницы {page} ", end=" ")
            try:
                page_vacancies = self.get_vacancies_response()
            except ParsingError as error:
                print(error)
            else:
                self.vacancies.extend(page_vacancies)
                print(f'Загружено вакансий: {len(page_vacancies)}')
            if len(page_vacancies)==0:
                break

class ParsingError(Exception):
    pass