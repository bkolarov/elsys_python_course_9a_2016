Всички сте използвали for цикъла. Той какво представлява с прости думи?
- `for итерираща_променлива in някаква_поредица`. В дефиницията на `някаква_поредица` може да влязат `list`, `tuple`, `set` и тн. Променливи от всички тези типове можем да използваме с цикъла `for`. Друго нещо, което можем да използваме вместо някой обект от някой такъв тип е например функцията `range()`. С `range(10)` ще можем да итерираме по всички цифри от 0 до 9. 

```python
numbers_list = [1,2,3]
for i in numbers_list:
	print(i)
```

```python
numbers_tuple = (1,2,3)
for i in numbers_tuple:
	print(i)
```

```python
for i in range(10):
	print(i)
```

```python
# same as the previous one
range_10 = range(10)
for i in range_10:
	print(i)
```

Какво обаче прави тези типове и функции толкова специални, че да можем да итерираме по тях? Общото между тях е, че всички те са итератори. `list` е итератор, `tuple` е итератор, функцията `range()` връща итератор и тн.

# Итератори #

Какво е итератор? Като цяло итератор е нещо, по което може да се итерира. (Yeah.. very useful... thanks) Итератор е обект, който може да се използва във `for` цикъл. 

Какво прави един обект итератор? За да бъде един обект итератор, той трябва да принадлежи на клас. Нека нашият обект, който ще е итератор, да принадлежи на този клас:

```python
# Not valid iterator
class OurIterator:
	def __init__(self):
		pass
		
obj = OurIterator()
```

Да бъде нашият обект дефиниран с клас не е достатъчно, за да бъде итератор. Класът трябва да има още нещо специално в него.

Дами и господа, представяме ви магическото шоу `Магически Методи` в Python.

### Магически Методи ###
Това са методи, които се отличават от останалите със:
 1. Не ги извикваме ние, а вместо това Python ги извиква, когато прецени, че трябва
 1. Имената на тези методи започват и завършват с `две долни черти`. Пример: `__init__(slef)`
    - Точно така, \_\_init\_\_, който по щастлива случайност (не е случайност) е дефиниран в нашия клас по-горе, е магически метод. Python го извиква, след като създаде нашия обект от този клас, за да инициализираме в него променливите си в класа.
	
Ако се чудите и си казвате "Добре де.. аз от къде да знам кои са магическите методи, които Python познава и извиква?" - ами описани са в документацията :)))) Аз, за ваше щастие, няма да ви карам да ходите и да ги търсите, а вместо това директно ви казвам тези, които са ни необходими за целите на обучението. Приемете го като договорка между вас и тези, които са създали Python. Договорката е такава:
Python казват: Ние ще търсим за следните магически методи, когато са ни необходими - (постави поредидца от магически методи тук). Този метод ще е за това, другият метод ще е за това и тн. Ако ви интересува кои са тези методи и кой за какво служи, можете да проверите в документацията.
Ние отговаряме: Добре, мерси. Сега ни трябва магическият метод, който прави един клас итератор.

Връщаме се отново при итераторите. Казахме, че итератор е обект от тип клас, който трябва да има нещо специално в себе си. Това специално нещо в себе си е магическият метод `__iter__()`.

```python
# Still not valid iterator
class OurIterator:
	def __init__(self):
		pass
		
	def __iter__(self):
		pass
	
obj = OurIterator()
```

Видите ли, имаме функцията `__iter__()`, която е магическа. Какво означава това пак? Означава, че Python ще я извика, когато му е необходимо. Това, разбира се, е необходимо например, когато използваме нашия обект в цикъл `for`.
Да обобщим с пример:

```python
# Still not valid iterator
class OurIterator:
	def __init__(self):
		pass
		
	def __iter__(self):
		pass
	
obj = OurIterator()
for a in obj: # Python calls __iter__() somewhere in the backscenes
	pass
```

Ако имахме следното:

```python
# Still not valid iterator
class OurIterator:
	def __init__(self):
		pass
		
obj = OurIterator()
for a in obj: # No __iter__() method, Python cries, throws an error and gets angry, or makes you angry. It's your fault tho...
	pass
```

*Бележка: Изпробвайте дадените примери и вижте резултатите.*

<br>

Ако обърнете внимание на коментара над класа, там пише, че все още не е валиден итератор. В този момент си казваме: 'Добре, нали дефинирах магическата функция `__iter__()`, значи нашият клас е итератор? Какъв е проблемът? 

Да. Нашият клас е итератор, но почти. Дефинирахме нашата функция `__iter__()`, но не казахме какво прави тя, какво връща, знаем само, че Python я извиква (примерно, ако използваме обекта във `for`), но толкова. Гмуркаме се в детайлите:
1. `__iter__()` е функция, която Python извиква, когато искаме да итерираме.
2. `__iter__()` трябва да върне обект, който да може да бъде итериран.

Чакай, чакай чакай.... Какво? Не е ли итераторът обекта, който може да бъде итериран? Не. Итераторът е нещото (обект от съответния клас), което има функцията `__iter__()`, **която** връща обект, който може да бъде итериран.

Ето какво прави `for` - На него сме подали обект, който е итератор (има функцията `__iter__()`). 
```python
obj = OurIterator()
for a in obj:
	pass
```
`for` извиква функцията `__iter__()` по начин, който можем да представим така:
```python
iterable = iter(obj)
```
*`iter()` е вградена в Python функция (също като print()), която казва на python да извика `__iter__()` на обекта.*

Съответно се очаква `__iter__()` да върне обект, който може да бъде итериран (iterable на английски). Обектът, който може да бъде итериран, е обектът, който дава всяка следваща стойност, когато въртим цикъла.

