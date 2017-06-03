## Структури от данни
Структурите от данни са начинът, по който тези данни са организирани, така че операциите върху тези данни да са лесни, бързи и ефикасни. Досега сте се запознали с поне два вида структури от данни - `list` и `dictionary`. В `list` данните са подредени последователно и се достъпват чрез съотетния индекс. В `dictionary` данните се достъпват чрез ключ. Всеки запис може да си го представите като Key-Value двойка. Достъпвате определена стойност чрез нейния ключ. 

Тук ще се разгледа и имплементира друг вид стуктура от данни - свързан списък.

## Свързан списък (Linked list)
Преди да ви въведа в свързания списък ще направя бързо припомняне за обикновения `list` в Python. 
```python
l = [1, 2, 3, 4]
print(l[0])
print(l[1])
print(l[3])
```
```
Output: 
1
2
4
```
Нищо сложно не се случва тук. Това е пример как сме запазили последователно 4 цифри и как ги достъпваме.

### Свързан списък (this time for real)
В един свързан списък данните се съхраняват във т. нар. възли (nodes). Всеки възел държи стойност и обект към възела, който е след него.

<img src="./resources/first_node.png">

Тази готина картинка изобразява един възел. Вътре в себе си държи стойност (в случая тя е 1 - първата стойност от list-а по-горе) и следващия обект в списъка. В момента нямаме втори възел, затова `next` сочи към `None`.

Да добавим още една цифра.

<img src="./resources/two_nodes.png">

Първият елемент е със стойност `1`. След като вече имаме и втори елемент, `next` на първия обект сочи към втория `Node` със стойност `2`. Трети елемент нямаме, затова на втория възел `next` сочи към `None`. Мисля че схващате идеята. Познайте как ще изглежда картинката, ако добавим трети и четвърти възел.

<img src="./resources/all_nodes.jpg">

### Имплементация
Как ще имплементираме това нещо в Python? Всеки възел може да бъде описан с клас. Всеки клас ще държи два обекта - стойност и `next`. 
```python
class Node:
	  def __init__(self, value):
		self.value = value
		self.next = None
```
Всеки път, когато трябва да създадем възел, ще създаваме обект от клас Node. Всеки нов възел първоначално няма следващ такъв, но трябва все пак да има в себе си обект `next`. Затова създаваме и инициализираме 
`self.next = None`. 

Да създадем списъка на картинката:
```python
class Node:
	  def __init__(self, value):
		self.value = value
		self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
```

В момента има създадени възли, но все още нямат връзка помежду си. Правим и нея.

```python
n1.next = n2
n2.next = n3
n3.next = n4
```

Готово. Да го пробваме! Дефинираме функция, която ще приема първия възел от един свързан списък. Имайки него, тя трябва да изкара на екрана всички стойности от списъка.

```python
def print_list(first_node):
	current_node = first_node
	while current_node != None:
		print(current_node.value)
		current_node = current_node.next
```

Какво прави функцията?
1. `current_node = first_node` - Минаваме през всеки един възел от списъка. Всеки един възел достъпваме, чрез името `current_node`. Започваме от първия възел, затова казваме, че `current_node` ще сочи към същия обект, към който сочи и `first_node`. 
1. `current_node = current_node.next` - След като сме приключили със сегашния възел, преминаваме на следващия. Всеки възел държи връзка към следващия. Съответно казваме, че `current_node` ще сочи към `current_node.next`. Така с `current_node` вече достъпваме следващия елемент.
1. `while current_node != None:` - Последният възел няма следващ, затова неговият `next` сочи към None. След като на всяка итерация `current_node` сочи към следващия възел, той в един момент ще стигне последния. Когато приключи и с последния, `current_node = current_node.next` ще се изпълни, където `current_node.next` сочи към None, следователно `current_node` ще сочи към None и цикълът ще приключи.

<img src="./resources/iterate_nodes.png">

