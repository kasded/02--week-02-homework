skaitlis = int(2)
String = str("Hi")
Float = float(5.22)

#Paskatas kas tie tādi ir
print(type(skaitlis))
print(type(String))
print(type(Float))

print(bool(skaitlis)) #Pārbaude vai skaitlis
print(bool(String)) # pārbauda vai string
print(bool(Float)) #Pārbauda vai float




print(int(3.86))
# print(int("3.14")) nedarbojas jo tas ir string iekomentats lai turpinatos kods 
print(int(float("3.14")))
