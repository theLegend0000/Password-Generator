import random as r
space = ' '
print(space*10,end='')
for i in range(20):         # some basic styling for the intro
    print('*',end='')

print(f'\n{space*11}PASSWORD GENRATOR')

print(space*10,end='')

for i in range(20):     
    print('*',end='')
print()

upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerCase = upperCase.lower()
numbers = '0123456789'
specialCh = '!@#$%&*'

while True:

    length = int(input('Enter the length of your password\n(minimum length is 8): '))
    if length >= 8:
        break
    else:
        print('length should be atleast 8')
        
    

##strength = input('Write the strength of your password(normal,strong,very strong) : ')
##
##test = ''
##
##if strength.lower() == 'normal':
##    test+=lowerCase
##    test+=numbers
##elif strength.lower() == 'strong':
##    test+=upperCase
##    test+=lowerCase
##    test+=numbers
##elif strength.lower() == 'very strong':
##    test+=upperCase
##    test+=lowerCase
##    test+=numbers
##    test+=specialCh


password = ''.join(r.sample(specialCh,round(length/8))) + ''.join(r.sample(upperCase,round(length/4))) + ''.join(r.sample(lowerCase,round(length/3))) + ''.join(r.sample(numbers,round(length/3)))


##print('Your password is',password)
print(f'Your password is: "{password}"')



