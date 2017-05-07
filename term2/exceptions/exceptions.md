# Изключения (Exceptions)

Всеки път, когато използвате някой софтуер (било той уеб базиран или локален на устройството), от вашата гледна точка всичко може да върви гладко. Ако погледнет зад колисите, обаче, понякога може дори да ви се доплаче (хаха, тука имаше рима :Д). 

В много случаи програмата иска да изпълни нещо, но поради една или друга причина това не може да се случи, при което възниква грешка. С цел да продължи нормално работата си, софтуерът трябва да се погрижи за този случай, в който по принцип не сме искали да попаднем (да направим изключение за него).

Нека разгледаме конкретен пример. Разработвате програма, в която потребителят иска да отвори даден файл. Файлът, за съжаление, се оказва, че не съществува. Ако не се погрижим за този случай, програмата ще се счупи. Вместо да прекратява работата си, тя може да изведе съобщение към потребителя и да му каже, че файлът липсва.


## Изключения в Python
Докато пишем нашите скриптове, доста често възникват грешки в програмата. 

Някои от тях са от неправилен синтаксис:
```python
>>> if a < 3
  File "<interactive input>", line 1
    if a < 3
           ^
SyntaxError: invalid syntax
```

Други от невалидна операция:
```python
>>> 1 / 0
Traceback (most recent call last):
 File "<string>", line 301, in runcode
 File "<interactive input>", line 1, in <module>
ZeroDivisionError: division by zero
```

Или пък, както е споменато по-горе, се опитваме да отворим файл, който не съществува:
```python
open("imaginary.txt")
Traceback (most recent call last):
 File "<string>", line 301, in runcode
 File "<interactive input>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'imaginary.txt'
```

Тези грешки възникват докато се изпълнява програмата (runtime). Всеки път, когато възникне такава грешка, Python създава т. нар. `exception` обект. Ако не сме се погрижили за за случая, се извежда съобщение за грешката, заедно с кратки детайли относно как грешката се е получила. Тази информация е предназначена за нас, като програмисти, да разберем какъв е проблемът. Ако се върнем на примера с деленето на нула:
```python
>>> 1 / 0
Traceback (most recent call last):
 File "<string>", line 301, in runcode
 File "<interactive input>", line 1, in <module>
ZeroDivisionError: division by zero
```

виждаме на кой ред е възникнала грешката - `File "<interactive input>", line 1, in <module>` и каква точно е тя - `ZeroDivisionError: division by zero`. 

