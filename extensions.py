import requests
import json
from config import keys

class APIException(Exception):
    pass

class CryptoConvert:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            amount = float(amount)
        except ValueError:
            raise APIException('Третий параметр должен быть числом!')
        if amount < 0:
            raise APIException('Третий параметр должен быть больше 0!')

        try:
            check_qoute = keys[quote]
        except KeyError:
            raise APIException(f'Валюты {quote} нету!')

        try:
            check_base = keys[base]
        except KeyError:
            raise APIException(f'Валюты {base} нету!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={check_qoute}&tsyms={check_base}')
        text = json.loads(r.content)
        total_sum = text[keys[base]] * int(amount)
        return total_sum

