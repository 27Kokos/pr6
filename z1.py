class Student:
    def __init__(self, fio, group):
        self.fio = fio
        self.group = group

    def short(self):
        parts = self.fio.split()
        if len(parts) == 2:
            return parts[0] + " " + parts[1][0] + "."
        elif len(parts) >= 3:
            return parts[0] + " " + parts[1][0] + ". " + parts[2][0] + "."
        return self.fio

s1 = Student("Иванов Иван Петрович", "09с33")
s2 = Student("Петрова Анна", "09с34")
print(s1.short(), "|", s1.group)
print(s2.short(), "|", s2.group)