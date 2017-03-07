# Модули #

Като цяло модулите в Python са просто файлове с `.py` разширение, като вътре в тях има имплементирани набор от функции. Модулите се използват от други модули, използвайки ключовата дума:
```python 
import
```
Всеки път, когато използваме някой модул, той се зарежда в изпълняващия се Python скрипт. 
Да кажем, че имаме скрипта `messenger.py`, който ще използва модула `greetings.py`. Приемаме, че и двата модула са в една директория:

### messenger.py ###
```python
import greetings # Python изпълнява нашия скрипт и зарежда модула greetings.py
```

### greetings.py ###
```python
def say_hi():
  print('Haiiiii')
```
___
### Важно ###
Сещате се как досега сме писали разни файлове, в които има функции и код, който е извън тези функции. Да кажем, че имаме файла `greetings.py`:


### greetings.py ###
```python
def say_hi():
  print('Haiiiii')
  
say_hi()
```

При изпълняване на командния ред `python3 greetings.py` в конзолата, веднага можем да кажем какво ще се случи:
* Python ще зареди скрипта ни
* ще прочете, че сме дефинирали функцията ```say_hi()```
* ще види, че я извикваме и ще я изпълни. Като резултат ще принтира 'Haiiiii' на екрана
    - Ако първо извикаме ```say_hi()``` и после я дефинираме, ще гръмне!

Връщаме се отново при ``` messenger.py ```. Имаме:
### messenger.py ###
```python
import greetings
``` 

### greetings.py ###
```python
def say_hi():
  print('Haiiiii')
  
say_hi()
``` 

Изпълняваме `python3 messenger.py` и виждаме, че при `import` на `greetings.py` се е извикала функцията `say_hi()`. Ако махнем извикването на функцията под нейната дефиниция, това няма да се случи.

`При import на модул, той се инициализира, като кодът вътре в него се изпълнява.`

Може да си го представите по следния начин - Каквото се е случвало досега, когато изпълним 
`python3 our_script.py`, това се случва и като използваме някой модул в нашия скрипт, посредством `import`.

___
### Още важно ###
Ако в модула, който използваме в нашия скрипт, има глобални променливи, то те остават едни и същи до края на изпълнението на скрипта ни. Изгубих ви? Споко :)


Ето го отново нашият модул `greetings.py`, но променен:

### greetings.py ###
```python
message = ''

def say_hi():
	print(message)

def set_bye():
	global message
	message = 'byeeee'

def set_hi():
	global message
	message = 'haiiii'

set_hi()
``` 

Имаме глобална променлива message. Тя може да бъде променяна с функциите ```set_hi()``` и ```set_bye()```. Вижда се, че след всички дефиниции се извиква set_hi(). Това какво значеше? - че ако изпълним ```python3 greetings.py``` или го използваме в друг модул с ```import greeetings```, ```set_hi()``` ще се извика и ```message``` ще се инициализира с ```'haiiii'```.

Ако не ми вярвате, пробвайте. И да ми вярвате, пак пробвайте!

### greetings.py ###
```python
message = ''

def say_hi():
	print(message)

def set_bye():
	global message
	message = 'byeeee'

def set_hi():
	global message
	message = 'haiiii'

set_hi()
``` 

### messenger.py ###
```python
import greetings

greetings.say_hi() # check the output
```
`python3 messenger.py`

Променяме леко `messenger.py`:
### messenger.py ###

```python
import greetings

greetings.say_hi() # check the output
greetings.set_bye()
greetings.say_hi() # check the output
```
`python3 messenger.py`

# МАЙМУНИ В РОКЛИ #
Привличам ви вниманието, тъй като тук трябва да се концентрирате повече.

Онова нещо, което пише по-горе - 'Ако в модула, който използваме в нашия скрипт, има глобални променливи, то те остават едни и същи до края на изпълнението на скрипта ни.'. Ето какво значи то:

Добавяме модула `greetings.py` веднъж. Извикваме `greetings.set_bye()` и вътре в него `message` вече e `'byeeee'`. Ако добавим още веднъж `greetings.py` с `import`, той **няма** да се инициализира отново. **Няма** отново да се извика 
`set_hi()`, съответно `message` ще бъде такова, каквото сме го оставили преди.


