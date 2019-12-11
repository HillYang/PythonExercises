while True:
    s1 = input('Please enter something you like (exit to quit):')
    if s1 == 'exit':
        break
    if len(s1) < 3:
        print('input is too small.')
        continue
    print('your input is of sufficient length.')
print('continue example is done')

while True:
    s = input('Please enter something you like :')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Your input is too small.')
    else:
        print('Your input is of sufficient length.')
print('Loop is done')