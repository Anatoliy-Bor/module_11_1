import requests
""" присваеваем переменной ответ с сайта к которому обращаемся"""
#response = requests.get('https://ya.ru/')
"""status_code 200 -  ответ страници что подключение успешно"""
#print(response.status_code)
"""headers - служебная инфа для обработки полученных данных, заголовок"""
#print(response.headers)
""" content получает строку в виде последоветельности байт"""
#print(response.content)
""" text - HTML код в виде текста"""
#print(response.text)

""" скачаем и сохраним страницу """
url = 'https://www.google.ru/search'
params = {'q': 'урбан университет'}
response = requests.get(url, params=params)
# print(response.text)
print(response.status_code, 'status_code')

# """ передача данных на сервер метод POST"""
# url = 'https://www.google.ru/post'
# params = [{ 'key': 'volume'}]
# response = requests.post(url, date=params)
