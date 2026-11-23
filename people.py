class AnketaError(Exception):
    pass

class Person:
    def __init__(self, fio, email, phone):
        self.fio = self.check_fio(fio)
        self.email = self.check_email(email)
        self.phone = self.check_phone(phone)

    @staticmethod
    def check_fio(fio):
        parts = fio.split()
        if len(parts) < 2:
            raise AnketaError("в ФИО меньше двух слов")
        return " ".join(parts).title()

    @staticmethod
    def check_email(email):
        email = email.strip().lower()
        if email.count("@") != 1:
            raise AnketaError("неверная почта")
        parts = email.split("@")
        if not parts[0] or not parts[1] or "." not in parts[1] or parts[1].startswith(".") or parts[1].endswith("."):
            raise AnketaError("неверная почта")
        return email

    @staticmethod
    def check_phone(phone):
        digits = "".join(c for c in phone if c.isdigit())
        if len(digits) != 11 or digits[0] not in "78":
            raise AnketaError("неверный телефон")
        if digits[0] == "8":
            digits = "7" + digits[1:]
        return digits

    def masked_phone(self):
        return f"+7 ({self.phone[1:4]}) ***-**-{self.phone[9:]}"

    def short_fio(self):
        parts = self.fio.split()
        if len(parts) == 2:
            return parts[0] + " " + parts[1][0] + "."
        return parts[0] + " " + parts[1][0] + ". " + parts[2][0] + "."

    def role(self):
        return "неизвестно"

    def extra(self):
        return "нет"

    def __str__(self):
        return self.fio

    def __lt__(self, other):
        return self.fio < other.fio

class Student(Person):
    def __init__(self, fio, email, phone, group):
        super().__init__(fio, email, phone)
        if not group.strip():
            raise AnketaError("пустая группа")
        self.group = group.strip()

    def role(self):
        return "студент"

    def extra(self):
        return self.group

class Teacher(Person):
    def __init__(self, fio, email, phone, dept):
        super().__init__(fio, email, phone)
        if not dept.strip():
            raise AnketaError("пустая кафедра")
        self.dept = dept.strip()

    def role(self):
        return "преподаватель"

    def extra(self):
        return self.dept