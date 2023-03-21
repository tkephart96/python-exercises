# conditional basics
# monday or not
day = input('Please enter a day of the week: ')
day = day.lower()

if day == 'mon' or day == 'monday':
    print('It is Monday')
else:
    print('It is not Monday')

# weekend or not
day = input('Please enter a day of the week: ')
day = day.lower()
weekend = ['sun', 'sat', 'sunday', 'saturday']

if day in weekend:
    print('It is the weekend')
else:
    print('It is a weekday')

# calculate weekly pay
hr_rate = 35
ot_rate = hr_rate * 1.5
hrs_worked = int(input('Hours worked: '))
ot_hrs = hrs_worked - 40
ot_pay = ot_hrs * ot_rate

if ot_hrs > 0:
    paycheck = hr_rate * hrs_worked + ot_pay
    print(paycheck)
    print('including overtime')
else:
    paycheck = hr_rate * hrs_worked
    print(paycheck)
    print('no overtime')

# loop basics
# while loop

i = int(input('Input number less than 15:'))

while i <= 15:
    print(i)
    i += 1

i = int(input('Input number less than 100:'))

while i <= 100:
    print(i)
    i += 2

i = int(input('Input number less than 1 mil:'))

while i <= 1_000_000:
    print(i)
    i **= 2

i = int(input('Input number greater than 5:'))

while i > 0:
    print(i)
    i -= 5

# for loop

num = int(input('Please enter a number for multiples table: '))
table = range(1, 11)

for n in table:
    m = num * n
    # print(num, 'x', n, '=', m)
    print(f'{num} x {n} = {m}')

nums = range(1, int(input('small number please: ')))

for n in nums:
    # n = str(n) * n
    # print(n)
    print(n*str(n))

# break and continue
i = int(input('Please enter a positive number: '))

# while i > 0:
#     print(i)
#     i -= 1
#     if i == 0:
#         break
for i in range(i, 0, -1):
    print(i)

n = range(int(input('Please enter a positive number: ')) + 1)

for i in n:
    print(i)

while True:
    i = input('Enter an odd number between 1 and 50: ')
    if i.isdigit() == False:
        print('Invalid input! Input odd number between 1 and 50')
        continue
    i = int(i)
    if i % 2 == 0:
        print('Invalid input! Input odd number between 1 and 50')
        continue
    if i < 1 or i > 50:
        print('Invalid input! Input odd number between 1 and 50')
        continue
    for n in range(1, 50, 2):
        if n == i:
            print(f'Yikes! Skipping number: {i}')
            continue
        print(n)
    break

# FizzBuzz
i = input('run FizzBuzz? y or n')
if i == 'y':
    for n in range(1, 101):
        if n % 15 == 0:
            print('FizzBuzz')
        elif n % 5 == 0:
            print('Buzz')
        elif n % 3 == 0:
            print('Fizz')
        else:
            print(n)

# display table of powers

while True:
    i = int(input('What number would you like to go up to?'))
    print('Here is your table!')
    print('number', '| squared', '| cubed')
    print('------', '| -------', '| -----')
    for n in range(1, i + 1):
        print('{:<6} | {:<7} | {:1}'.format(n, n ** 2, n ** 3))
    cont = input('Would you like to continue? y or n')
    if cont.lower() == 'y':
        continue
    break

# grades

while True:
    n = int(input('Enter grade score from 0-100: '))
    if n > 87:
        print('A')
    elif n > 79:
        print('B')
    elif n > 66:
        print('C')
    elif n > 59:
        print('D')
    else:
        print('F')
    cont = input('Would you like to continue? y or n')
    if cont.lower() == 'y':
        continue
    break

# list of dict

library = [
    dict(title='Tales of Demons and Gods', author='MadSnail', genre='Action'),
    dict(title="Omniscient Reader's Viewpoint", author='Sing-Shong', genre='Fantasy'),
    dict(title='Overlord', author='Kugane Maruyama', genre='Fantasy')
]
i = input('list library? y or n')
if i == 'y':
    for i in library:
        print(i['title'], '-', i['author'], '-', i['genre'])

g = input('Choose a genre: Action or Fantasy?')
for l in library:
    if g == l['genre'].lower():
        print(l['title'])

