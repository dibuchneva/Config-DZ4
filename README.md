##Задание 4

Вариант 2

Для ассемблера необходимо разработать читаемое представление команд УВМ. Ассемблер принимает на вход файл с текстом исходной программы, путь к которой задается из командной строки. Результатом работы ассемблера является бинарный файл в виде последовательности байт, путь к которому задается из командной строки. Дополнительный ключ командной строки задает путь к файлу-логу, в котором хранятся ассемблированные инструкции в духе списков “ключ=значение”, как в приведенных далее тестах.

Команды:
1. Запись константы: 

A --> Биты 0—4 --> 19 

B --> Биты 5—11 --> Адрес 

C --> Биты 12—28 --> Константа

Размер команды: 4 байт. Операнд: поле C. Результат: регистр по адресу,которым является поле B.

Тест (A=19, B=32, C=849):

0x13, 0x14, 0x35, 0x00

2. Чтение значения из памяти

A --> Биты 0—4 --> 28

B --> Биты 5—11 --> Адрес 

C --> Биты 12—18 --> Адрес

Размер команды: 4 байт. Операнд: значение в памяти по адресу, которым является регистр по адресу, которым является поле C. Результат: регистр по адресу, которым является поле B.

Тест (A=28, B=43, C=21):

0x7C, 0x55, 0x01, 0x00

3. Запись значения в память

A --> Биты 0—4 --> 7

B --> Биты 5—11 --> Адрес 

C --> Биты 12—18 --> Смещение 

D --> Биты 19—25 --> Адрес

Размер команды: 4 байт. Операнд: регистр по адресу, которым является поле D. Результат: значение в памяти по адресу, которым является сумма адреса (регистр по адресу, которым является поле B) и смещения (поле C).

Тест (A=7, B=9, C=83, D=20):

0x27, 0x31, 0xA5, 0x00

4. Бинарная операция: побитовый логический сдвиг вправо

A --> Биты 0—4 --> 30

B --> Биты 5—11 --> Адрес 

C --> Биты 12—18 --> Адрес 

D -->  Биты 19—25 --> Адрес 

Размер команды: 4 байт. Первый операнд: регистр по адресу, которым является поле D. Второй операнд: регистр по адресу, которым является поле C. Результат: значение в памяти по адресу, которым является регистр по адресу, которым является поле B.

Тест (A=30, B=103, C=16, D=104):

0xFE, 0x0C, 0x41, 0x03

Форматом для файла-лога является csv