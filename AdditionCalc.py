import time, os
while True:
    try:
        x = input('What is the first number?: ')
        y = input('What is the second number?: ')
        ans = int(x) + int(y)
        print(f'\n{x} + {y} = {ans}')
        z = input('\nEnter any key to continue. ')
        os.system('cls')
    except:
        print('Invalid choice.')
        time.sleep(2)