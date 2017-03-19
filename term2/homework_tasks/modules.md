Създайте структура от пакети и модули за чат приложение. Главният пакет се казва messenger. В него има модул на име `main`. Освен модула, вътре има два други пакета - `ui` и `networking`. 
* `ui` - съдържа два модула:
	- `main_controller`
	- `layout_loader` - Този модул не трябва да може да може да бъде добавен с `from ui import *`.
	
* `networking` - съдържа три модула - `client`, `connector` и `config`. `connector` и `config` не трябва да могат да бъдат добавени с `from networking import *`.


Фукнционалността, ще бъде почти никаква. Модулите трябва само да имат някаква инициализация и някоя друга дефинирана функция.

1. messenger: 
    - `main` - Извиква дефинираната в `main_controller` функция `start()`
1. ui:
    - `main_controller` - добавя в себе си `layout_loader` и `client`. Трябва да има дефинирана в себе си функцията `start()`, която принтира на екрана `'starting app'`. 
	Накрая дефинирате трета функция `on_message_received(message)`. Тя принтира на екрана подаденото съобщение по следния начин: `'main_controller - on_message_received: ' + message`. 
	В `start()` извивкате функциите `send_message(message)` и `register_message_received(callback)`, дефинирани в client. На `send_message()` подавате `'outgoing message'`, а на `register_message_received()` - `on_message_received`.
	
1. networking
    - `config` - Държи две променливи - `ip_address`, `port`. При `import` на този модул, `ip_address` се инициализира с `'123.34.22.19'`, а `port` с `'992'`.
    - `connector` - добавя в себе си `config`. Има в себе си няколко функции:
        * `connect()` - извиква се при инициализация на модула. Вътре в нея се изкарват на екрана ip–то и порта от `config` модула. Двете се разделят с `':'`. Т.е. в нашия случай трябва да изкара `'123.34.22.19:992'`.
	    * `get_input()` - принтира на екрана `'acquiring network input'`
	    * `get_output()` - принтира на екрана `'acquiring network output'`
    - `client` - добавя в себе си `connector`. Дефинира две функции:
        * `send_message(message)` - приема стринг за аргумент и го принтира на екрана по следния начин: `'sending message: ' + message`
        * `register_message_received(callback)` - приема като аргумент друга функция (спомнете си, че функциите също са обекти). Вътре в `register_message_received(callback)` извиквате `callback` и подавате следния стринг: `'on message received'`
