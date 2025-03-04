"""Пример решения сложной задачи на словари
Рассмотрим такую задачу: словарь задан в виде набора строк, в каждой строке записано слово на английском языке, затем следует символ -, затем, через запятую, перечислены возможные переводы слова на латынь. 

Требуется составить латино-английский словарь и вывести его в том же виде. Все слова должны быть упорядочены по алфавиту. Возможные переводы одного слова должны быть также упорядочены по алфавиту.

Например, для ввода:

apple - malum, pomum, popula
fruit - baca, bacca, popum
punishment - malum, multa

Вывод должен выглядеть так:

baca - fruit
bacca - fruit
malum - apple, punishment
multa - punishment
pomum - apple
popula - apple
popum - fruit

Идея решения заключается в следующем: разрежем каждую строку на английское и латинские слова. Каждое из латинских слов возьмем в качестве ключа и добавим к его значениям английское слово (переводов может быть несколько). Затем пройдем по сортированным ключам и для каждого ключа выведем отсортированный список переводов:
"""
n = int(input())
latinEnglish = {}
for i in range(n):
    line = input()
    english = line[:line.find('-')].strip()
    latinsStr = line[line.find('-') + 1:].strip()
    latins = map(lambda s : s.strip(), latinsStr.split(','))
    for latin in latins:
        if latin not in latinEnglish:
            latinEnglish[latin] = []

