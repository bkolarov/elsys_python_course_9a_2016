## Задача: 
  
Помислете как онлайн продавач ще организира базата си от данни за музикални продукти за продан.
Да кажем, че има 3 вида продукти: CD, Vinyl и Download. Всички те ще имат общи атрибути като:
artist, title, price и tracklist, но и всеки продукт ще има свои собствени атрибути: downloadQuality, vinylSize и shippingCost.
Реализирайте йерархията от класове, така че да няма класове с еднакви атрибути.
Предвид, че има различни видове продукти, значи че има и различни начини те да се купят. 
Освен класовете за продукти има класове, които продават всеки отделен вид продукт. Всеки "продавач" може да 
продава определен продукт "sell(item)", но всеки "продавач" го прави по различен начин. 
Дефинирайте изключение MethodNotImplementedError, което ще възникне, ако се извика "sell" и той не е имплементиран.


Да кажем, че има 3 вида продукти: CD, Vinyl и Download. Всички те ще имат общи атрибути...
Значи има три различни вида продукт, с общи характеристики - три различни класа, които наследяват един общ.


Всички те ще имат общи атрибути като: artist, title, price и tracklist
```python
class Product:
  def __init__(self, artist, title, price, tracklist):
      self.artist = artist
      self.title = title
      self.price = price
      self.tracklist = tracklist
      
class CDProduct(Product):
  pass

class VinylProduct(Product):
  pass

class DownloadProduct(Product):
  pass
```

#...всеки продукт ще има свои собствени атрибути: downloadQuality, vinylSize и shippingCost.
# Преценяваме кой атрибут за кой продукт е. Добавяме атрибутите към съответните класове

```python
class CDProduct(Product):
  pass

class VinylProduct(Product):
  pass

class DownloadProduct(Product):
  pass
```
