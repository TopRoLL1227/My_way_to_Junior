import json
# Допустимі типи значення в JSON: 1) string - str
#                                 2) number - int, float
#                                 3) JSON object - dict
#                                 4) boolean - bool
#                                 5) array - list, tuple
#                                 6) null - None

json_str = '{"id":235, "brand": "Nike", "qty": 84, "status": {"isForSale": true}}'

sneakers = json.loads(json_str)  # loads - один із атрибутів об'єктів JSON, а json - це екземляр класу модуль
print(type(sneakers))  # <class 'dict'>

print(sneakers['id'])  # 235
print(sneakers['status']['isForSale'])  # True

my_dict = {
    "id":235, 
    "brand": "Nike",  
    "qty": 84, 
    "status": {
        "isForSale": True
        }
}

bounty = json.dumps(my_dict)
print(type(bounty))  # <class 'str'>
print(bounty)  # {"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale": true}}


# Форматування JSON
my_format_dict = json.dumps(my_dict, indent=1)
print(my_format_dict)  # {
#                         "id": 235,
#                         "brand": "Nike",
#                         "qty": 84,
#                         "status": {
#                         "isForSale": true
#                          }
#                         }


json_array = '[{"a": 1}, {"b": 2}]'  # JSON формат

my_array = json.loads(json_array)
print(my_array)  # [{'a': 1}, {'b': 2}] список словарів Python
print(type(my_array))  # <class 'list'>

my_back_json = json.dumps(my_array)
print(type(my_back_json))  # <class 'str'>
print(my_back_json)  # [{"a": 1}, {"b": 2}] JSON формат



json_string = '{"id":235, "brand": "Nike", "qty": 84, "status": {"isForSale": true}}'
mars = json.loads(json_string)  # loads - один із атрибутів об'єктів JSON, а json - це екземляр класу модуль
print(type(mars))  # <class 'dict'>
json_from_dict = json.dumps(mars, indent=1)
print(json_from_dict)  # створив відформатований JSON з dict



