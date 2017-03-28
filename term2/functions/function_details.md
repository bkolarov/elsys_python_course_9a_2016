# Детайли за функциите

Всички вече сте запознати с функциите. Всички имате някакво определение за тях. Да кажем, че те са блок от код или съвкупност от последователни операции (една или повече или без да се случва нищо, ако просто сложим ключовата дума `pass`). Този блок от код е пакетиран на едно място и го използваме, чрез неговото име (името на функцията). Функцията може да има параметри или да не приема нищо. Стойността на параметрите (ако има такива) може да бъде използвана в тялото на функцията.

```python
def pow(number, power):
  result = number**power
  return result
```

Това е функция, на име `pow`, която **има** параметри, които са `number` и `power` и има тяло:
```python
  result = number**power
  return result
```

Целта на урока е да погледнем леко зад колисите на функциите, за да придобием по ясна представа за нещата. 

## def

Как дефинираме функция? Чрез ключовата дума `def`. `def` реално представлява изпълним код вътре в Python. Знаете, че всичко в Python е обект. Това прави и `def` - създава обект функция вътре в паметта. Когато интерпретаторът стигне до `def` в нашата програма, той взима тялото на функцията, опакова го в един обект в паметта и инициализира името на функцията да сочи към този обект.

Загубихте се? И аз бих.

Имаме тази функция:
```python
def pow(number, power):
  result = number**power
  return result
```

Python започва да интерпретира ред по ред. Първия ред, първата дума - това е `def`. Преди нея, нека паметта ни е това празно кръгче (mad paint skills!!! Даже не е пейнт, защото съм на Линукс :Д):

![Empty memory](https://github.com/bkolarov/elsys_python_course_9a_2016/blob/master/term2/functions/empty_memory.png?raw=true)


След като Python стигне `def`, обаче, се случва следното:
![Created function](https://github.com/bkolarov/elsys_python_course_9a_2016/blob/master/term2/functions/created_function_object.png?raw=true)


Създаден е обект функция, и сме казали, че ще имаме променлива `pow`, която ще сочи към този обект. Сетете се как всичко в Python е обект и без проблем можем да имаме:
```python
def do_something():
  pass
  
print (do_something) # output <function do_something at 0x7f74956d6f28>
do_something = 3
print (do_something) # output 3
```

Имаме функцията `do_something`, или по-точно имаме името `do_something`, което сочи към функция. После взимаме това име и му казваме, че вече сочи към цифрата 3.

Както ние казваме на имената към какво да сочат, така и `def` казва на името след него (в първоначалния пример `pow`) да сочи към обекта функция.


Именно защото `def` е изпълним код и се случва в реално време, по време на изпълнението на програмата, това е причината да можем да дефинираме функция почти навсякъде в кода. Дали ще срещнем `def` в някой `if` или в някой `for` цикъл, или пък в друга функция, това ще се изпълни, както всичко друго би се изпълнило на негово място. Ще се изпълни и ще създаде функция.

```python
def define_printer(number): # creates function and define_printer points to it
  if number <= 10:
    def printer_less(): # in this case we define function with body print('<= 10') and print_less points to it
      print('<= 10')
      
    # we create another name, printer, that points to the same object that printer_less points to.
    # in this case both printer and printer_less point to the function object
    printer = printer_less 
  else:
    def printer_greater(): # otherwise we define function with body print('> 10') and printer_greater points to it
      print('> 10')
    
    # we create another name, printer, that points to the same object that printer_greater points to.
    # in this case both printer and printer_greater point to the function object
    printer = printer_greater
    
  # Either we have the first case (number is <= 10) or the second one. In both of them we create the variable printer
  # and it points to a function, so we are sure that it exists and we can return it.
  return printer
```
