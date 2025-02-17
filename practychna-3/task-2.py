#Завдання 2: Створити таблицю множення від 1 до 10

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{j} × {i} = {j * i}".ljust(12), end=" ")
    print()
