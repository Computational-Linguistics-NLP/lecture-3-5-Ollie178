# Первый способ
text = input("Введите текст: ")
dlina = len(text)
if dlina <= 2:
    print("чудовищно мало")
elif dlina <= 5:
    print("очень мало")
elif dlina <= 10:
    print("мало")
elif dlina <= 30:
    print("ок")
elif dlina <= 100:
    print("много")
else:
    print("чудовищно много")



# Второй способ
text = input("Введите текст: ")
dlina = len(text)
result = "чудовищно много"
if dlina <= 2:
    result = "чудовищно мало "
if 2 < dlina <= 5:
    result = "очень мало"
if 5 < dlina <= 10:
    result = "мало"
if 10 < dlina <= 30:
    result = "ок"
if 30 < dlina <= 100:
    result = "много"
print(result)
