## Resources
[Download cars.csv](https://my.pcloud.com/publink/show?code=XZ0LHIZIKHSjyxusXB5dGfM0o5S1pmICBeV)

*Бележка: Отворете файла `cars.csv` с текстов редактор (Notepad, Sublime, Gedit и пр) и проверете как са разделени колоните. Може да не е с `;`, а с някой друг символ.*

## Задачи
1. Отворете файла 'cars.csv' и принтирайте всички редове на екрана.
1. Изнесете кода от първа задача в отделна функция на име read_file, която приема за аргумент името на файла.
1. Направете функцията генератор, който yield-ва всеки ред от файла.
1. Използвайте генератора в цикъл, за да изкарате редовете на екрана.
1. В същия цикъл разделете реда, така че всяка колона да бъде елемент от list. Принтирайте всеки лист.
1. Изнесете цикъла, който разделя реда на елементи в лист, в генератор на име read_rows, който приема за аргумент името на файла. Генераторът yield–ва всеки нов лист от колони.
1. Направете нов цикъл, който итерира по read_rows. Принтирайте само този лист на екрана, чийто елемент за колона 'Origin' съдържа 'Europe'. <br>
*Подсказка: Отворете файла cars.csv в някой редактор. Първия ред на файла е с имената на колоните. Проверете, коя колона е с името Origin. Бройте от 0 :)*
1. Изнесете цикъла в нов генератор на име filter_lines_by_row, който приема име на файл и yield-ва всеки лист, отговарящ на условието.
1. Дефиинирате функцията file_row_filter. Нека тя да приема 1 аргумент, който ще е string. Тази функция да връща True ако 'Europe' се съдържа в подадения стринг, в противен случай False.
1. Променете filter_lines_by_row да приема два аргумента. Вторият аргумент ще е функция row_filter. Променете if-а в цикъла да използва подадената функция, като й подава съответния елемент.
1. Итерирайте по filter_lines_by_row като подадете дефинирата функция file_row_filter.
1. Променете извикването на filter_lines_by_row, като вместо да подавате file_row_filter, подавате lambda израз, който прави същото.

## Решения

### 1. Отворете файла 'cars.csv' и принтирайте всички редове на екрана.
```python
f = open('cars.csv', 'r')

for line in f:
	print (line)

f.close()
```

### 2. Изнесете кода от първа задача в отделна функция на име read_file, която приема за аргумент името на файла.
```python
def read_file(name):
	f = open('cars.csv', 'r')

	for line in f:
		print(line)

	f.close()
	
read_file('cars.csv')
```

### 3. Направете функцията генератор, който yield-ва всеки ред от файла.
```python
def read_file(name):
	f = open('cars.csv', 'r')

	for line in f:
		yield line # difference

	f.close()
```

### 4. Използвайте генератора в цикъл, за да изкарате редовете на екрана.
```python
for line in read_file('cars.csv'):
	print(line)
```

### 5. В същия цикъл разделете реда, така че всяка колона да бъде елемент от list. Принтирайте всеки лист.
```python
def read_file(name):
	f = open('cars.csv', 'r')

	for line in f:
		yield line

	f.close()

for line in read_file('cars.csv'):
	rows = line.split(';') # Check what symbol is used for row separator. It may not be ';' but something else.
	print(rows)
```

### 6. Изнесете цикъла, който разделя реда на елементи в лист, в генератор на име read_rows, който приема за аргумент името на файла. Генераторът yield–ва всеки нов лист от колони.
```python
def read_file(name):
	f = open('cars.csv', 'r')

	for line in f:
		yield line 

	f.close()

def read_rows(name):
	for line in read_file(name):
		rows = line.split(';')
		yield rows # difference

for rows in read_rows('cars.csv'):
	print (rows)
```

