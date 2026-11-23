class AgeError(Exception):
    pass

class Person:
    def __init__(self, name, age):
        if age < 0 or age > 120:
            raise AgeError(f"{name} – возраст {age} вне границ 0..120")
        self.name = name
        self.age = age

people = [("Иванов Иван", 19), ("Петрова Анна", 200), ("Сидоров Пётр", -5)]
good = []
for name, age in people:
    try:
        p = Person(name, age)
        good.append(p)
    except AgeError as e:
        print("Не принято:", e)

for p in good:
    print(f"Принято: {p.name}, {p.age} лет")