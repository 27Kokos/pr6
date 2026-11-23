class Temperature:
    def __init__(self, c):
        self.c = c

    @property
    def fahrenheit(self):
        return self.c * 9 / 5 + 32

    def __str__(self):
        return f"{self.c:.1f} C = {self.fahrenheit:.1f} F"

    def __lt__(self, other):
        return self.c < other.c

t1 = Temperature(21.5)
t2 = Temperature(-3.0)
t3 = Temperature(10.0)
temps = [t1, t2, t3]
print(t1)
print(t2)
print("по возрастанию:")
for t in sorted(temps):
    print(t)
print("самый тёплый:", max(temps))