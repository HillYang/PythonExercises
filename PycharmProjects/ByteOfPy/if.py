number = 23

guess = int(input('Enter an integer :'))

if guess == number:
    print('Congratulations, you guessed it!')

elif guess < number:
    print("No, it's a little higher than that.")

else:
    print("No, it's a little lower than that.")

print('Done, you have only one chance.')