### 7. Направете нов цикъл, който итерира по read_rows. Принтирайте само този лист на екрана, чийто елемент за колона 'Origin' съдържа 'Europe'. <br>
*Подсказка: Отворете файла cars.csv в някой редактор. Първия ред на файла е с имената на колоните. Проверете, коя колона е с името Origin. Бройте от 0 :)* 
```python
def read_file(name):
	f = open('cars.csv', 'r')

	for line in f:
		yield line 

	f.close()

def read_rows(name):
	for line in read_file(name):
		rows = line.split(';')
		yield rows # difference

for rows in read_rows('cars.csv'):
	# The last element of the list is the last word/row in the csv file. This means that it may contain '\n' (new line character).
	# 'Europe' is not the same as 'Europe\n', but 'Europe' is in 'Europe\n'.
	if 'Europe' in rows[8]: 
		print (rows)
```

### 8. Изнесете цикъла в нов генератор на име filter_lines_by_row, който приема име на файл и yield-ва всеки лист, отговарящ на условието.
```python
def read_file(name):
	f = open('cars.csv', 'r')

	for line in f:
		yield line 

	f.close()

def read_rows(name):
	for line in read_file(name):
		rows = line.split(';')
		yield rows 

def filter_lines_by_row(name):
	for rows in read_rows(name):
		# The last element of the list is the last word/row in the csv file. This means that it may contain '\n' (new line character).
		# 'Europe' is not the same as 'Europe\n', but 'Europe' is in 'Europe\n'.
		if 'Europe' in rows[8]: 
			yield rows # difference

for rows in filter_lines_by_row('cars.csv'):
	print(rows)
```

### 9. Дефиинирате функцията file_row_filter. Нека тя да приема 1 аргумент, който ще е string. Тази функция да връща True ако 'Europe' се съдържа в подадения стринг, в противен случай False.
```python
def file_row_filter(row):
	if 'Europe' in row:
		return True
		
	return False
```

### 10. Променете filter_lines_by_row да приема два аргумента. Вторият аргумент ще е функция row_filter. Променете if-а в цикъла да използва подадената функция, като й подава съответния елемент.
```python
def read_file(name):
	f = open('cars.csv', 'r')

	for line in f:
		yield line 

	f.close()

def read_rows(name):
	for line in read_file(name):
		rows = line.split(';')
		yield rows 

def filter_lines_by_row(name, row_filter):
	for rows in read_rows(name):
		if row_filter(rows[8]): # difference
			yield rows 

def file_row_filter(row):
	if 'Europe' in row:
		return True
		
	return False
```

### 11. Итерирайте по filter_lines_by_row като подадете дефинирата функция file_row_filter.
```python
def read_file(name):
	f = open('cars.csv', 'r')

	for line in f:
		yield line 

	f.close()

def read_rows(name):
	for line in read_file(name):
		rows = line.split(';')
		yield rows 

def filter_lines_by_row(name, row_filter):
	for rows in read_rows(name):
		if row_filter(rows[8]): # difference
			yield rows 

def file_row_filter(row):
	if 'Europe' in row:
		return True
		
	return False

for rows in filter_lines_by_row('cars.csv', file_row_filter): # difference
	print(rows)
```

### 12. Променете извикването на filter_lines_by_row, като вместо да подавате file_row_filter, подавате lambda израз, който прави същото.
```python
def read_file(name):
	f = open('cars.csv', 'r')

	for line in f:
		yield line 

	f.close()

def read_rows(name):
	for line in read_file(name):
		rows = line.split(';')
		yield rows 

def filter_lines_by_row(name, row_filter):
	for rows in read_rows(name):
		if row_filter(rows[8]): # difference
			yield rows 

'''
# !!! WE DON'T NEED THAT ANYMORE !!!
def file_row_filter(row):
	if 'Europe' in row:
		return True
		
	return False
# !!! WE DON'T NEED THAT ANYMORE !!!
'''

for rows in filter_lines_by_row('cars.csv', lambda row: 'Europe' in row): # difference
	print(rows)
```
