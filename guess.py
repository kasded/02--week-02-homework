import random

print("Sveiks minēšanas spēlē!")

while True:  # ārējais cikls — spēlējam atkārtoti
    slepenais = random.randint(1, 100)
    meginajumi = 0

    print("\nEs esmu izvēlējies skaitli no 1 līdz 100. Uzmini to!")
    print("Tev ir 10 mēģinājumi.")

    while True:  # iekšējais cikls — minējumi
        minejums = input("Tavs minējums: ")

        # pārbaudām, vai ievade ir skaitlis
        if not minejums.isdigit():
            print("Kļūda: jāievada skaitlis!")
            continue

        minejums = int(minejums)
        meginajumi += 1

        if minejums == slepenais:
            print(f"Pareizi! Tu uzminēji ar {meginajumi} mēģinājumiem.")
            break
        elif minejums < slepenais:
            print("Par mazu!")
        else:
            print("Par lielu!")

        if meginajumi >= 10:
            print(f"\nMēģinājumi beigušies! Pareizā atbilde bija {slepenais}.")
            break

    # piedāvā spēlēt vēlreiz
    velreiz = input("\nVai vēlies spēlēt vēlreiz? (j/n): ").lower()
    if velreiz != "j":
        print("Paldies par spēli!")
        break

