import requests
import pprint

# response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('author', 'dante123456'))
#
# pprint.pprint(response.json())

token = 'b0dd88200bf7f2298657a9bc1d365450d0bd7b8b'   # не админ
#token  = 'c3de6737d99d50898c9d5f85f74a3e162e6c84d5'   # админ

headers = {'Authorization': f'Token {token}'}
#auth = ('valery','12345')  # admin
#auth = ('kosolapov','1234567890')   # no admin
#response = requests.get('http://127.0.0.1:8000/api/v0/task/', headers=headers)  # просмотр не админ
response = requests.get('http://127.0.0.1:8000/api/v0/variant/', headers=headers)   # нелзя не админ
#response = requests.get('http://127.0.0.1:8000/api/v0/variant/', auth=auth  )  # для базовой авторизации
pprint.pprint(response.json())