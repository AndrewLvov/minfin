# pip install requests
import requests
import re  # regular expressions, стандартная библиотека
# from requests import get

from lxml import html


def main():
    response = requests.get('http://minfin.com.ua/currency/auction/')
    # сервер отвечает HTTP OK (200), если данные получены и всё хорошо
    # response.status_code - тип ошибки
    # response.content - сама страница в HTML, строка
    # response.encoding - кодировка страницы
    if response.status_code != 200:  # 200 = HTTP OK
        print("Failed to get page")
        return -1

    # превратить байтовую строку из сети в unicode строку,
    # с которыми мы обычно работаем в Python
    unicoded_string = response.content.decode(response.encoding)
    # re.findall() вернёт список результатов вида ['0:26', '9:05', '10:31', ...]
    times = re.findall(r'\d{1,2}:\d\d', unicoded_string)

    # for t in times:
    #     print(t)
    # можно заменить на:
    # обьеденить все елементы из times в одну строку, разделяя элементы значением ", "
    print(", ".join(times))

    # tree = html.fromstring(response.content)
    # for data in tree.xpath('//table/'):
    #     pass


main()