___
При имплементация на свързан списък пазим само първия възел. Конвенцията е да го достъпваме чрез име `head`. Да дефинираме функция, която добавя нов възел в края на списъка. Нека функцията приема `head` и само стойността, която ще се държи, а самия `Node` да го създава тя.

<img src="./resources/linked_list.png">

```python
def add(head, value):
	new_node = Node(value)
	current_node = head
	
	while current_node.next != None:
		current_node = current_node.next
	
	current_node.next = new_node
```

Какво прави функцията?
1. `def add(head, value)` - Приема само първия възел от списъка и стойността, която ще се държи във възел, който ще закачим накрая.
1. `new_node = Node(value)` - След като функцията приема стойността на новия възел, а не самия възел, тогава създаваме новия възел ние. По-късно ще разберете, защо го правим по този начин.
1. `current_node = head` - Трябва да минем през всички възли в списъка (както направихме във функцията `print_list`). Разбира се ще започнем от първия.
1. Цикъла
	```python
	while current_node.next != None:
			current_node = current_node.next
	```
	За разлика от функцията `print_list`, тук не итерираме докато `current_node` не сочи към `None`, а докато `current_node.next` не сочи към `None`. Схващате ли разликата? Искаме да стигнем до последния възел, а не до един след него. Последният възел е този, чийто `next` сочи към `None` (вижте картинките). В момента, в който `current_node.next` сочи към `None`, значи `current_node` е последния възел.
1. `current_node.next = new_node` - След като цикълът приключи, `current_node` ще сочи към текущия последен възел. Към него закачаме новия възел.

Да пробваме как работи.
```python
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

def print_list(head):
	current_node = head
	while current_node != None:
		print(current_node.value)
		current_node = current_node.next

def add(head, value):
	new_node = Node(value)
	current_node = head
	
	while current_node.next != None:
		current_node = current_node.next
	
	current_node.next = new_node

head = Node(1)

add(head, 5)
add(head, 'Multicet')

print_list(head)
```
```
Output:
1
5
Multicet
```

## Клас LinkedList
С цел удобство, четимост на кода, модуларност, капсулиране и тн., ще създадем клас `LinkedList`. Операциите ще се извършват вътре в класа. Класът ще се грижи за тях. Освен това този клас ще може да държи информация за самия списък. Примерно неговия размер. Така всеки път като създаваме списък, ще имаме дължината на всеки списък поотделно.

```python
class LinkedList:

	def __init__(self):
		self.head = None
		self.size = 0

	class Node:
		def __init__(self, value):
			self.value = value
			self.next = None

	def add(self, value):
		new_node = LinkedList.Node(value)
		current_node = self.head
	
		while current_node.next != None:
			current_node = current_node.next
	
		current_node.next = new_node
		self.size += 1

ll = LinkedList()

ll.add(1)
```

Държим `head` локално за обектите `LinkedList`, следователно го достъпваме посредством `self`. Казахме, че ще пазим размера на всеки свързан списък. За целта при инициализиране на нов обект `LinkedList`, създаваме променлива `size` и я инициализираме с 0 (първоначално списъкът е празен) - `self.size = 0`. Увеличаваме тази променлива накрая на метода `add`, т.е. всеки път като добавим нов елемент. 

Какво е първото нещо, което забелязваме щом изпълним този код? Че той не работи.

```
Output:
Traceback (most recent call last):
  File "list_ex.py", line 24, in <module>
    ll.add(1)
  File "list_ex.py", line 16, in add
    while current_node.next != None:
AttributeError: 'NoneType' object has no attribute 'next'
```

Има един съществен проблем. Кога е празен списъкът? Когато `self.head = None`.

Какво се случва? В `add` използваме `self.head`. `self.head`, обаче, е `None` в началото (още не сме добавили нищо). `current_node` сочи там, където и `self.head`, т.е. също към `None`. В цикъла се опитваме на `current_node`, който сочи към `None`, да достъпим атрибут с име `next`. Това е все едно да напишем <br>`None.next != None`. Не работи.

