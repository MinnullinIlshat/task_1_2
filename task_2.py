import re
import time
import aiohttp
import asyncio

'''A. Функция принимает в качестве аргумента набор ссылок. 
Ссылки имеют формат ссылок на проекты на гитхабе 
(например: https://github.com/miguelgrinberg/Flask-SocketIO, 
https://github.com/miguelgrinberg/Flask-SocketIO.git). 
Функция должна обработать полученные ссылки и вывести в консоль 
названия самих гит-проектов. Стоит рассмотреть защиту от ссылок "вне формата".'''
def project_names_from_links(links):
    pattern = re.compile(r'^((https://)?github.com/)(\w+/)(?P<name>[\w\-]+)(\.git)?$')
    p_names = [res.group('name') for link in links if (res:= re.match(pattern, link))]
    print(*p_names, sep='\n')

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
    print(res:= list(map(lambda it: f"abc_{it}_cba" \
        if isinstance(it, str) else it**2, items)))
    return res

'''D. Реализовать функцию, которая замеряет время на исполнение100 
запросов к адресу: http://httpbin.org/delay/3. Запросы должны выполняться 
асинхронно. Допускается написание вспомогательных функций и использование 
сторонних библиотек. Результат замера времени выводит в консоль. 
# Ожидаемое время не должно превышать 10 секунд.'''
async def get_http(url='http://httpbin.org/delay/3', times=100):
    start_time = time.perf_counter() 
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(session.get(url)) for _ in range(times)]
        await asyncio.gather(*tasks)
    res_time = time.perf_counter() - start_time 
    print(f"{times} запросов выполнено за {res_time:.1f} секунд.")


if __name__ == '__main__': 
    asyncio.run(get_http())