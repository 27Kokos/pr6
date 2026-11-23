class Counter:
    def __init__(self, name):
        self.name = name
        self.value = 0

    def add(self, n=1):
        self.value += n

    def reset(self):
        self.value = 0

    def __str__(self):
        return self.name + ": " + str(self.value)

c1 = Counter("принято")
c2 = Counter("отклонено")
c1.add(7)
c2.add(1)
print(c1, c2)
c1.reset()
print("после сброса:", c1)