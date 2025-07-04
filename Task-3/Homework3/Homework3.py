import random

mass = []

while True:
    print("Нажмите 1 что бы сгенерировать новое число или 0 что бы выйти")
    x = int(input())
    if x == 1:
        rand = random.randint(1, 100)
        print(rand)
        mass.append(rand)
    elif x == 0:
        break
for num in mass[:-1]:
    print(f"Ваши числа {num}")