Какво прави един обект `iterable`? За да бъде един обект `iterable`, класът му трябва да имплементира в себе си магическия метод - `__next__()`. 

```python
class OurIterator:
	def __init__(self):
		pass
		
	def __iter__(self):
		return self
		
	def __next__(self):
		pass
	
obj = OurIterator()
for a in obj: # Python calls iter on obj: iterable = iter(obj) - and then starts iterating by doing this: а = next(itreable), а = next(itreable), а = next(itreable) etc.
	pass
```

*Бележка: Както имаме функцията iter(obj), която извиква `__iter__()` на обекта и очаква тя да върне `iterable`, така и функцията next(obj) извиква `__next__()`, за да вземе следващата стойност.*

В посочения пример `OurIterator` е и итератор и може да бъде итериран (it's both an iterator and iterable). `iterator` е, защото има функцията `__iter__()`, която връща `iterable`. Обектът, който връща е същият, на който е извикано `__iter__()`. Той е и `iterable`, защото има функцията `__next__()`. В нашия случай `iterator` обектът и `iterable` обектът са един и същи.

```python
class OurIterator:
	def __init__(self):
		pass
		
	def __iter__(self):
		return self
		
	def __next__(self):
		pass
	
obj = OurIterator()
# We have '__iter__()`, we can call iter(obj)
iterable = iter(obj) # In our case this will return obj (see how __iter__() returns self). obj is iterable because it has __next__()
# In this case iterator is the same as obj, because __iter__() returns self.
value1 = next(iterable)
value2 = next(iterable)
```

Все още не сме готови обаче... Нека дадем смисъл на нашия клас `OurIterator` и го направим итератор, който ще има същата работа като `range()`. Тя ще е при итериране да дава числата от 0 до максималното подадено число.

```python
class OurIterator:
	def __init__(self, max_num):
		self.max_num = max_num
		
	def __iter__(self):
		self.cur_num = 0
		return self
		
	def __next__(self):
		number = self.cur_num
		self.cur_num += 1
		
		return number
```

В този пример `__next__()` връща запазва сегашното число в нова променлива, увеличава сегашното число и връща запазеното. С други думи - `__next__()` ще върне стойност, с 1 по-голяма от предходната или 0, ако се извиква за пръв път.


Накрая трябва да кажем кога това нещо ще спре. Трябва да проверим кога сме достигнали максималното число и да кажем на Python да спре да вика нашия `__next__()`.

```python
class OurIterator:
	def __init__(self, max_num):
		self.max_num = max_num
		
	def __iter__(self):
		self.cur_num = 0
		return self
		
	def __next__(self):
		number = self.cur_num
		
		if number == self.max_num:
			raise StopIteration # This is how you tell Python to stop calling __next__() in an iterator.
		
		self.cur_num += 1
		return number
```

Знаете как, когато имате грешка в кода и Python ви изхвърля някаква грешка. Тази грешка се нарича `Exception`. За `Exception`и ще говорим допълнително, но за момента ви стига да знаете, че когато ние кажем `raise StopIteration` в `__next__()`, Python ще разбере, че трябва да спре да извиква този метод. Все едно Python се е абонирал и чака да му кажем `StopIteration`. 

*Бележка: в тялото на `for` цикъла не е препоръчително да използвате `raise StopIteration` вместо `break`, както не можете в итератор да използвате `break` вместо `raise StopIteration`*

```python
for i in range(10):
	if i == 3:
		raise StopIteration
	print(i)
```
*Това ще спре цикъла, но ще ви изведе и грешка на изхода. Пробвайте :)))*


```python
class OurIterator:
	def __init__(self, max_num):
		self.max_num = max_num
		
	def __iter__(self):
		self.cur_num = 0
		return self
		
	def __next__(self):
		number = self.cur_num
		
		if number == self.max_num:
			raise StopIteration # This is how you tell Python to stop calling __next__() in an iterator.
		
		self.cur_num += 1
		return number
		
obj = OurIterator(10)
for i in obj:
	print(i)
```

Готови сме. Пробвайте!

Още код за пробване:

```python
class OurIterator:
	def __init__(self, max_num):
		self.max_num = max_num
		
	def __iter__(self):
		self.cur_num = 0
		return self
		
	def __next__(self):
		number = self.cur_num
		
		if number == self.max_num:
			raise StopIteration # This is how you tell Python to stop calling __next__() in an iterator.
		
		self.cur_num += 1
		return number
		
obj = OurIterator(3)
iterable = iter(obj)
print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))
```
___
Цялата последователност - for иска обектът да има `__iter__()` функцията, тази функция да връща обект, който има `__next__()` се нарича итератор протокол.

### Iterator Protocol ###
Това са обобщено изискванията, които класът на един обект трябва да спазва, за да може да бъде използван във `for`. 
```python
for a in obj:
	pass
```
Класът на `obj` трябва:
  1. Да има `__iter__()` метод
  1. `__iter__()` методът му да връща `iterable` обект
  1. `iterable` обектът е обект, който има `__next__()`

По-долу трябва да се показва схемата на итератор протокола:
(calls `__iter__()` internally, returns `iterable`)<br>
for: iter(obj) -> iterable; <br>
(calls `__next__()` internally, returns value)<br>
next(iterable) -> value; <br>
next(iterable) -> value; <br>
next(iterable) -> value<br>
...<br>

___
```python
class OurRange:
	def __init__(self, max_num):
		self.max_num = max_num
		
	def get_max(self):
		return self.max_num
		
class RangeIterator:
	def __init__(self, our_range):
		self.our_range = our_range
		
	def __iter__(self):
		self.cur_num = 0
		return self
		
	def __next__(self):
		num = self.cur_num
		
		if num == self.our_range.get_max():
			raise StopIteration
		
		self.cur_num += 1
		return num



```
