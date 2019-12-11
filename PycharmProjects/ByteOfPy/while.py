number = 23
running = True

while running:
    guess = int(input('Please enter an integer!: '))
    if guess == number:
        print('Yes, congratulations, you guessed it!')
        running = False
    elif guess < number:
        print("No, it's a little higher than that..")
    else:
        print("No, it's a little lower than that..")
else:
    print('The while loop is done')
