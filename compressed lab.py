#space kasi masulit nak
def space():
    print ("\n\n--------------------------------------------------------------\n\n")

#prent case :)
def case(q):
    print('case ', q, ' \n\n')

#case 1
case(1)


pi = 3.14159
diameter = 3
rad = diameter/2
area = pi*(rad*rad)
print (area)


space()
#case 2
case(2)


exp1 = (5 - 3)//2
print (exp1)


space()
#case 3
case(3)


res = (8 - 3) * (2 - (1 + 1))
print (res)


space()
#boleans and conditionals
#case 1
print('boleans and conditionals')
case(1)


def sign(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    elif num < 0:
        return -1
print (sign(10))
print (sign(-15))
print (sign(0))

space()
#case 2
case(2)

def to_smash(total_candies):
    print("Splitting", total_candies, "candies")
    return total_candies % 3

print (to_smash(91), "left to smash")
print (to_smash(1), "left to smash")
print (to_smash(3), "left to smash")
print (to_smash(100), "left to smash")

space()
#case 3
case(3)

def exactly_one_sauce(ketchup, mustard, onion):
    if (
        ketchup == True
        and mustard == False
        or ketchup == False
        and mustard == True
    ):
        return True
    elif ketchup == True and mustard == True:
        return False
    else:
        return False

print(exactly_one_sauce(True, False, True))
print(exactly_one_sauce(True, True, True))
print(exactly_one_sauce(False, True, False))
print(exactly_one_sauce(False, False, True))
print(exactly_one_sauce(True, False, False))
print(exactly_one_sauce(False, True, False))

space()
#func and py doc
#case 1
print('functions and python documents')
case(1)

def to_share(total_candies, n_friends=4):
    return  print(total_candies / n_friends)

to_share(10, 4)
to_share(5)
to_share(1, 5)

space()
#case 2
case(2)

def match(x,y):
    if x<y :
        return print(x)
    elif x>y :
        return print(y)
    
match(0, -2)
match(10, -21)
match(-5, 25)

space()
#case3
case(3)

def neg(x):
    if x > 0:
        return print("-"  + str(x))
    else:
        return print(x)
    
neg(-10)
neg(0)
neg(91)
space()


#list and tuples
#case 1
print('list and tuples')
case(1)

def select_last(L):
    if L:
        return L[-1]
    else:
        return None

cakes = ['sponge', 'biscuit', 'chiffon', 'genoise']
soda = ['coke', 'sprite', 'royal']
sugar = []

print(select_last(cakes))
print(select_last(soda))
print(select_last(sugar))

space()
#case 2
case(2)

def losing_team_captain(team):
    if team:
        worst_team = team[-1]
        if len(worst_team) >= 2:
            return worst_team[1]  # Second player is the captain
        else:
            return None  # No captain found for the worst team
    else:
        return None
    
t1 = [
    ['Mark', 'Simon', 'George', 'Percy', 'Jake', 'Rudy'],
    ['Jonathan', 'Ashton', 'Leo', 'Lance', 'Jed', 'Felix'], 
    ['Oliver', 'Liam', 'Daniel', 'Miles', 'Henry', 'Harry']
]

print(losing_team_captain(t1))

space()
#case 3
case(3)

def fashionably_late(arrivals, name):
    index = arrivals.index(name)
    return index > len(arrivals)/2 and index != len(arrivals) - 1

attendees = ['George', 'Annie', 'Owen', 'Lorna', 'Mona', 'Gilbert', 'Ford']

print(fashionably_late(attendees, 'George'))
print(fashionably_late(attendees, 'Gilbert'))
print(fashionably_late(attendees, 'Lorna'))
print(fashionably_late(attendees, 'Mona'))


space()
#loops 
#case 1
print('loops and list comprehenshion')
case(1)

def is_lucky(nums):
    for nums in nums:
        if nums == 0:
            return False
        luck = nums% 9
        if luck == 0:
            return True
        else:
            continue
    if nums != 0:
        return False

x = [1, 3, 2, 18, 9]
y = [81, 5, 1, 1]
z = [0, 0, 1, 1]

print("is X lucky? ", is_lucky(x))
print("is Y lucky? ", is_lucky(y))
print("is Z lucky? ", is_lucky(z))

space()
#case 2
case(2)

def list_is_greater(L, thresh):
    return [True if x > thresh else False for x in L]

x = [1, 3, 2, 18, 9]
y = [81, 5, 1, 1]
z = [0, 0, 1, 1]

print(list_is_greater(x, 3))
print(list_is_greater(x, 81))
print(list_is_greater(x, 0))

space()
#case 3
case(3)

def check_duplicate(L):
    seen = set()
    for no in L:
        if no in seen:
            return True
        seen.add(no)
    return False

x = [1, 3, 2, 18, 9]
y = [81, 5, 1, 1]
z = [0, 0, 1, 1]

print(check_duplicate(x))
print(check_duplicate(y))
print(check_duplicate(z))