Просто решение - преди цикъла във функцията `add`, ще проверим дали списъкът не е празен. Ако е празен, казваме на `self.head` да сочи към новия елемент и приключваме. В случай, че ще ни трябва и в бъдеще, ще дефинираме функция, която казва дали списъкът е празен и ли не. Тя ще изглежда така:

```python
	def is_empty(self):
		return self.head == None
```

Промяната на `add` е следната:
```python
	def add(self, value):
		new_node = LinkedList.Node(value)
		current_node = self.head

		if self.is_empty(): # Notice the difference
			self.head = new_node
		else:
			while current_node.next != None:
				current_node = current_node.next

			current_node.next = new_node
			
		self.size += 1
```

Целия клас досега:
```python
class LinkedList:

	def __init__(self):
		self.head = None
		self.size = 0

	class Node:
		def __init__(self, value):
			self.value = value
			self.next = None

	def add(self, value):
		new_node = LinkedList.Node(value)
		current_node = self.head

		if self.is_empty():
			self.head = new_node
		else:
			while current_node.next != None:
				current_node = current_node.next

			current_node.next = new_node
			
		self.size += 1

	def is_empty(self):
		return self.head == None
```
```python
ll = LinkedList()

ll.add(1)
```
Не гърми.<br>
Липсва една функция, която написахме по-рано. Функцията за изкарване на списъка на екрана. Тя какво трябва да прави? Да итерира по целия списък и да изкара стойността на всеки възел. Итериране. И..террр...атор.

