# super_cat
Программа, которая в качестве аргумента принимает имя файла (не указан файл или указан несуществующий — ошибка) и выводит его содержимое на экран.
В добавок, программа может принимать дополнительные агрументы:
«--count» для вывода кол-ва строк в конце сообщения,
«--num» для вывода порядкового номера с пробелом в начале каждой строки,
«--sort» для сортировки строк в алфавитном порядке перед выводом.
Пусть файл text1.txt содержит строки:

Houston
we have
a problem

Пример 1
Ввод	Вывод
python3 solution.py --num text1.txt
0 Houston
1 we have
2 a problem
Пример 2
Ввод	Вывод
python3 solution.py --count --sort text1.txt
Houston
a problem
we have
rows count: 3
Пример 3
Ввод	Вывод
python3 solution.py --count --sort textX.txt
ERROR
