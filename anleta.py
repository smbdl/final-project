print("Здравствуйте! Необходимо запполнить анкету.")

name = input("Введите ваше имя: ").title()
while True:
    try:
        age = int(input("Введите ваш возраст: "))
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите число для возраста.")

gender = input("Введите ваш пол: ")

while True:
    try:
        weight = float(input("Введите ваш вес (в кг): "))
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите число для веса.")

while True:
    try:
        height = float(input("Введите ваш рост (в см): "))
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите число для роста.")

print("\nГотово, вот ваши данные: ")
print("Имя:", name)
print("Возраст:", age)
print("Пол:", gender)
print("Вес:", weight, "кг")
print("Рост:", height, "см")