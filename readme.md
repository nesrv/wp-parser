# WB API


```bash

python3 -m venv venv

pip freeze > req.txt
pip install -r req.txt
```



## Метод предоставляет информацию о товарах по их артикулам: цены, валюту, общие скидки и скидки для WB Клуба.

[https://discounts-prices-api.wildberries.ru/api/v2/list/goods/filter?limit=20&offset=0](https://discounts-prices-api.wildberries.ru/api/v2/list/goods/filter?limit=20&offset=0)

```
curl -X 'GET' \
  'https://discounts-prices-api.wildberries.ru/api/v2/list/goods/filter?limit=20&offset=0' \
  -H 'accept: application/json' \
  -H 'Authorization: eyJhbGci..._ng'
```