import re 

'''A. Функция принимает в качестве аргумента набор ссылок. 
Ссылки имеют формат ссылок на проекты на гитхабе 
(например: https://github.com/miguelgrinberg/Flask-SocketIO, 
https://github.com/miguelgrinberg/Flask-SocketIO.git). 
Функция должна обработать полученные ссылки и вывести в консоль 
названия самих гит-проектов. Стоит рассмотреть защиту от ссылок "вне формата".'''
def project_names_from_links(links):
    def get_name_or_none(link):
        pattern = re.compile(r'^((https://)?github.com/)(\w+/)(?P<name>[\w\-]+)(\.git)?$')
        if (res:= re.match(pattern, link)):
            return res.group('name')
    print(*[name for link in links if (name:= get_name_or_none(link))], sep='\n')

'''B. Реализовать функцию, принимающую два списка и возвращающую словарь 
(ключ из первого списка, значение из второго), упорядоченный по ключам. 
Результат вывести в консоль. Длина первого списка не должна быть равна 
длине второго. Результат вывести в консоль.'''
def lists_to_dict(keys: list, values: list) -> dict:
    print(res:= dict(zip(keys, values)))
    return res 

'''C. Реализовать функцию с помощью методов map и lambda. Функция 
принимает список элементов (состоящий из строк и цифр), возвращает 
новый список, с условием - если элемент списка был строкой, в начало 
строки нужно добавить текст "abc_", в конец строки - "_cba". 
Если элемент был int - то его значение нужно возвести в квадрат. 
Результат вывести в консоль.'''
def abc_cba(items: list) -> list:
    # если это не строка и не число, остается без изменений
    if_int = lambda x: x**2 if isinstance(x, int) else x
    if_str = lambda x: f'abc_{x}_cba' if isinstance(x, str) else if_int(x)
    print(res:= list(map(if_str, items)))
    return res