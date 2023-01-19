import re
import time
import aiohttp
import asyncio
import collections
from itertools import zip_longest


# A
def project_names_from_links(links: list):
    '''Принимает список ссылок на проекты на github.
    Выводит в консоль названия проектов на которые ведет ссылка.
    Ссылки вне формата игнорируются.
    https://github.com/miguelgrinberg/Flask-SocketIO >> Flask-SocketIO'''
    pattern = re.compile(r'^((https://)?github.com/)(\w+/)(?P<name>[\w\-]+)(\.git)?$')
    p_names = [res.group('name') for link in links if (res:= re.match(pattern, link))]
    print(*p_names, sep='\n')

# B
def lists_to_dict(keys: list, values: list) -> dict:
    '''Принимает два списка. Возвращает словарь.
    Ключи из списка keys, значения из списка values. 
    Если len(keys) < len(values) - недостающие ключи равны значению
    Если len(values) < len(keys) - значения равны None.
    Функция выводит результат в консоль и возвращает словарь'''
    result = {}
    for k, v in zip_longest(keys, values):
        if not k:
            k = v 
        result[k] = v 
    print(result)
    return result

# C
def abc_cba(items: list) -> list:
    '''Принимает список состоящий только из int и str
    Возвращает новый список. К строкам добавляется abc__ + str + __cba
    Числа возводятся в квадрат.'''
    print(res:= list(map(lambda it: f"abc_{it}_cba" \
        if isinstance(it, str) else it**2, items)))
    return res

# D
async def get_http(url='http://httpbin.org/delay/3', times=100):
    '''Функция исполняет 100 GET запросов к url.
    Выводит в консоль результат времени выполнения'''
    start_time = time.perf_counter() 
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(session.get(url)) for _ in range(times)]
        await asyncio.gather(*tasks)
    res_time = time.perf_counter() - start_time 
    print(f"{times} запросов выполнено за {res_time:.1f} секунд.")

# F
def time_it(func):
    '''декоратор который воводит в консоль время 
    выполнения функции или метода'''
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)
        res_time = time.perf_counter() - start_time 
        print(f"Метод {func.__name__} выполнен за {res_time:.3f} сек.")
        return res 
    return wrapper

def time_methods(cls):
    '''декоратор класса. При выполнении каждого метода, 
    выводит в консоль время его выполнения.'''
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, __name: str):
            try:
                return super().__getattribute__(__name)
            except AttributeError:
                pass 

            attr = getattr(self._obj, __name)

            if isinstance(attr, type(self.__init__)):
                return time_it(attr)
            return attr 
    return Wrapper

# E
@time_methods
class TextInfo:
    '''класс для получения информации о тексте'''
    def __init__(self, text: str):
        self.text = text
        self.text_list = re.findall(r'[a-zA-Z]+', text)

    def get_longest(self):
        '''возвращает самое длинное слово'''
        return max(self.text_list, key=len)

    def get_most_frequent(self):
        '''возвращает слово которое чаще всего встречается'''
        counter = collections.Counter(self.text_list)
        return counter.most_common(1)[0][0]
        
    def get_punctuation_num(self):
        '''возвращает количество знаков пунктуации'''
        return len(re.findall(r'[^\w\s]', self.text))

    def get_palindromes(self):
        '''принтит все палиндромсы'''
        unique_words = set(self.text_list)
        palindromes = [word for word in unique_words \
            if word[::-1] == word and len(word) > 1]
        print(*palindromes, sep=', ')


if __name__ == '__main__': 
    print('#A тест project_names_from_links'.center(60, '-'))
    links = ['https://github.com/miguelgrinberg/Flask-SocketIO',
        'https://github.com/miguelgrinberg/Flask-SocketIO.git',
        'https://www.google.com/asdasd/sdaasd']
    print('Ссылки:', links)
    project_names_from_links(links)
    print()
    print('#B тест функции list_do_dict'.center(60, '-'))
    test_cases = [
        ([1,2,3,4,5,6,7,8,9], list('abcd')),
        ([1,2,3,4], list('abcdefghi'))]
    print('Тестовые данные:', test_cases)
    for keys, values in test_cases:
        lists_to_dict(keys, values)
    print()
    print('#C тест функции abc_cba'.center(60, '-'))
    data = ['asd','a','asdas', 232, 'sf', 34, 65, '56']
    print('Тестовые данные:', data)
    print('Результат:', end='')
    abc_cba(data)
    print('#D тест async запросов'.center(60, '-'))
    asyncio.run(get_http())
    print()
    print('#E тест класса TextInfo'.center(60, '-'))
    with open('moby_dick_ch1.txt') as file:
        txt = file.read()

    text_info = TextInfo(txt)
    print('Самое длинное слово:', text_info.get_longest())
    print('Самое частое слово:', text_info.get_most_frequent())
    print('Кол-во знаков пунктуации:', text_info.get_punctuation_num())
    print('Палиндромы:')
    text_info.get_palindromes()