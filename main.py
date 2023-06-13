from exceptions import InvalidRequest
from source.hh_api.headhunter_api import HHApi
from source.jsonhandler.jsonhandler import JSONHandler
from source.sj_api.superjob_api import SJApi
from concurrent.futures import ThreadPoolExecutor


def search_vacancies():
    while True:
        keywords = input('Введите поисковой запрос: \n')

        hh = HHApi(keywords)
        sj = SJApi(keywords)

        with ThreadPoolExecutor() as executor:
            hh_future = executor.submit(hh.get_vacancies)
            sj_future = executor.submit(sj.get_vacancies)

            try:
                hh_vacancies = hh_future.result()
            except InvalidRequest:
                print('Неверный запрос для HHApi')
                continue
            try:
                sj_vacancies = sj_future.result()
            except InvalidRequest:
                print('Неверный запрос для SJApi')
                continue
        platform_list = [hh_vacancies, sj_vacancies]
        all_vacancies = [vacancies for vacancies in platform_list]
        json_handler = JSONHandler(all_vacancies)

        json_handler.save()
        vacancies_obj = json_handler.get_all_vacancies()

        top = int(input('Введите количество вакансий для вывода \n'))
        while True:
            sort_vacancies = input('Хотите отсортировать по заработной плате? \n').lower()
            if sort_vacancies == 'да':
                vacancies_obj.sort(
                    key=lambda vacancy: vacancy.salary if vacancy.salary else 0, reverse=True)
                for vacancy in vacancies_obj[:top]:
                    print(vacancy)
                break
            elif sort_vacancies == 'нет':
                for vacancy in vacancies_obj[:top]:
                    print(vacancy)
                break
            else:
                print('Введите да или нет.')


if __name__ == '__main__':
    search_vacancies()
