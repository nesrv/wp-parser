

BASE_URL_ANALYTICS = "https://seller-analytics-api.wildberries.ru/"
BASE_URL_STATISTICS = "https://statistics-api.wildberries.ru"

#
PING_ANALYTICS = f"{BASE_URL_ANALYTICS}/ping"
PING_STATISTICS = f"{BASE_URL_STATISTICS}/ping"


PING1 = "https://common-api.wildberries.ru/ping" # +
PING2 = "https://content-api.wildberries.ru/ping" # +
PING3 = "https://seller-analytics-api.wildberries.ru/ping" # 
PING4 = "https://discounts-prices-api.wildberries.ru/ping" # 
PING5 = "https://statistics-api.wildberries.ru/ping" # 

# PRICES = "https://discounts-prices-api.wildberries.ru/ping"
PRICES1 = "https://content-api.wildberries.ru/content/v2/get/cards/list"


import os
import requests
import json

def check_wb_api_key(api_key):
    # URL для проверки API-ключа
    url = PING5
    
    # Заголовки с ключом
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        # Отправляем GET-запрос
        response = requests.get(url, headers=headers)
        
        # Проверяем статус ответа
        if response.status_code == 200:
            print("API-ключ действителен!")
            print(f"Ответ сервера: {response.text}")
        else:
            print(f"Ошибка проверки ключа: {response.status_code}")
            print(f"Сообщение: {response.text}")
            
    except requests.exceptions.RequestException as e:
        print(f"Произошла ошибка при проверке ключа: {e}")

# Пример использования

api_key = os.getenv("WB_API_KEY")
check_wb_api_key(api_key)