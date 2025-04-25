import requests, os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

# URL для запроса
url = os.getenv("URL_WB_API")

# Параметры запроса
params = {"limit": 2, "offset": 0}

# Заголовки
headers = {"accept": "application/json", "Authorization": os.getenv("WB_API_KEY")}

# Отправка запроса
response = requests.get(url, params=params, headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    data = response.json()
    wb_prices = {
        item["nmID"]: item["sizes"][0]["price"] for item in data["data"]["listGoods"]
    }
    
    print(wb_prices)
    
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret_486432485699-o4nsk2117uphig7p15pjda710omongvk.apps.googleusercontent.com.json', scope)  # Замените на путь к вашему JSON-ключу
    gc = gspread.authorize(credentials)

    # Открываем таблицу (замените на название вашей таблицы)
    sh = gc.open("test_table")

    # Выбираем лист (можно по имени или индексу)
    worksheet = sh.get_worksheet(0)  # Первый лист

    # Ваш словарь
    data_dict = {32168349: 32354}

    # Подготавливаем данные для записи (каждая пара ключ-значение - новая строка)
    data_to_write = [[key, value] for key, value in data_dict.items()]
    
else:
    print(f"Ошибка: {response.status_code}")
