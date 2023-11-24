import requests
from decorator_2 import logger

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = 'dict.1.1.20230901T100704Z.00fd6b0137cd82ed.b2f5ad40859f277502653463390e0e7a6eed5aad'
path = 'Переводчик.log'
@logger(path)
def translate_word(word):
    response = requests.get(f'{url}?key={token}&lang=ru-en&text={word}')
    dictionary = response.json()
    trans_word = dictionary.get('def')[0].get('tr')[0].get('text')
    return trans_word


if __name__ == '__main__':
    word = 'машина'
    translate_word(word)

