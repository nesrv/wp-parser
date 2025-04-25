import os
import requests
from dotenv import load_dotenv
from typing import Optional, Dict, List

load_dotenv()  # Загружаем переменные окружения из .env файла


class WBAPIClient:
    BASE_URL = "https://suppliers-api.wildberries.ru"
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("WB_API_KEY")
        if not self.api_key:
            raise ValueError("API key is required. Set WB_API_KEY in .env file or pass it directly.")
        
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        })
    
    def get_product_info(self, nm_id: int) -> Optional[Dict]:
        """Получить информацию о товаре по его артикулу (nm_id)"""
        url = f"{self.BASE_URL}/public/api/v1/info"
        params = {"nm": nm_id}
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error getting product info: {e}")
            return None
    
    def get_product_list(self, params: Optional[Dict] = None) -> List[Dict]:
        """Получить список товаров с возможностью фильтрации"""
        url = f"{self.BASE_URL}/content/v1/cards/cursor/list"
        
        default_params = {
            "sort": {
                "cursor": {
                    "limit": 100
                },
                "filter": {
                    "withPhoto": -1
                }
            }
        }
        
        if params:
            default_params.update(params)
        
        try:
            response = self.session.post(url, json=default_params)
            response.raise_for_status()
            data = response.json()
            return data.get("data", {}).get("cards", [])
        except requests.exceptions.RequestException as e:
            print(f"Error getting product list: {e}")
            return []
    
    def get_stock_info(self, warehouse_id: int) -> List[Dict]:
        """Получить информацию о остатках товаров на складе"""
        url = f"{self.BASE_URL}/api/v2/stocks"
        params = {"warehouseId": warehouse_id}
        
        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            return response.json().get("stocks", [])
        except requests.exceptions.RequestException as e:
            print(f"Error getting stock info: {e}")
            return []


if __name__ == "__main__":
    # Пример использования
    api_key = "your_api_key_here"  # Лучше хранить в .env файле
    client = WBAPIClient(api_key)
    
    # Получение информации о конкретном товаре
    product = client.get_product_info(12345678)  # Замените на реальный nm_id
    print("Product info:", product)
    
    # Получение списка товаров
    products = client.get_product_list({
        "sort": {
            "filter": {
                "price": {
                    "min": 1000,
                    "max": 5000
                }
            }
        }
    })
    print(f"Found {len(products)} products")
    
    # Получение информации о остатках
    stocks = client.get_stock_info(123)  # Замените на реальный ID склада
    print(f"Stock info for {len(stocks)} items")