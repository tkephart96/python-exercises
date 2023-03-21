# functions exercise
# is_two defines a single integer, n, and will return true or false if it is a 2
def is_two(n):
    # will return true or false after making n an int if it can and if it is 2
    return int(n) == 2

# is_vowel defines a single character string, i, and checks if it is a vowel
def is_vowel(i):
    # v = ['a', 'e', 'i', 'o', 'u']
    v = 'aeiou'
    return type(i) == str and len(i) == 1 and i.lower() in v

# is it a consonant
def is_consonant(i):
    return type(i) == str and i.isalpha() == True and is_vowel(i) == False

# cap first letter
def cap(s):
    if is_consonant(s) == True:
        return s.capitalize()

# calculate tip
def calculate_tip(tip, bill):
    if 0 <= tip <= 1:
        return bill + (bill * tip)

# apply discount
def apply_discount(discount, bill):
    if 0 <= discount <= 1:
        return bill - (bill * discount)

# handle commas
def handle_commas(s):
    return int(s.replace(',',''))

# get letter grade
def get_letter_grade(n):
    if type(n) in [int, float]:
        if n > 87:
            g = 'A'
        elif n > 79:
            g = 'B'
        elif n > 66:
            g = 'C'
        elif n > 59:
            g = 'D'
        else:
            g = 'F'
        return g

# remove vowels
def remove_vowels(s):
    for c in s:
        if is_vowel(c):
            s = s.replace(c,'')
    return s

# normalize name
def normalize_name(s):
    s = s.strip()
    for i in s:
        if i in ['!','@','#','$','%']:
            s = s.replace(i,'')
        if s[0].isdigit() == True:
            s = s.replace(s[0],'')
        if is_vowel(i) == True or is_consonant(i) == True:
            continue
    s = ((s.strip()).replace(' ','_')).lower()
    return s

# cumulative sum
def cumulative_sum(ls):
    for i in range(1, len(ls)):
        ls[i] += ls[i-1]
    return ls

# Bonus
# convert from am/pm to 24-hour
def twelveto24(t):
    t = t.replace(':','')
    if 'pm' in t:
        t = int(t.strip('pm'))
        if t < 1200:
            t += 1200
            if t >= 2400:
                t -= 2400
    if 'am' in t and t >= '1200am':
        t = t.strip('12')
    t = str(t)
    t = t.strip('am')
    t = ((4 - len(t)) * '0') + t
    t = t[:2] + ':' + t[2:]
    return t

# convert 24-hour to am/pm
def twelvefrom24(t):
    t = t.replace(':','')
    if t >= '1300':
        t = int(t) - 1200
        t = str(t) + 'pm'
    else:
        t = int(t)
        if t < 100:
            t += 1200
            t = str(t) + 'am'
        elif t < 1200:
            t = str(t) + 'am'
        else:
            t = str(t) + 'pm'
    t = t[:-4] + ':' + t[-4:]
    return t