В Python има набор от вградени грешки (exceptions), които съответстват на определени проблеми в програмата. [Тук](https://docs.python.org/3/library/exceptions.html) можете да видите всичките, заедно с техните описания.

## Обработка

![](https://cdn.programiz.com/sites/tutorial2program/files/python-exception-handling_1.jpg)

Когато възникне грешка и тя не бъде обработена, текущият процес спира и предава грешката на извикващия процес. Ако и той не се погрижи, грешката се предава нагоре. Така, докато не се стигне до главния процес и ако грешката не бъде обработена никъде, програмата приключва работата си извънредно.

### Обработка на изключенията в Python

В Python грешките се обработват с помощта на ключовата дума `try`. След `try` трябва да има блок, в който да се изпълни критичния код (кодът, от който е възможно да се възпроизведе грешка). След което, кодът който обработва грешката, ако тя настъпи, трябва да се намира в `except` блок.

```python
try:
    f = open('random_file', 'r') # We try to open the file.
except:
    # The file is probably missing. An Error occured and this block will be executed.
    print('Sorry, but something went wrong with your file. Is it missing?')
```

Примерът по-долу добре показва как при възникване на грешка, при обработка програмата продължава. Пробвайте го и вижте резултата. Разгледайте какво и кога се случва:
```python
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)
```

### Обработка на специфични изключения
В примера по-горе не сме определили кои изключения(грешки) точно ще обработваме с `except` клаузата. Това не е добра практика. Обикновено знаем какви изключения искаме да обработваме и искаме да се занимаваме само с тях. Възникването на неочаквани изключения би било знак за бъг в програмата ни. За да забележим по-бързо проблема, тази грешка трябва да остане необработена и да развали нормалното изпълнение на програмата. С други думи - не сме очаквали нещо да се случи, ще е хубаво ако програмата ни крашне, че да имаме защо да кажем набор от обидни думи за нечии роднини и веднага да се заемем с проблема.

Как става обработката на изключения? Няма да ви кажа! Добре де.. 
Всяко възникнало изключение е създаден обект. Съответно този обект е описан със съответния клас. `except` ключовата дума може да приеме списък от изключенията, които трябва да се обработят в блока.

```python
def divide_by(number, divisor):
  try:
    return number / divisor
  except ZeroDivisionError:
    # handle division by zero exception
    pass

```

```python
def divide_string_nums(number, divisor):
  try:
    return int(number) / int(divisor)
  except (ZeroDivisionError, ValueError):
    # handle the two errors above
    pass
```

Ако е възможно да възникнат повече от едно изключения и трябва да се обработят поотделно.. Ами тогава плачем. Шегувам се. Има решение и за този случай:
```python
def divide_string_nums(number, divisor):
  try:
    return int(number) / int(divisor)
  except ValueError:
    # handle ValueError
    pass
  except ZeroDivisionError:
    # handle ZeroDivisionError
    pass
```

Тази комбинация също е възможна:
```python
try:
   # do something
   pass

except ValueError:
   # handle ValueError exception
   pass

except (TypeError, ZeroDivisionError):
   # handle multiple exceptions
   # TypeError and ZeroDivisionError
   pass

except:
   # handle all other exceptions
   pass
```

### Вложена try-except структура

Ето един пример за това как при възникване на грешка, тя се предава.

```python
try:

    try:
        f = open('numbers', 'r')
        number = int(f.readline())
    except ValueError:
        print('handling the value error')
        
except FileNotFoundError:
    print('handling FileNotFoundError)    
```

В случая имаме вложена try-except структура. Във вътрешния `try` блок отваряме файл, четем от него и се опитваме прочетения `string` да превърнем в число. Да кажем, че възможните грешки, които могат да възникнат са две:
1. Прочетеният `string` може да не може да се превърне в число. Ако във файла е записано 'abc' и се опитаме да го превърнем в число, ще имаме грешка. 
1. Файлът може да не съществува

В случай, че възникне първата грешка - `ValueError` - тогава тя ще бъде обработена във вътрешния `except` блок и външният дори няма да разбере, че нещо не е било наред. Ако се окаже, че файлът не съществува, тогава ще имаме `FileNotFoundError`. Python ще види, че тази грешка не може да бъде обработена във вътрешния `except` блок, затова разширява пространството, в което гледа и ще стигне до външния `except` блок. Идеята е, че тръгваме от вътре навън. По-долу има илюстрация за яснота. Прилича на поничка.

![](https://github.com/bkolarov/elsys_python_course_9a_2016/blob/master/term2/exceptions/resources/exceptions_dount1.jpg?raw=true)

Какво ще се случи, ако кодът в `try` блока е изнесен във функция?

```python
def convert_number_from_file():
  f = open('numbers', 'r')
  number = int(f.readline())

try:

    try:
        convert_number_from_file()
    except ValueError:
        print('handling the value error')
        
except FileNotFoundError:
    print('handling FileNotFoundError)    
```

Разлика в изпълнението няма да има. Ако възникне грешка във функцията, тя ще бъде предадена до мястото, където функцията е извикана (в случая `try` блока). Ако не бъде обработена във вътрешния `try`, ще отиде към външния и тн. 

Да кажем, обаче, че правим тази малка промяна:

```python
def convert_number_from_file():
  try:
    f = open('numbers', 'r')
    number = int(f.readline())
  except ValueError: # If ValueError occurs, it will be handled here. The caller won't even know about that.
    print('handling the value error')

try:

    try:
        convert_number_from_file()
    except ValueError: # This won't be called, because the function handled this exception by itself.
        print('handling the value error')
        
except FileNotFoundError: # This still will get called, because no one else handles this kind of error inside the outer try block.
    print('handling FileNotFoundError)    
```

В този случай при възникване на ValueError във функцията, тя ще обработи случая сама. Блокът, който обработва `ValueError` извън функцията, никога няма да бъде изпълнен.

![](https://github.com/bkolarov/elsys_python_course_9a_2016/blob/master/term2/exceptions/resources/exceptions_donut2.jpg?raw=true)
___
Полезни и използвани връзки:
* https://www.programiz.com/python-programming/exceptions
* https://www.programiz.com/python-programming/exception-handling
