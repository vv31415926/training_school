import requests
import os
import pprint
SERVER = 'http://127.0.0.1:8000/'
PAGE = 'api/task/'

#task = '9'

response = requests.get( os.path.join( SERVER, PAGE ) )
print( os.path.join( SERVER, PAGE ) )
print( response.status_code )
pprint.pprint( response.json() )