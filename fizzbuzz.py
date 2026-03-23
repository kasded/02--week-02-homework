import sys

# --- Pārbaudām, vai ir padots N ---
if len(sys.argv) < 2:
    print("Kļūda: jānorāda skaitlis N. Piemērs: python fizzbuzz.py 20 3 Fizz 5 Buzz 7 Jazz")
    sys.exit()

# --- Pārbaudām, vai N ir skaitlis ---
try:
    N = int(sys.argv[1])
    if N <= 0:
        print("Kļūda: N jābūt pozitīvam veselam skaitlim.")
        sys.exit()
except ValueError:
    print("Kļūda: N jābūt veselam skaitlim.")
    sys.exit()

# --- Parametrizētie noteikumi ---
# Formāts: python fizzbuzz.py 20 3 Fizz 5 Buzz 7 Jazz
# Tātad pāri: (3, "Fizz"), (5, "Buzz"), (7, "Jazz")

rules = []

args = sys.argv[2:]

if len(args) % 2 != 0:
    print("Kļūda: noteikumiem jābūt pāros: <skaitlis> <vārds>")
    sys.exit()

for i in range(0, len(args), 2):
    try:
        divisor = int(args[i])
        word = args[i + 1]
        rules.append((divisor, word))
    except ValueError:
        print("Kļūda: dalītājam jābūt skaitlim.")
        sys.exit()

# Ja nav noteikumu, izmanto klasisko FizzBuzz
if not rules:
    rules = [(3, "Fizz"), (5, "Buzz")]

# --- FizzBuzz loģika ---
for i in range(1, N + 1):
    output = ""

    for divisor, word in rules:
        if i % divisor == 0:
            output += word

    print(output if output else i)

