import random
.
n = random.randint(1, 100)

a = -1

guesses = 0

print("\n" + "=" * 30)  # string repetition
print("🎯 NUMBER GUESSING GAME")
print("=" * 30)

while(a != n):

    print("Choose a number between 1 and 100")
    
    try:
        a = int(input("Guess The Number Please: "))

        if (a < 1 or a > 100):
            print("Invalid Number")

        else:
            guesses += 1
            
            if (a > n):
                print("Lower Number Please")
                
            elif (a == n):
                print("🎉 Correct! You guessed the number.")
                
            elif (a < n):
                print("Higher Number Please")

    except ValueError:
        print("Invalid Input")

print(f"You have guessed the number {n} correctly in {guesses} attempts.")