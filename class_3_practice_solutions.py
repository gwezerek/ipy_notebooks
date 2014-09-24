#Class 3 Practice Solutions

#1.

m = [1,2,3,4,5,6]

n = 0
while n < len(m):
    if n % 2 == 0:
        print(m[n])
    n += 1

################

#2.

nums = []

n = 0
while n < 10:
    nums.append(int(input("give me a number: ")))
    n += 1

n = 0
while n < len(nums):
    if nums[n] % 3 == 0:
        del nums[n]
    n += 1

print(nums)

###############

#3.

a = [1,2,3]
b = [4,5,6]

#method 1

c = []
n = 0
while n < len(a):
    c.append(a[n])
    n += 1
n = 0
while n < len(b):
    c.append(b[n])
    n += 1

#method 2

c = a[:] #this syntax means make a copy of the list. it's part of the advanced class
c.extend(b)  #extend adds all the elements in b to c

#method 3

c = a + b

#####################

#4.

a = [1,3,5,7]
b = [2,4,6,8]

result = []
n = 0
while n < len(a):
    result.append(a[n])
    result.append(b[n])
    n += 1

######################

#5.

#This method is formally known as 'selection sort'.
#It works by looping through the list and swapping the nth element
#with the lowest element in whatever's left. So the first swap puts
#the lowest element in first place; the second swap puts the next lowest
#element in second place, and so on.
#This is definitely using a few tricks I have not taught in
#the beginners class quite yet.
#But I don't think it's a bad thing to progressively encounter
#unfamiliar techniques.

m = [4,7,2,4,-45,8,90,4]

n = 0
while n < len(m) - 1:
	print("Remaining to be sorted: " + str(m[n:]))
	lowest = min(m[n:])
	print("The next lowest number is: " + str(lowest))
	location = m[n:].index(lowest)
	print("The next lowest number is found at index " + str(location) + \
              " within the remaining unsorted sequence.")
	temp = m[n]
	if temp == lowest:  #this prevents us swapping things that are identical
                n += 1      #by moving on directly to the next iteration of the loop
                continue
	m[n] = lowest
	m[n + location] = temp
	print("The list is now: " + str(m))
	n += 1
	if len(m[n:]) >= 2:
            ignoreThisVariable = input("Ready for the next step? Hit enter.")
            print()

print(m)

#######################

#6.

m = [ [1,2,3], [4,5,6], [7,8,9] ]

_sum = 0
n = 0
while n < len(m):
    x = 0
    while x < len(m[n]):
        _sum += m[n][x]
        x += 1
    n += 1

print(sum)

##########################

#7.

#This is a kind of tricky problem.
#It works by moving two indices around
#progressively and keeping track
#of the indices of the largest positive sequence
#found so far.

m = [1, 4, -2, 11, 5, -2, 7, -22, 14, 3, 1]

_sum = 0
start, end = 0, 0
largestSequenceStart = 0
largestSequenceEnd = 0

while end < len(m):

    if m[start] < 0:
        start += 1
        end += 1
        continue
    if m[end] >= 0:
        largestSequenceStart = start
        largestSequenceEnd = end
        end += 1
        continue
    elif m[end] < 0:
        largestSequenceStart = start
        largestSequenceEnd = end - 1
    start, end = end, end
    
print(m[largestSequenceStart:largestSequenceEnd+1])

#######################

#8.

#Remember, you can exit an infinite loop with Ctrl + C.

m = [1,2,3]

n = 0
while n < len(m):
    m.append(4)
    print(m)
    n += 1

########################

#9.

m = [1, 2, 2, 5, 3, 3, 7, 1]

found = []
n = 0
while n < len(m):
    if m[n] in found:
        del m[n]
        continue
    else:
        found.append(m[n])
        n += 1

#################

#10.
#I want clarify the meaning of this problem. Look at the following list:

#[1,2,1,2,3]

