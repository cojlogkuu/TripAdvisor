# 1️⃣ Базовий образ Python
FROM python:3.11-slim

# 2️⃣ Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# 3️⃣ Копіюємо файл залежностей
COPY requirements.txt .

# 4️⃣ Встановлюємо всі пакети
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Копіюємо весь проєкт у контейнер
COPY . .

# 6️⃣ Відкриваємо порт 5000 для Flask
EXPOSE 5000

# 7️⃣ Запускаємо застосунок
CMD ["python", "app.py"]
