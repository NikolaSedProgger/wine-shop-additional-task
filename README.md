# Генерируем расписание обхода охранников

Данная программа генерирует расписание для обходов охранников к разным объектам.

### Как пользоваться скриптом?

Python3 должен быть уже установлен.

Затем используйте pip (или pip3, есть конфликт с Python2) для установки необходимых библиотек:
```bash
pip install -r requirements.txt
```

Запускаем ```main.py```
```bash
python main.py
```

И на выходе получаем сгенерированый файл расписания ```ВчерашняяДата-СегодняшняяДата.docx```

### Как добавить новые объекты?

Чтобы добавить объект/объекты заходим ```objects.txt```
После чего вводим новые обекты на НОВОЙ строчке

Пример:
```text
ГСМ
Стоянка
Ангар
...
```
### Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).