Това звучи като "дай пример".

### greetings.py ###
```python
message = ''

def say_hi():
	print(message)

def set_bye():
	global message
	message = 'byeeee'

def set_hi():
	global message
	message = 'haiiii'

set_hi()
```

### messenger.py ###
```python
import greetings

def print_greeting():
	import module1
	module1.say_hi() # check the output

greetings.say_hi() # check the output
greetings.set_bye()
greetings.say_hi() # check the output

print_greeting()
```
`python3 messenger.py`

Можем да го обобщим и по следния начин - В рамките на изпълнението на нашия скрипт, колкото и пъти да добавим един модул, неговото състояние е едно и също и **не се променя** със всеки следващ `import`.

Пробвайте и това:

### messenger.py ###
```python
import greetings

greetings.set_bye()

import greeter
greeter.greet()
```

### greetings.py ###
```python
message = ''

def say_hi():
	print(message)


def set_bye():
	global message
	message = 'byeeee'

def set_hi():
	global message
	message = 'haiiii'

set_hi()
```

### greeter.py ###
```python
import greetings

def greet():
	greetings.say_hi()
```

`python3 messenger.py`
___

# Пакети #
Когато работим по големи проекти, ако ги пишем, както трябва, ще се озовем с голямо количество файлове, които в нашия случай ще бъдат основно модули. За да можем, като програмисти, по-лесно да се оритентираме сред всичките тези модули, ние ги разделяме в пакети.

Представете си пакетите като папки. Те всъщност са си папки. Всеки пакет може да съдържа в себе си модули и други пакети. Модулите и пакетите в един общ пакет се очаква да имат обща смислена връзка помежду си.


Всеки пакет в Python **трябва** да съдържа специален файл с име `__init__.py`. Този файл казва на Python, че директорията, в която е, е Python пакет. Знаейки това, Python позволява този пакет да бъде използван с `import` също като модулите. 


За пример ще използваме файловете от раздела с модули. Ще разбием файловете по този начин:
```
messenger/
├── messenger.py
└── greet
    ├── __init__.py
    ├── greetings.py
    └── greeter.py
```

Ето ги и файловете, променени, така че да използват пакетите:
### dir messenger: ###
### messenger.py ###
```python
import greet.greetings as greetings

greetings.set_bye()

import greet.greeter as greeter
greeter.greet()
```

### dir greet: ###
### __init__.py ###
```python
#empty
```

### greeter.py ###
```python
import greet.greetings as greetings

def greet():
	greetings.say_hi()
```

### greetings.py ###
```python
message = ''

def say_hi():
	print(message)


def set_bye():
	global message
	message = 'byeeee'

def set_hi():
	global message
	message = 'haiiii'

set_hi()
```
Забележете, че, където използваме `import`, използваме пълния път до модула и името на модула, разделени с точка. 
___
`__init__.py` може да бъде по-полезен от това само да си стои празен и да гледа тъпо, докато Python го чете. 

Както вече знаете, един пакет може да съдържа много модули. В нашия случай `greet` съдържа `greetings.py` и `greeter.py`. Вместо да добавяме всеки модул поотделно, можем да кажем `import` на всички модули от пакета по следния начин:
`from packageName import *`

### messenger.py ###
```python
from greet import *

greetings.set_bye()
greeter.greet()
```
В някои случаи, обаче, някои модули извършват тежки операции при инициализация (кодът, който се изпълнява, когато ги добавим в друг модул) или задължават да бъдат добавени изрично като използваме `import` само с тяхното име. За да ограничим кои пакети да бъдат видими при използването на `from packageName import *`, на помощ идва магическата променлива `__all__`, която инициализираме в `__init__.py`. Тя представлява `list` от имената, които да бъдат видими.

### __init__.py ###
```python
__all__ = ['greeter']
```

### messenger.py ###
```python
from greet import *

greeter.greet()
greetings.set_bye() # ERROR
```
