

def search_vacancies():

    keywords = input('Введите поисковой запрос: \n')
    hh = HHApi(keywords)
    sj = SJApi(keywords)
    json_handler = JSONHandler([hh, sj])

    json_handler.save()

    for vacancy in json_handler.platform.get_vacancies():
        Vacancy(
            id=vacancy['id'],
            name=
        )

    top = int(input('Введите количество вакансий для вывода'))
    sort_vacancies = input('Хотите отсортировать по заработной плате?').lower()

    while True:
        if sort_vacancies == 'да':
            handler.sort_vacancies(top, sort_vacancies)
            break
        elif sort_vacancies == 'нет':
            handler.get_all()
            break
        else:
            print('Введите да или нет.')


if __name__ == '__main__':
    print(search_vacancies())
