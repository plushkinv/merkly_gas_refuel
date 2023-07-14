# Автор
PLushkin https://t.me/plushkin_blog        

**На чай с плюшками автору:**
Полигон, БСК, Арбитрум - любые токены - `0x79a266c66cf9e71Af1108728e455E0B1D311e95E`
Трон TRC-20 только USDT, остальное не доходит - `TEZG4iSmr31wWnvBixKgUN9Aax4bbgu1s3`

# Чё делает
позволяет переводить нативные токены из одной сети в другую с автоматической конвертацией
через merkly gas refuel .   все транзакции попадают L0

1. ДОбавьте ваши приватники в файл private_keys.txt
2. в файле main.py  в самом начале выберите сеть назначения и сеть откуда переводите. а так же укажите сколько хотите поулчить нативного токена в сети назначения 
3. и запускайте. 

# Установка и запуск: Linux/Mac

Linux/Mac
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python main.py
```
Windows - https://www.youtube.com/watch?v=EqC42mnbByc
```
pip install virtualenv
virtualenv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python main.py
```


