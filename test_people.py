import pytest
from people import Person, Student, Teacher, AnketaError

# ТЕСТЫ ФИО
@pytest.mark.parametrize("raw, expected", [
    ("иванов иван", "Иванов Иван"),
    ("  петров   петр  ", "Петров Петр"),
    ("петров-водкин кузьма", "Петров-Водкин Кузьма"),
    ("СИДОРОВ СИДОР", "Сидоров Сидор")
])
def test_fio_normalize(raw, expected):
    p = Person(raw, "test@mail.ru", "89211112233")
    assert p.fio == expected

def test_fio_odno_slovo():
    with pytest.raises(AnketaError):
        Person("Иванов", "test@mail.ru", "89211112233")

# ТЕСТЫ ПОЧТЫ
@pytest.mark.parametrize("raw, expected", [
    ("IVAnov@Mail.Ru", "ivanov@mail.ru"),
    ("PETROV@YANDEX.RU", "petrov@yandex.ru")
])
def test_email_lower(raw, expected):
    p = Person("Иванов Иван", raw, "89211112233")
    assert p.email == expected

@pytest.mark.parametrize("bad_email", [
    "kuznetsov.mail.ru", "iv anov@mail.ru", "a@b", "@mail.ru"
])
def test_email_bad(bad_email):
    with pytest.raises(AnketaError):
        Person("Иванов Иван", bad_email, "89211112233")

# ТЕСТЫ ТЕЛЕФОНА
@pytest.mark.parametrize("raw_phone", [
    "+7 (921) 111-22-33", "89211112233", "7 921 111 22 33", "+79211112233"
])
def test_phone_normalize(raw_phone):
    p = Person("Иванов Иван", "a@b.ru", raw_phone)
    assert p.phone == "79211112233"

@pytest.mark.parametrize("bad_phone", [
    "123", "+7 (921) 111-22-334", "59211112233"
])
def test_phone_bad(bad_phone):
    with pytest.raises(AnketaError):
        Person("Иванов Иван", "a@b.ru", bad_phone)

# МАСКА, ИНИЦИАЛЫ, РОЛИ
def test_masked_phone():
    p = Person("Иванов Иван", "a@b.ru", "+7 (921) 111-22-33")
    assert p.masked_phone() == "+7 (921) ***-**-33"

def test_short_fio():
    p = Person("Иванов Иван Петрович", "a@b.ru", "89211112233")
    assert p.short_fio() == "Иванов И. П."

def test_roles():
    s = Student("Иванов Иван", "a@b.ru", "89211112233", "09с33")
    t = Teacher("Петров Петр", "a@b.ru", "89211112233", "Кафедра И9")
    assert s.role() == "студент"
    assert t.role() == "преподаватель"

def test_student_no_group():
    with pytest.raises(AnketaError):
        Student("Иванов Иван", "a@b.ru", "89211112233", "   ")