import random
import re

def intro():
    print('Здравствуй, дорогой друг. Я - генератор стишков-"пирожков", и я предлагаю тебе познакомиться с моим творчеством. Но для начала выбери фандом: \n 1) "Руслан и Людмила" А.С.Пушкин \n 2) Стихотворения Фредерико Гарсии Лорка (недоступно сейчас) \n 3) Актуальные новости (недоступно сейчас) \n 4) Тексты песен Земфиры (недоступно сейчас) \n 5) Песенки и стихотворения из "Смешариков" ')
    element = input()
    while element != '1' and element != '2' and element != '3' and element != '4' and element != '5':
        print('Неправильно выбран фандом. Попробуйте ещё раз!')
        element = input()
    if element == '1':
          element = 'Руслан.txt'
    elif element == '2':
          element = 'Лорка.txt'
    elif element == '3':
          element = 'Новости.txt'
    elif element == '4':
          element = 'Земфира.txt'
    elif element == '5':
          element = 'Смешарики.txt'
    return element

def opener(element):
    with open(element, encoding='utf-8') as file:
        text = file.read()
    return text

def first_third(text):
    st = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию]\'[цкнгшщзхфвпрлджчсмтьбъ]* ?'
    unst = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию][^\'][цкнгшщзхфвпрлджчсмтьбъ]* ?'
    pattern = unst + st + unst + st + unst + st + unst + st + unst
    result = re.findall(pattern, text)
    result1 = random.choice(result)
    result3 = random.choice(result)
    return result1, result3

def second(text):
    st = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию]\'[цкнгшщзхфвпрлджчсмтьбъ]* ?'
    unst = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию][^\'][цкнгшщзхфвпрлджчсмтьбъ]* ?'
    pattern = unst + st + unst + st + unst + st + unst + st
    result2 = re.findall(pattern, text)
    result2 = random.choice(result2)
    pattern_rhyme = st + '$'
    rhyme = re.search(pattern_rhyme, result2)
    rhyme = rhyme.group()
    return result2, rhyme
    
def fourth(text, rhyme):
    rhyme = rhyme[1]
    st = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию]\'[цкнгшщзхфвпрлджчсмтьбъ]* ?'
    unst = '[цкнгшщзхфвпрлджчсмтьбъ]*[уеыаоэяию][^\'][цкнгшщзхфвпрлджчсмтьбъ]* ?'
    rhyme_find = unst + rhyme
    fourthsearcher = re.findall(rhyme_find, text)
    fourthsearcher = ' '.join(fourthsearcher)
    pattern = unst + st
    result4 = re.findall(pattern, fourthsearcher)
    result4 = random.choice(result4)
    return result4


def main():
    a = intro()
    b = opener(a)
    c1 = first_third(b)
    c2 = second(b)
    c3 = first_third(b)
    c4 = fourth(b, c2)
    c = list()
    c.append(c1[0])
    c.append(c2[0])
    c.append(c3[0])
    c.append(c4)
    c = '\n'.join(c)
    print(c)
    
if __name__ == '__main__':
    main()
