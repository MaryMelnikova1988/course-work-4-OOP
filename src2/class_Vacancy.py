class Vacancy:
    """Класс для создания экземпляров и работы с ними"""
    def __init__(self, name: str, requirement:str, salary_from: int, salary_to: int, employer: str, area: str, url: str, currency="RUR"):
        self.name = name
        self.requirement = requirement
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.employer = employer
        self.area = area
        self.url = url
        self.currency=currency
        # self.all.append(self)

    def __str__(self):
        return (f'Название вакансии: {self.name }\n'\
                f'Требования: {self.requirement}\n'\
                f'Зарплата: {self.salary_from} - {self.salary_to} {self.currency}\n'\
                f'Работодатель: {self.employer}\n'\
                f'Местоположение (город): {self.area}\n'\
                f'Ссылка на вакансию: {self.url}\n')
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.requirement}, {self.salary_from},{self.salary_to}, {self.employer}, {self.area}, {self.url}, {self.currency})"

    # def __eq__(self, other):
    #     if type(other) == Vacancy:
    #         return self.salary_from == other.salary_from
    #     else:
    #         raise TypeError
    #
    # def __ne__(self, other):
    #     if type(other) == Vacancy:
    #         return self.salary_from != other.salary_from
    #     else:
    #         raise TypeError
    #
    # def __lt__(self, other):
    #     if type(other) == Vacancy:
    #         return self.salary_from < other.salary_from
    #     else:
    #         raise TypeError

    def __gt__(self, other):
        if type(other) == Vacancy:
            return self.salary_from > other.salary_from
        else:
            raise TypeError

    # def __le__(self, other):
    #     if type(other) == Vacancy:
    #         return self.salary_from <= other.salary_from
    #     else:
    #         raise TypeError
    #
    # def __ge__(self, other):
    #     if type(other) == Vacancy:
    #         return self.salary_from >= other.salary_from
    #     else:
    #         raise TypeError
    #
    # def sort_vacancies_salary_from(self):
    #     """Метод сортировки по зарплате"""
    #     return self.all.sort(reverse=True)

