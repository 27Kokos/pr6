import pytest
from registry import Registry
from people import Student, Teacher

@pytest.fixture
def test_registry(tmp_path):
    f = tmp_path / "test_anketa.txt"
    f.write_text(
        "s; иванов иван;ivanov@mail.ru;89211112233;09c33\n"
        "t; петров петр;petrov@mail.ru;89211112233;Кафедра И9\n"
        "s; сидорова анна;sidorova@mail.ru;89211112233;09c34\n"
        "x; непонятный;bad@mail.ru;89211112233;что-то\n"
        "s; иванов;bad@mail.ru;89211112233;09c33\n"
        "s; плохая почта;bad.mail.ru;89211112233;09c33\n", 
        encoding="utf-8"
    )
    reg = Registry()
    reg.load(f)
    return reg

def test_empty_registry():
    assert len(Registry()) == 0

def test_registry_load(test_registry):
    assert len(test_registry.good) == 3

def test_registry_bad_count(test_registry):
    assert len(test_registry.bad) == 3

def test_registry_bad_lines(test_registry):
    lines = [b[0] for b in test_registry.bad]
    assert lines == [4, 5, 6]

def test_load_missing_file():
    reg = Registry()
    assert reg.load("net_takogo.txt") is False

def test_stats_roles(test_registry):
    roles, _ = test_registry.stats()
    assert roles == {"студент": 2, "преподаватель": 1}

def test_stats_groups(test_registry):
    _, groups = test_registry.stats()
    assert groups == {"09c33": 1, "09c34": 1, "Кафедра И9": 1}

def test_iteration(test_registry):
    count = 0
    for p in test_registry.good:
        count += 1
    assert count == 3

def test_sorting(test_registry):
    test_registry.good.sort()
    assert test_registry.good[0].fio == "Иванов Иван"
    assert test_registry.good[1].fio == "Петров Петр"
    assert test_registry.good[2].fio == "Сидорова Анна"

def test_save_ok(test_registry, tmp_path):
    path = tmp_path / "ok.txt"
    test_registry.save_ok(path)
    assert path.exists()
    lines = path.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 3

def test_save_errors(test_registry, tmp_path):
    path = tmp_path / "errors.txt"
    test_registry.save_errors(path)
    assert path.exists()
    content = path.read_text(encoding="utf-8")
    assert "неизвестный тип" in content