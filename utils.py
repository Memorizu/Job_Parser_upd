import time


def user_interface(lst: list) -> dict:
    """Функция для создания интерфейса работы с пользователем"""
    return {index: value for index, value in enumerate(lst)}


def check_time_to_work(func):
    """Декоратор для просмотра времени выполнения функции"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Время выполнения {func.__name__}: {end - start} секунд")
        return result
    return wrapper
