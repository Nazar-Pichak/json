# json - (java-script object notation)

import json
import math
from datetime import datetime

def my_factorial(n):
    if n == 0:
        return 1
    return n * my_factorial(n - 1)

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def method_from_class(self):
        return f'The person has name {self._name} and age {self._age}'

person_var = Person('Alex', 20)


with open(r'C:\Users\Назар\Favorites\Desktop\PYTHON\EGOROV_CHANNEL_YOUTUBE\FILE_HANDLING\example.txt', 'r') as txt_file:
    reader = txt_file.read()

with open(r"C:\Users\Назар\Favorites\Desktop\PYTHON\EGOROV_CHANNEL_YOUTUBE\JSON\parsing_from_json.json", 'r') as json_file:
    deserialization_to_python = json.load(json_file)
    del deserialization_to_python['quiz']['maths']

    deserialization_to_python['Python_True_to_json'] = True
    deserialization_to_python['Python_False_to_json'] = False
    deserialization_to_python['Python_None_to_json'] = None
    deserialization_to_python['Python_Datetime_to_json'] = '{:%d/%m/%Y}'.format(datetime.now())
    deserialization_to_python['cyrillic_to_json'] = 'Ось нове значення до ключа в кирилиці'
    deserialization_to_python['integer_to_json'] = 10
    deserialization_to_python['float_to_json'] = 11.6
    deserialization_to_python['dict_to_json'] = {'name': 'Alex', 'age': 20}
    deserialization_to_python['list_to_json'] = [1, 2, 3, 4]
    deserialization_to_python['str_to_json'] = 'Text here...'
    deserialization_to_python['tuple_to_json'] = (1, 2, 3, 4)
    deserialization_to_python['module_function_to_json'] =  math.factorial(10)
    deserialization_to_python['own_function_to_json'] =  my_factorial(10)
    deserialization_to_python['file_to_json'] =  reader
    deserialization_to_python['method_from_class_to_json'] = person_var.method_from_class()

    
with open('parsed.json', 'w') as serialization_to_json:
    json.dump(deserialization_to_python, serialization_to_json, indent=4)
    

    

