import random

print("🎯 Zahlen-Ratespiel 🎯")
print("Ich denke mir eine Zahl zwischen 1 und 10 aus.")

secret = random.randint(1, 10)

while True:
    guess = int(input("Dein Tipp: "))

    if guess == secret:
        print("🎉 Richtig! Du hast gewonnen!")
        break
    elif guess < secret:
        print("Zu niedrig, versuch’s nochmal!")
    else:
        print("Zu hoch, versuch’s nochmal!")
