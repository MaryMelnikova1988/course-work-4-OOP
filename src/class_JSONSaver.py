import json
import os
from abc import ABC, abstractmethod


class Saver(ABC):
    """Абстрактный класс. Сохранение информации о вакансиях в файл"""
    @abstractmethod
    def __init__(self):
        pass
class JSONSaver(ABC):
    """Сохранение информации о вакансиях в JSON-файл"""

    def __init__(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def load_file(self):
        """Загрузка файла"""
        filename = "search_by_vacancies.json"
        with open(filename,'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def save_to_json(self, data) -> None:
        """Сохраняет данные в JSON-файл"""
        filename = "search_by_vacancies.json"
        with open(filename, "a", encoding='utf-8') as f:
            if os.stat(filename).st_size == 0:
                json.dump([data], f, ensure_ascii=False)
            else:
                with open(filename) as json_file:
                    data_list = json.load(json_file)
                data_list.append(data)
        # with open(filename, "w", encoding='utf-8') as json_file:
        #     json.dump(data, json_file, ensure_ascii=False)



    # не использую
    def add_vacancy(self, vacancy):
        """Добавление вакансии в json-файл"""
        new_vacancy = {
        'name': vacancy.name,
        'requirement': vacancy.requirement,
        'salary_from': vacancy.salary_from,
        'salary_to': vacancy.salary_to,
        'employer': vacancy.employer,
        'area': vacancy.area,
        'url': vacancy.url
        }
        data_add = list(self.load_file())
        data_add.append(new_vacancy)
        self.save_to_json(data_add)

    # не использую
    def get_vacancies_by_salary(self, salary: int):
        """Для получения топ-N вакансий по зарплате"""
        data_salary = []
        data = self.load_file()
        for item in data:
            if item['salary'] >= salary:
                data_salary.append(item)
        return data_salary


    def delete_vacancy(self,url_vacancy: str):
        """Удаление вакансии по url"""
        data = self.load_file()
        for item in data:
            if item['url']==url_vacancy:
                data.remove(item)
        return data


