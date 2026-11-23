from registry import Registry

reg = Registry()
if not reg.load("anketa.txt"):
    print("Файл anketa.txt не найден")
    exit()

reg.good.sort()

print(f"{'№':<3} | {'ФИО':<30} | {'Роль':<15} | {'Группа/кафедра':<20} | {'Телефон'}")
print("-" * 90)
for i, p in enumerate(reg.good, 1):
    print(f"{i:<3} | {p.fio:<30} | {p.role():<15} | {p.extra():<20} | {p.masked_phone()}")

print("-" * 90)
print(f"Принято: {len(reg.good)} | Отклонено: {len(reg.bad)}")

if reg.bad:
    print("Отклоненные строки:")
    for b in reg.bad:
        print(f"строка {b[0]}: {b[2]}")

roles, groups = reg.stats()
print("По ролям:")
for k, v in roles.items():
    print(" ", k, v)
print("По группам:")
for k, v in groups.items():
    print(" ", k, v)

reg.save()
print("Сохранено в ok.txt и errors.txt")