

def search_vacancies():

    keywords = input('Введите поисковой запрос: \n').split()
    hh = HHApi(keywords)
    sj = SJApi(keywords)
    handler = JSONHandler([hh, sj])

    handler.save()

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
