#NUMBER GUESSING GAME
		
import random

# Generate a random number between 1 and 50
num = random.randint(1, 50)

print("🎯 Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 50.")

while True:
    inp = int(input("Enter your guess: "))

    if inp == num:
        print("🎉 Congratulations! You guessed it right!")
        break
    elif abs(num - inp) <= 5:
        print("🔥 Very close! Just a little higher!" if inp < num else "🔥 Very close! Just a little lower!")
    elif abs(num - inp) <= 10:
        print("✨ Close! Try going higher!" if inp < num else "✨ Close! Try going lower!")
    else:
        print("❌ Far away! Guess much higher!" if inp < num else "❌ Far away! Guess much lower!")
