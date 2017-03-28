# Flashback

Преди да четете този урок, по-добре прочетете [детайлите за функциите](https://github.com/bkolarov/elsys_python_course_9a_2016/blob/master/term2/functions/function_details.md). 

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
