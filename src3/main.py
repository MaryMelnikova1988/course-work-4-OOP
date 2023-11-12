from src3.utils import *


def main():
    print("Здравствуйте, пользователь. Поможем получить информацию о вакансиях с разных платформ в России.")

    while True:
        print()
        print("""Введите число для продолжения работы:
    1 - Создание топ-N вакансий с "HeadHunter" по ключевому слову
    2 - Создание топ-N вакансий с "SuperJob" по ключевому слову
    3 - Вывод сохраненного файла "Вакансии"
    0 - выход """)

        user_choice = input("Ввод пользователя: ")

        if user_choice == "1":
            choice_keyword_HeadHunter()

        elif user_choice == "2":
            choice_keyword_SuperJob()

        elif user_choice == "3":
            print()
            pprint(choice_json_file(), sort_dicts=False)

        elif user_choice == "0":
            break

        else:
            print("Ой, что-то пошло не так. Выход программы.")
            break


if __name__ == '__main__':
    main()