# Foydalanuvchidan son kiritishni so'raymiz
son = int(input("Biror butun son kiriting: "))

# Juft yoki to'q ekanligini tekshiramiz
if son % 2 == 0:
    print(f"{son} — juft son.")
else:
    print(f"{son} — to'q son.")

# Musbat yoki manfiyligini tekshiramiz (ichma-ich if-else)
if son >= 0:
    if son == 0:
        print("Kiritilgan son nolga teng.")
    else:
        print(f"{son} — musbat son.")
else:
    print(f"{son} — manfiy son.")