def to_bool(answer: str) -> bool:
    """Pārvērš 'j'/'n' uz True/False."""
    return answer.lower() == "j"


# --- Ievade ar kļūdu apstrādi ---
age_input = input("Ievadi vecumu: ")

try:
    age = int(age_input)
    if age < 0:
        print("Kļūda: vecums nevar būt negatīvs.")
        exit()
except ValueError:
    print("Kļūda: vecumam jābūt skaitlim.")
    exit()

has_license = to_bool(input("Vai ir autovadītāja apliecība? (j/n): "))
is_student = to_bool(input("Vai ir students? (j/n): "))
is_veteran = to_bool(input("Vai ir veterāns? (j/n): "))

print("---")

# --- Loģiskie nosacījumi ---
can_vote = age >= 18
can_rent_car = age >= 21 and has_license
senior_discount = age >= 65 or is_veteran
student_discount = (16 <= age <= 26) and is_student

# --- Palīgfunkcija ✓ ✗ ---
def yes_no(flag: bool) -> str:
    return "Jā ✓" if flag else "Nē ✗"


# --- Rezultātu izvade ---
print(f"Balsošana: {yes_no(can_vote)}")

if not can_rent_car:
    reason = ""
    if age < 21:
        reason = "(par jaunu) "
    if not has_license:
        reason += "(nav apliecības)"
    print(f"Auto īre: Nē ✗ {reason}")
else:
    print("Auto īre: Jā ✓")

print(f"Senioru atlaide: {yes_no(senior_discount)}")
print(f"Studentu atlaide: {yes_no(student_discount)}")
