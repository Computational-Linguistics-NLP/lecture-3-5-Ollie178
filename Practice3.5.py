text = input("Введите текст: ")
dlina = len(text)
if dlina <= 2:
    print("чудовищно мало")
else:
    if dlina <= 5:
        print("очень мало")
    else:
        if dlina <= 10:
                print("мало")
        else:
            if dlina <= 30:
                print("ок")
            else:
                if dlina <= 100:
                    print("много")
                else:
                    print("чудовищно много")