### Итератор
В случай, че сте забравили, може да погледнете [урока за итератори](https://github.com/bkolarov/elsys_python_course_9a_2016/blob/master/term2/iterators_generators/iterators_generators.md).
За да можем да итерираме по списъка, трябва класът `LinkedList` да спазва итератор протокола. Какъв беше той? - Да имплементира функцията `__iter__`, която да връща обект, чийто клас има функцията `__next__`. 

Ще дефинираме вътрешен за `LinkedList` клас на име `Iterator`. Негова инстанция ще се връща от метода `__iter__`. Този клас ще иска да има `head`-а на списъка. Все пак трябва да започне от първия елемент. При всяко извикване на `__next__`, този метод ще връща стойността от следващия във списъка възел.

### LinkedList.Iterator
```python
class Iterator:
		def __init__(self, head):
			self.current_node = head

		def __next__(self):
			if self.current_node == None:
				raise StopIteration
				
			current_value = self.current_node.value
			self.current_node = self.current_node.next
			
			return current_value
```

1. Итераторът трябва да започва от първия възел - `head`. 
	```python
			def __init__(self, head):
				self.current_node = head
	```
1. Списъкът е празен, ако `head` сочи към `None`. Тогава и `current_node` ще е `None`. Отделно ще сме минали всички възли от списъка, когато `current_node` стане `None` (вижте картинките по-горе). И в двата случая `self.current_node` ще е `None`, затпва трябва да кажем, че приключваме с итерирането.
	```python
			def __next__(self):
				if self.current_node == None:
					raise StopIteration
				...
	```
1. Преди да преместим `current_node` да сочи към следващия възел, трябва да запазим стойността на сегашния възел, за да може `__next__` да я върне - `current_value = self.current_node.value`
1. Преместваме `current_node` към следващия възел и връщаме запазената стойност:
	```python
	...
	self.current_node = self.current_node.next
	
	return current_value
	```
	
Целият клас `LinkedList` към момента:
```python
class LinkedList:

	def __init__(self):
		self.head = None
		self.size = 0

	class Node:
		def __init__(self, value):
			self.value = value
			self.next = None

	def add(self, value):
		new_node = LinkedList.Node(value)
		current_node = self.head

		if self.is_empty():
			self.head = new_node
		else:
			while current_node.next != None:
				current_node = current_node.next
	
			current_node.next = new_node
			
		self.size += 1

	def __iter__(self): # new method
		return LinkedList.Iterator(self.head)

	class Iterator: # new inner class
		def __init__(self, head):
			self.current_node = head

		def __next__(self):
			if self.current_node == None:
				raise StopIteration
				
			current_value = self.current_node.value
			self.current_node = self.current_node.next
			
			return current_value

	def is_empty(self):
		return self.head == None
```

Сега можем да си дефинираме отново функцията `print_list`, която този път ще приема обект `LinkedList` и ще й е много по-лесно да премине и да изкара стойностите от списъка на екрана.
```python
def print_list(linked_list):
	for value in linked_list:
		print(value)
```

```python
cars = LinkedList()
names = LinkedList()

cars.add('BMW')
cars.add('VW')
cars.add('Mazda')
cars.add('Ford')

names.add('Stamat')
names.add('Multicet')
names.add('Spas')
names.add('Mariika')
names.add('Scott Pilgrim')

print_list(cars)
print()
print_list(names)
```
```
Output:
BMW
VW
Mazda
Ford

Stamat
Multicet
Spas
Mariika
Scott Pilgrim
```

Обърнете внимание на добавянето на стойности. Просто казваме `names.add('Multicet')`. Знаем, че класът сам се оправя да създаде новия възел. **В противен случай** трябваше ние да пишем `names.add(LinkedList.Node('Multicet'))`. Спестихме си малко писане на код.

### len()
Досега пазихме размера на списъка и го увеличавахме всеки път, когато добавим нов възел. За нищо не го използваме, обаче. 

Как се взима размера на един `list` в Python? 
```python
l = [1, 2, 3]
print(len(l))
```
```
Output:
3
```

Щеше да е яко, ако можехме да направим същото и при нас. Примерно `print(len(linked_list))`. Всъщност ще е доста просто да се направи.
`len()` е една от вградените в Python функции, която извиква функцията `__len__` на подадения й обект. Имплементираме една такава в LinkedList и сме готови.
```python
def __len__(self):
	return self.size
```

Целия клас до момента:
```python
class LinkedList:

	def __init__(self):
		self.head = None
		self.size = 0

	class Node:
		def __init__(self, value):
			self.value = value
			self.next = None

	def add(self, value):
		new_node = LinkedList.Node(value)
		current_node = self.head

		if self.is_empty():
			self.head = new_node
		else:
			while current_node.next != None:
				current_node = current_node.next
	
			current_node.next = new_node
			
		self.size += 1

	def __iter__(self):
		return LinkedList.Iterator(self.head)

	class Iterator:
		def __init__(self, head):
			self.current_node = head

		def __next__(self):
			if self.current_node == None:
				raise StopIteration
				
			current_value = self.current_node.value
			self.current_node = self.current_node.next
			
			return current_value

	def is_empty(self):
		return self.head == None

	
	def __len__(self): # new method
		return self.size
```
```python
cars = LinkedList()
names = LinkedList()

cars.add('BMW')
cars.add('VW')
cars.add('Mazda')
cars.add('Ford')

print('cars size: {}'.format(len(cars)))

names.add('Stamat')
names.add('Multicet')
names.add('Spas')
names.add('Mariika')
names.add('Scott Pilgrim')

print('names size: {}'.format(len(names)))
```

```
Output:
cars size: 4
names size: 5
```

### Премахване на възел
За да премахнем един възел, трябва просто да премахнем връзката към него. След като няма връзка към обекта, той ще бъде унищожен. Казано с думи - на възела, чийто `next` сочи към този, който искаме да изтрием, казваме, че следващият му възел е следващия на този, който искаме да изтрием. Ако имаме списък A -> B -> C (А сочи към В, който сочи към С) и искаме да изтрием B. Казваме просто A -> C (А да сочи към С).

<img src="./resources/delete_node.png">

В случай, че този възел, който искаме да изтрием, е първият (т.е. `head`), просто преместваме `head` да сочи към следващия. 

<img src="./resources/delete_head.png">

Дефинираме функция `delete` в LinkedList. Тя ще приема стойност. Трябва да изтрие първия възел в списъка, който държи същата стойност. Може да се направи и така, че да изтрие всички възли със същата стойност, но разликата няма да е голяма. Придържаме се към първия вариант.

За да дефинираме функицята, трябва да съобразим две неща:
	- Списъкът може да е празен - ако е празен, не трябва да правим нищо
	- Нямаме достъп до предходния възел. - Ако имаме списък A -> B -> C и искаме да изтрием B. Ще итерираме по списъка, докато не стигнем този, който трябва да изтрием (в случая B). Проблемът е, че когато `current_node` е този, който трябва да изтрием, няма как да кажем на предишния да сочи към следващия. Или ако минаваме през всичките възли (A, B и C), и `current_node` е стигнал B, няма как да кажем на A да сочи към C.

<img src="./resources/delete_fail.png">

За да се справим с проблема, просто когато итерираме ще проверяваме дали **следващият** възел не е този, който трябва да изтрием. Така ще кажем на сегашния да сочи към по-следващия, вместо следващия. 

<img src="./resources/delete_fail_fix.png">

При това решение на проблема трябва да съобразим само още едно нещо:
	- Започваме от първия възел. Винаги започваме при `current_node = head`. Това значи, че нямаме предишен възел, чийто следващ да проверим дали трябва да изтрием. Затова ще опишем това в отделен случай, ако този елемент, който трябва да се изтрие, не е първият.

```python
def delete(self, value):
		if self.is_empty():
			return
		
		current_node = self.head
		
		if self.head.value == value: # the first node is the one to delete
			self.head = self.head.next
		else:
			while current_node.next != None:
				if current_node.next.value == value:
					to_delete_node = current_node.next
					current_node.next = to_delete_node.next
					break
					
				current_node = current_node.next
				
		self.size -= 1
```
Целия клас досега:
```python
class LinkedList:

	def __init__(self):
		self.head = None
		self.size = 0

	class Node:
		def __init__(self, value):
			self.value = value
			self.next = None

	def add(self, value):
		new_node = LinkedList.Node(value)
		current_node = self.head

		if self.is_empty():
			self.head = new_node
		else:
			while current_node.next != None:
				current_node = current_node.next
	
			current_node.next = new_node
			
		self.size += 1

	def delete(self, value):
		if self.is_empty():
			return
			
		current_node = self.head
	
		if self.head.value == value:
			self.head = self.head.next
		else:
			while current_node.next != None:
				if current_node.next.value == value:
					to_delete_node = current_node.next
					current_node.next = to_delete_node.next
					break
					
				current_node = current_node.next
				
		self.size -= 1

	def __iter__(self):
		return LinkedList.Iterator(self.head)

	class Iterator:
		def __init__(self, head):
			self.current_node = head

		def __next__(self):
			if self.current_node == None:
				raise StopIteration
				
			current_value = self.current_node.value
			self.current_node = self.current_node.next
			
			return current_value

	def is_empty(self):
		return self.head == None

	
	def __len__(self):
		return self.size
```

```python
def print_list(linked_list):
	for value in linked_list:
		print(value)

def print_info(msg, cars):
	print(msg)
	print('cars size: {}'.format(len(cars)))
	print_list(cars)
	print()
	

cars = LinkedList()

cars.add('BMW')
cars.add('VW')
cars.add('Mazda')
cars.add('Ford')

print_info('before deletion', cars)

cars.delete('BMW')
print_info('after deletion', cars)

cars.delete('Mazda')
print_info('after another deletion', cars)

cars.delete('Ford')
print_info('final deletion', cars)
```

```
Output:
before deletion
cars size: 4
BMW
VW
Mazda
Ford

after deletion
cars size: 3
VW
Mazda
Ford

after another deletion
cars size: 2
VW
Ford

final deletion
cars size: 1
VW

```

### Вмъкване на възел
Вмъкването на възел ще е доста подобно на триенето на такъв. Отново ще работим с `current_node` и отново ще проверяваме следващия му възел. Функцията за вмъкване ще трябва да добави нов възел на мястото на друг. На мястото на кой възел ще вмъква, ще зависи от подадена стойност. Например ако имаме списък 1 -> 2 -> 4 -> 5, ще искаме да вмъкнем нов възел със стойност 3 на мястото на 4. Така ще се получи 1 -> 2 -> 3 -> 4 -> 5.

Съобразяваме същите неща като при триенето:
	- Списъкът може да е празен.
	- Нямаме достъп до предходния възел, ако проверяваме дали да вмъкнем на мястото на `current_node`, а не на `current_node.next`.
	- Може да вмъкваме на мястото на първия възел.

<img src="./resources/insert_node.png">

```python
class InvalidInsertionError(Exception):
	def __init__(self):
		super().__init__("Attempring to insert into an empty list or into one, that doesn't have a node with the given before_value")
		
	def insert(self, before_value, new_value):
		new_node = LinkedList.Node(new_value)
		insert_succeeded = False
	
		if self.is_empty():
			insert_succeeded = False
		elif self.head.value == before_value:
			tmp = self.head
			new_node.next = tmp
			self.head = new_node
			insert_succeeded = True
		else:
			current_node = self.head
			while current_node.next != None:
				if current_node.next.value == before_value:
					new_node.next = current_node.next
					current_node.next = new_node
					insert_succeeded = True
					break
				
				current_node = current_node.next
		
		if insert_succeeded:
			self.size += 1
		else:
			raise InvalidInsertionError
```

Какво прави функцията?
1. `insert_succeeded = False` - Има два случая, в които вмъкването може да се провали - ако списъкът е празен или ако няма такъв възел, на чието място да вмъкнем (няма възел със стойност равна на `before_value`). Приемаме, че първоначално `insert_succeeded` е `False`, защото е по-лесно да му дадем стойност `True`, когато успеем да вмъкнем. В противен случай в `else` блока трябва да проверяваме дали цикълът е свършил без да вмъкваме каквото и да било и да зададем стойност `False`. Това е в случай, че сме създали `insert_succeeded` инициализирано с `True`, а не с `False`. Написано по сегашния начин си спестяваме някой друг `if`.
1. Вмъкване в празен списък
	```python
		if self.is_empty():
			insert_succeeded = False
	```
		Не можем да търсим да вмъкнем на място на някой възел, като нямаме никакви възли. Вмъкването не е успешно.
1. Вмъкване на мястото на `head`
	```python
		elif self.head.value == before_value:
			tmp = self.head
			new_node.next = tmp
			self.head = new_node
			insert_succeeded = True
	```
	В случай, че мястото, на което вмъкваме, е първия възел - запазваме кой е първия възел (`tmp = self.head`), казваме, че сегашният първи възел вече ще е следващия на новия първи възел (`new_node.next = tmp`) и накрая казваме, че новият възел е първи (`self.head = new_node`). Вмъкването е успешно.
1. Вмъкване навътре в списъка:
	```python
		current_node = self.head
			while current_node.next != None:
				if current_node.next.value == before_value:
					new_node.next = current_node.next
					current_node.next = new_node
					insert_succeeded = True
					break
				
				current_node = current_node.next
	```
	Минаваме през всички възли и на всеки текущ възел (`current_node`) проверяваме дали не трябва да вмъкнем на мястото на следващия (`current_node.next`). 
	- Ако условието (`if current_node.next.value == before_value:`) е вярно, значи вмъкваме на мястото на следващия елемент. 		
		* Казваме, че на новия възел следващият е следващия на сегашния възел:
			```python
				new_node.next = current_node.next
			```
		* Казваме на текущия възел, че следващият му е новия възел:
			```python
				current_node.next = new_node
			```
		* Вмъкването е успешно и прекратяваме цикъла
	- Ако условието е грешно преместваме `current_node` да сочи към следващия възел. 
	След като мине цикъла, щом сме влезли в този блок, значи нищо от предните условия не се е изпълнило. Ако на нито една итерация не е влязло във вътрешния за цикъла `if`, `insert_succeeded` няма да бъде равно на `True`. 
1. Края на функцията
	```python
	if insert_succeeded:
		self.size += 1
	else:
		raise InvalidInsertionError
	```
- В случай, че вмъкването е успешно трябва да увеличим размера на списъка с 1.
	
- Ако нещо сме прецакали - дефинирали сме си изключението `InvalidInsertionError` и го създаваме, за да кажем, че нещо не е наред.

LinkedList и InvalidInsertionError
```python
class InvalidInsertionError(Exception):
	def __init__(self):
		super().__init__("Attempring to insert into an empty list or into one, that doesn't have a node with the given before_value")
		
class LinkedList:

	def __init__(self):
		self.head = None
		self.size = 0

	class Node:
		def __init__(self, value):
			self.value = value
			self.next = None

	def add(self, value):
		new_node = LinkedList.Node(value)
		current_node = self.head

		if self.is_empty():
			self.head = new_node
		else:
			while current_node.next != None:
				current_node = current_node.next
	
			current_node.next = new_node
			
		self.size += 1

	def delete(self, value):
		if self.is_empty():
			return
			
		current_node = self.head
	
		if self.head.value == value:
			self.head = self.head.next
		else:
			while current_node.next != None:
				if current_node.next.value == value:
					to_delete_node = current_node.next
					current_node.next = to_delete_node.next
					break
					
				current_node = current_node.next
				
		self.size -= 1

	def insert(self, before_value, new_value):
		new_node = LinkedList.Node(new_value)
		insert_succeeded = False
	
		if self.is_empty():
			insert_succeeded = False
		elif self.head.value == before_value:
			tmp = self.head
			new_node.next = tmp
			self.head = new_node
			insert_succeeded = True
		else:
			current_node = self.head
			while current_node.next != None:
				if current_node.next.value == before_value:
					new_node.next = current_node.next
					current_node.next = new_node
					insert_succeeded = True
					break
				
				current_node = current_node.next
		
		if insert_succeeded:
			self.size += 1
		else:
			raise InvalidInsertionError

	def __iter__(self):
		return LinkedList.Iterator(self.head)

	class Iterator:
		def __init__(self, head):
			self.current_node = head

		def __next__(self):
			if self.current_node == None:
				raise StopIteration
				
			current_value = self.current_node.value
			self.current_node = self.current_node.next
			
			return current_value

	def is_empty(self):
		return self.head == None

	
	def __len__(self):
		return self.size
```
```python
def print_list(linked_list):
	for value in linked_list:
		print(value)

def print_info(msg, linked_list):
	print(msg)
	print('size: {}'.format(len(linked_list)))
	print_list(linked_list)
	print()	

numbers = LinkedList()

for i in range(5):
	numbers.add(i)
	

print_info('before insertion', numbers)

numbers.insert(3, 2.5)
print_info('after insertion', numbers)

numbers.insert(0, -1)
print_info('after second insertion', numbers)


numbers.insert(4, 3.5)
print_info('after third insertion', numbers)

print('invalid insertion')
numbers.insert(5, 4)
```

```
Output:
before insertion
size: 5
0
1
2
3
4

after insertion
size: 6
0
1
2
2.5
3
4

after second insertion
size: 7
-1
0
1
2
2.5
3
4

after third insertion
size: 8
-1
0
1
2
2.5
3
3.5
4

invalid insertion
Traceback (most recent call last):
  File "list_ex.py", line 129, in <module>
    numbers.insert(5, 4)
  File "list_ex.py", line 74, in insert
    raise InvalidInsertionError
__main__.InvalidInsertionError: Attempring to insert into an empty list or into one, that doesn't have a node with the given before_value
```

Линк към целия код: https://github.com/bkolarov/elsys_python_course_9a_2016/blob/master/term2/linked_list/linked_list.py
___
### Sorry of the long post. Here is a cool potato
![](https://i.imgur.com/HF9FmkL.jpg)
