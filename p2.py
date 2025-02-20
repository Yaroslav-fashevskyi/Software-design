"""
Завдання 2: Створити функцію, яка буде викликати генератор n-кількість разів.
 Назва функції - prime_num_getter. Аргументи функції - n.
 Функція повинна виводити певну кількість простих чисел. Дану функцію обгорнути у декоратор.
 Назва декоратора - timer_wrapper. Декоратор повинен обчислювати час, витрачений для виконання завдання.
"""
import time


def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Час виконання: {end-start:.4f} секунд")
    return wrapper

def prime_generator():
    num = 2
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1


@timer_wrapper
def prime_num_getter(n):
    prime_gen = prime_generator()
    primes = [next(prime_gen) for _ in range(n)]
    print(primes)


prime_num_getter(5000)



