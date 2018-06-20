import random
r = random.randint(0,100)
print r
guesses = []

print "I have a number now. Its your turn to guess !"

while True:
    guess = input('Enter your guess (0-100): ')
    guesses.append(str(guess))
    
    if guess < r:
        print "Low"
    elif guess > r:
        print "High"
    else:
        print "Bingo! you guessed it right!"
        print "You took", len(guesses), "guesses"
        print "These were your guesses"
        print "-->".join(guesses)
        break


# 58
# enter a guess
# 20
# Low
# 70
# High
# 50
# Low
# Bingo! you got it right

# 50-->70-->45

