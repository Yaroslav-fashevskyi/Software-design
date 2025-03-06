# Використовуємо Python 3.12 як початковий образ
FROM python:3.12-slim

# Встановлюємо робочу директорію у контейнері
WORKDIR /task

# Копіюємо всі файли з поточної директорії у контейнер
COPY . /task

# Якщо є залежності (наприклад, в requirements.txt), їх потрібно встановити
# RUN pip install --no-cache-dir -r requirements.txt

# Вказуємо команду для запуску вашого файлу p1.py
CMD ["python", "p1.py"]
