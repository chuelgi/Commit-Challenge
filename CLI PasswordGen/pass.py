from random import choice
from string import ascii_letters, digits, punctuation
#secrets is for security tasks

bank = digits + ascii_letters +punctuation
print('Welcome to password generator.')
pl = input('Enter password length: ')

res = ''
for x in range(int(pl)):
    res += choice(bank)

print('\nGenerated password: ')
print(res)
