def summa(a, b):
    return a + b

def skidka(cena, procent):
    if procent < 0 or procent > 90:
        raise ValueError("Скидка должна быть от 0 до 90")
    return round(cena - (cena * procent / 100), 2)

def srednee(spisok):
    if len(spisok) == 0:
        raise ValueError("Список пуст")
    return sum(spisok) / len(spisok)