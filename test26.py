person = {}

person["name"] = input ("Name: ")
person ["age"] = int(input("Alter: "))
person ["city"]= input ("Stadt: ")

print ("\nZusammenfassung:")
for key, value in person.items():
    print(f"{key}:{value}")