from source.hh_api.headhunter_api import HHApi
from source.jsonhandler.jsonhandler import JSONHandler
from source.sj_api.superjob_api import SJApi
from source.vacancies.vacancy import Vacancy


def search_vacancies():
    keywords = input('Введите поисковой запрос: \n')
    hh = HHApi(keywords)
    sj = SJApi(keywords)
    json_handler = JSONHandler([hh, sj])

    json_handler.save()

    all_vacancies = [Vacancy(
        id=vacancy['id'],
        url=vacancy['url'],
        name=vacancy['name'],
        salary=vacancy['salary'],
        description=vacancy['description'],
        requirements=vacancy['requirements'],
        area=vacancy['area'],
        platform=vacancy['platform'],
    ) for vacancy in json_handler.get_all_vacancies()]

    while True:
        top = int(input('Введите количество вакансий для вывода \n'))
        sort_vacancies = input('Хотите отсортировать по заработной плате? \n').lower()
        if sort_vacancies == 'да':
            all_vacancies.sort(
                key=lambda vacancy: vacancy.salary['from'] if vacancy.salary and 'from' in vacancy.salary and
                                                              vacancy.salary['from'] is not None else float(
                    '-inf'), reverse=True)
            for vacancy in all_vacancies[:top]:
                print(vacancy)
            break
        elif sort_vacancies == 'нет':
            for vacancy in all_vacancies[:top]:
                if vacancy.salary and 'from' in vacancy.salary:
                    print(vacancy)
            break
        else:
            print('Введите да или нет.')


if __name__ == '__main__':
    print(search_vacancies())
