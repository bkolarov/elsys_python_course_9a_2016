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

...всеки продукт ще има свои собствени атрибути: downloadQuality, vinylSize и shippingCost.
Преценяваме кой атрибут за кой продукт е. Добавяме атрибутите към съответните класове

```python
class CDProduct(Product):
  # Обърнете внимание, че подаваме на CDProduct всички необходими стойности за Product. Все пак CDProduct е вид продукт.
  # Разликата е там, че добавяме още един атрибут (shippingCost), за който също подаваме стойност.
  def __init__(self, artist, title, price, tracklist, shippingCost):
    # Извикваме __init__ метода на Product и му подаваме необходимите стойности.
    super().__init__(artist, title, price, tracklist)
    # Запазваме това, което е само за CDProduct в негов си атрибут.
    self.shippingCost = shippingCost

class VinylProduct(Product):
  # Същото като при CDProduct, но VinylSize има друг атрибут с друго име.
  def __init__(self, artist, title, price, tracklist, vinylSize):
    super().__init__(artist, title, price, tracklist)
    self.vinylSize = vinylSize
    
class DownloadProduct(Product):
  def __init__(self, artist, title, price, tracklist, downloadQuality):
    super().__init__(artist, title, price, tracklist)
    self.downloadQuality = downloadQuality
```
"Реализирайте йерархията от класове, така че да няма класове с еднакви атрибути." Направихме го. Всички продукти: CDProduct, VinylProduct и DownloadProduct наследяват атрибутите на Product, които са написани само веднъж точно в Product. Всеки един от трите продукта си има свой собствен атрибут, различен от на останалите.


"Предвид, че има различни видове продукти, значи че има и различни начини те да се купят. 
Освен класовете за продукти има класове, които продават всеки отделен вид продукт. Всеки "продавач" може да 
продава определен продукт "sell(item)", но всеки "продавач" го прави по различен начин."

```python
class Seller:
  def sell(self, item):
    pass
```

"Всеки "продавач" може да 
продава определен продукт "sell(item)", но всеки "продавач" го прави по различен начин."

```python
class CDSeller(Seller):
  def sell(self, item):
    print('Sending CD: {}'.format(item))
    
class VinylSeller(Seller):
  def sell(self, item):
    print('Sending Vinyl: {}'.format(item))
    
class DownloadSeller(Seller):
  def sell(self, item):
    print('Downloading: {}'.format(item))
```

"Дефинирайте изключение MethodNotImplementedError, което ще възникне, ако се извика "sell" и той не е имплементиран."
```python
class MethodNotImplementedError(Exception):
  def __init__(self):
    super().__init__('Method is not implemented!')
```

"... което ще възникне, ако се извика "sell" и той не е имплементиран"
```python
class Seller:
  def sell(self, item):
    raise MethodNotImplementedError
```
