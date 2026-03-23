# Konstantes
KM_TO_MI = 0.621371
MI_TO_KM = 1.609340

KG_TO_LB = 2.20462
LB_TO_KG = 0.453592

L_TO_GAL = 0.264172
GAL_TO_L = 3.785410

USD_TO_EUR = 0.84235020
EUR_TO_USD = 0.87000000



print("Izvēlies konversiju: 1) km<->mi 2) kg<->lb 3) L<->gal 4) $<->€")
choice = input("> ")

# --- KM <-> MI ---
if choice == "1":
    print("Virziens: 1) km -> mi 2) mi -> km")
    direction = input("> ")

    try:
        value = float(input("Ievadi vērtību: "))
        if direction == "1":
            result = value * KM_TO_MI
            print(f"{value:.2f} km = {result:.2f} mi")
        elif direction == "2":
            result = value * MI_TO_KM
            print(f"{value:.2f} mi = {result:.2f} km")
        else:
            print("Nepareizs virziens.")
    except ValueError:
        print("Kļūda: jāievada skaitlis.")

# --- KG <-> LB ---
elif choice == "2":
    print("Virziens: 1) kg -> lb 2) lb -> kg")
    direction = input("> ")

    try:
        value = float(input("Ievadi vērtību: "))
        if direction == "1":
            result = value * KG_TO_LB
            print(f"{value:.2f} kg = {result:.2f} lb")
        elif direction == "2":
            result = value * LB_TO_KG
            print(f"{value:.2f} lb = {result:.2f} kg")
        else:
            print("Nepareizs virziens.")
    except ValueError:
        print("Kļūda: jāievada skaitlis.")

# --- L <-> GAL ---
elif choice == "3":
    print("Virziens: 1) L -> gal 2) gal -> L")
    direction = input("> ")

    try:
        value = float(input("Ievadi vērtību: "))
        if direction == "1":
            result = value * L_TO_GAL
            print(f"{value:.2f} L = {result:.2f} gal")
        elif direction == "2":
            result = value * GAL_TO_L
            print(f"{value:.2f} gal = {result:.2f} L")
        else:
            print("Nepareizs virziens.")
    except ValueError:
        print("Kļūda: jāievada skaitlis.")

# --- USD <-> EUR ---
elif choice == "4":
    print("Virziens: 1) $ -> € 2) € -> $")
    direction = input("> ")

    try:
        value = float(input("Ievadi vērtību: "))
        if direction == "1":
            result = value * USD_TO_EUR
            print(f"{value:.2f} $ = {result:.2f} €")
        elif direction == "2":
            result = value * EUR_TO_USD
            print(f"{value:.2f} € = {result:.2f} $")
        else:
            print("Nepareizs virziens.")
    except ValueError:
        print("Kļūda: jāievada skaitlis.")

else:
    print("Nepareiza izvēle.")

