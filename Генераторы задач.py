import random

def task_132():
    '''Генератор аналогичных задач: https://kuzovkin.info/one_exercise_1/132 '''
    for _ in range(5):
        number_1 = round(random.uniform(1, 10), 2)
        number_2 = round(random.uniform(1, 10), 2)

        expression = f"{number_1} * {number_2}"
        result = round(number_1 * number_2, 2)

    print(f"Задача: {expression}")
    print(f"Результат вычисления: {result}")

def task_139():
    for _ in range(5):
        number_1 = round(random.uniform(1, 10), 2)
        number_2 = random.randint(1, 10)

        expression = f"{number_1} / {number_2}"
        result = round(number_1 / number_2, 2)

    print(f"Задача: {expression}")
    print(f"Результат вычисления: {result}")

def task_154():
    for _ in range(5):
        number_1 = round(random.uniform(1, 10), 2)
        number_2 = random.randint(1, 100)
        number_3 = round(random.uniform(1, 10), 2)

        expression = f"{number_1} / {number_2} + {number_3}"
        result = round(number_1 / number_2 + number_3, 2)

    print(f"Задача: {expression}")
    print(f"Результат вычисления: {result}")

#if __name__ == '__main__':
