# Ламбда изрази

## Flashback

Преди да четете този урок, по-добре да сте прочели [детайлите за функциите](https://github.com/bkolarov/elsys_python_course_9a_2016/blob/master/term2/functions/function_details.md). 

От урока за функции трябва да е станало ясно, че функциите **не** са просто статично зададени, че ще са с еди какво си тяло, с еди какво си име и друго име не може да се използва за тази функция. Това **не е** така. Разбрахме, че функциите се създават динамично и че към техния обект сочи името, което сме дали при `def`, но можем да кажем това име да сочи към нещо друго ИЛИ да зададем друго име, което сочи към същата функция.

```python
def do_something():
	pass
  
do_nothing = do_something # now we have two names for the same function
do_something()
do_nothing()

do_something = 3
do_nothing()
do_something() # Error. This name is no longer pointing to a function
```

Щом функциите са обекти, можем да ги подаваме на други функции:
```python
def multiply_by_two(getter):
	return 2 * getter()
	
def get_number():
	return 10
	
result = multiply_by_two(get_number)
print(result) # Output: 20
```
## lambda

В Python освен с `def` има и друг начин за създаване на функция. Той е чрез ключовата дума `lambda`. 
```python
get_number = lambda: 10
```

`lambda: 10` ще създаде обект функция, съответно `get_number` ще сочи към нея. Тялото на функцията, дефинирана с `lambda` се намира от дясната страна на двете точки `:`. Това, което се намира от дясната страна на двете точки ще се изпълни, ще се изчисли (it will evaluate). Връщатана стойност на функцията, дефинирана с `lambda` е резултата от израза след двете точки. В нашия случай това е 10.

```python
get_number = lambda: 10
print(get_number()) # Output 10
```

```python
get_number = lambda: 2 + 5
print(get_number()) # Output 7
```

```python
get_number = lambda: 2 + 5 + 10
print(get_number()) # Output 17
```

```python
get_number = lambda: 2**3
result = get_number()
print(result) # Output 8
```

```python
get_number = lambda: 2*2
result = get_number()
print(result) # Output 4
```

Еквивалентът на този пример с `lambda` е този:
```python
def ten(): # this could be lambda: 10
	return 10
    
get_number = ten
print(get_number())
```

И `def ten(): return 10` и `lambda: 10` правят едно и също. Създават функция. Едната разликата е, че на `def` даваме име, което да сочи към създадената функция (`ten` в случая), докато `lambda` връща обекта на функцията и нуе трябва да кажем на някое име да сочи към нея (`get_number`) в случая. Другата разлика е, че на функцията дефинирана с `def` трябваше да кажем изрично да върне 10, докато на функцията, създадена с `lambda` написахме просто 10. Това е защото, както вече е споменато, `lambda` функциите връщат резултата от израза вътре в тялото им. Резултатът на 10 си е 10.

Друга разлика между `def` и `lambda` е, че в `def` можем да имаме г.д колкото си искаме операции в тялото на функцията, докато при `lambda` можем да имаме само едно нещо.

```python
def visit_grandmother():
	print('EAT EAT EAT')
	return 20
```

```python
# You can do that
def do_multiple_things():
	food_for_home = visit_grandmother()
	print('I overate again...')
	return food_for_home
```
```python
# ERROR ERROR ERROR
do_multiple_things = lambda: # you can't have new line
	food_for_home = visit_grandmother() # You can't use =. This is like two operations. First you call visit_grandmother() and then u asign the result to food_for_home.
	print('I overate again...') # you can't do multiple things
	return food_for_home # you can't use return
```
```python
# ERROR ERROR ERROR. You can't do that either
do_multiple_things = lambda: food_for_home = visit_grandmother(); print('I overate again...'); return food_for_home
```

Това което може да се направи е:
```python
eat_and_bring_food = lambda: visit_grandmother() # we are doing only one thing here
```
Това ще създаде функция, която ще връща резултата от `visit_grandmother()`. 

```python
eat_and_bring_food = lambda: visit_grandmother() # we are doing only one thing here
food = eat_and_bring_food()
print (food) # Output: 20
```
