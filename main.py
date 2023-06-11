from source.hh_api.headhunter_api import HHApi
from source.jsonhandler.jsonhandler import JSONHandler
from source.sj_api.superjob_api import SJApi


def search_vacancies():
    keywords = input('Введите поисковой запрос: \n')
    hh = HHApi(keywords)
    sj = SJApi(keywords)
    platforms = [hh, sj]
    vacancies = [platform.get_vacancies() for platform in platforms]
    json_handler = JSONHandler(vacancies)

    json_handler.save()
    vacancies_obj = json_handler.get_all_vacancies()

    while True:
        top = int(input('Введите количество вакансий для вывода \n'))
        sort_vacancies = input('Хотите отсортировать по заработной плате? \n').lower()
        if sort_vacancies == 'да':
            vacancies_obj.sort(
                key=lambda vacancy: vacancy.salary['from'] if vacancy.salary and 'from' in vacancy.salary and
                                                              vacancy.salary['from'] is not None else float(
                    '-inf'), reverse=True)
            for vacancy in vacancies_obj[:top]:
                print(vacancy)
            break
        elif sort_vacancies == 'нет':
            for vacancy in vacancies_obj[:top]:
                if vacancy.salary and 'from' in vacancy.salary:
                    print(vacancy)
            break
        else:
            print('Введите да или нет.')


if __name__ == '__main__':
    print(search_vacancies())
