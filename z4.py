class Figure:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def __str__(self):
        return f"{self.name}: площадь {self.area():.2f}"

class Rect(Figure):
    def __init__(self, w, h):
        super().__init__("Прямоугольник")
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Figure):
    def __init__(self, r):
        super().__init__("Круг")
        self.r = r

    def area(self):
        return 3.14159 * self.r * self.r

figs = [Rect(3, 4), Circle(2), Rect(5, 3)]
total = 0
for f in figs:
    print(f)
    total += f.area()
print(f"Общая площадь: {total:.2f}")