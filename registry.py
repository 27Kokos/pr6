from people import Student, Teacher, AnketaError

class Registry:
    def __init__(self):
        self.good = []
        self.bad = []

    def load(self, filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            return False

        for i, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split(";")
            if len(parts) != 5:
                self.bad.append((i, line, "полей не 5"))
                continue
            t, fio, email, phone, extra = parts
            try:
                if t == "s":
                    self.good.append(Student(fio, email, phone, extra))
                elif t == "t":
                    self.good.append(Teacher(fio, email, phone, extra))
                else:
                    raise AnketaError("неизвестный тип: " + t)
            except AnketaError as e:
                self.bad.append((i, line, str(e)))
        return True

    def add(self, person):
        self.good.append(person)

    def __len__(self):
        return len(self.good)

    def save_ok(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for p in self.good:
                f.write(f"{p.fio};{p.email};{p.phone}\n")

    def save_errors(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            for b in self.bad:
                f.write(f"Строка {b[0]}: {b[2]}\n{b[1]}\n")

    def stats(self):
        roles = {}
        groups = {}
        for p in self.good:
            r = p.role()
            roles[r] = roles.get(r, 0) + 1
            e = p.extra()
            groups[e] = groups.get(e, 0) + 1
        return roles, groups