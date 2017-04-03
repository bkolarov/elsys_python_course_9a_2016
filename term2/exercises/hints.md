
```python 
def compare_numbers(num1, num2):
  return num1 == num2

result = compare_numbers(11, 343)

# SAME AS
compare_numbers = lambda num1, num2: num1 == num2

result = compare_numbers(11, 343)
```

```python

def make_list(num1, num2):
  return [num1,num2]
  
result = make_list(1, 2)

# SAME AS

make_list = lambda num1, num2: [num1, num2]

result = make_list(1, 2)
```
