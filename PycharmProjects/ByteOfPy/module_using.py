import sys
import os

print('The command line arguments are :')
for i in sys.argv:
    print(i)

print('\n\nthe PYTHON_PATH is ', sys.path, '\n')

print(sys.argv[0])
print(os.getcwd())
print(__name__)
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('This program is being run by imported from another module')