#The subsequence [1,2] is repeated consecutively....we have [1,2,1,2].
#Anytime a subsequence of length 2 is repeated side by side, I want to remove
#the repeat. Thtat's the goal of this problem. So for that list, we should end with:

#[1,2,3]

m = [3, 7, 34, 2, 1, 2, 1, 67, 3, 8, 3, 8]

n = 0
while n < len(m):
    if n < len(m) - 3:   #stop before we run out of things to compare
        if m[n] == m[n+2] and m[n+1] == m[n+3]:
            del m[n:n+2]   #deleting everything from m[n] up to but not
            continue        #including m[n+2]
    n += 1

print(m)

###########################

#11.

names = ["Harry", "David", "Liz", "Nahid", "George", "Kayla"]
ages = [12,45,23,67,2,13]

result = dict(zip(names, ages))

##########################

#12.

def analyzeDict(d):
    keyTypes, valueTypes = [], []
    for key, value in d.items():
        if str(type(key)) not in keyTypes:
            keyTypes.append(str(type(key)))
        if str(type(value)) not in valueTypes:
            valueTypes.append(str(type(value)))
    return (len(d), tuple(keyTypes), tuple(valueTypes))

################################

#13.

def doubleDuplicates(lst):
    lst = lst.copy()
    skipNext = False
    for i, e in enumerate(lst):
        print(i, e)
        if lst.count(e) > 1 and not skipNext:
            lst.insert(i, e)
            skipNext = True
        else:
            skipNext = False
    return lst

##############################

#14.

data_bank = {3454: 250}      #I initialized it with one sample account.
#data_bank = {}     #Comment the upper line and uncomment the other to start it as empty instead.

while True:
    action = input("Enter your PIN or type \"new\" for a new account. ")
    if action == "new":
        desired_PIN = int(input("Enter your desired PIN. "))
        while desired_PIN in data_bank:
            print("That PIN is taken. Try again.")
            desired_PIN = int(input("Enter your desired PIN. "))
        data_bank[desired_PIN] = int(input("How much would you like to deposit? "))
    else:
        PIN_attempt = int(action)
        if PIN_attempt in data_bank:
            amount_to_withdraw = input("How much would you like to withdraw? ")
            amount_to_withdraw = int(amount_to_withdraw)
            if amount_to_withdraw <= data_bank[PIN_attempt]:
                data_bank[PIN_attempt] -= amount_to_withdraw
                print("Disbursing $" + str(amount_to_withdraw))
                print("$" + str(data_bank[PIN_attempt] + " remaining.")
                print("Ending transaction.")
            else:
                print("Who are you kidding? You don't have that kind of money.")
        else:
            print("Invalid PIN.")


##################################

#15.


def uniqueInts(a, b, c, d):
    sets = [set(), set(), set(), set()]   #four empty sets....because {} is an empty dictionary
    for i, lst in enumerate((a, b, c, d)):  #read up on the enumerate function
        for el in lst:
            if lst.count(el) == 1:
                sets[i].add(el)
    a,b,c,d = sets
    return a ^ b ^ c ^ d #symmetric difference...another set operation.
                        #read up on the documentation!
                    #http://docs.python.org/3.3/library/stdtypes.html#set
                      
#example usage...should return {1,5,8,9}
print(uniqueInts([1,2,3,3],[4,5,6, 6],[7,8,9],[7,4,2]))

#####################################

#16.

def removeConsecutiveDuplicates(text):
    result = text.split(" ")
    previous = result[0]
    n = 0
    while n < len(result) - 1:
        if result[n][0] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" \
            and result[n] == result[n+1]:
            del result[n]
            continue
        n += 1
    return " ".join(result)
                      
#example usage
print(removeConsecutiveDuplicates("""Hey see see this text text has some errors.
Mr. Glue Glue's name is is going to be ignored, but but the rest will be fixed.""")
)

################################

#17. no way am I writing out this solution right now.
