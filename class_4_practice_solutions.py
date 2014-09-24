# Class 5 Practice Problem Solutions

# 1

def findSubSequences(L, num):
    start = 0
    end = 0
    result = 0
    while start < len(L):
        while end < len(L):
            if sum(L[start:end+1]) == num:
                result += 1
                #print(start, end) #uncomment to see where matches are
            end += 1
        start += 1
        end = start
    return result

#print(findSubSequences([4, -5, 0, 3, 2, 2, 4, -2], 2))

#2

def findSubstringLocations(string, sub):
    result = []
    for i in range(len(string)):
        if string[i:i+len(sub)] == sub:
            result.append(i)
    return result

#print(findSubstringLocations("cough thought ouchouou", "ou"))

#3

#Easy to find online, "insertion sort pseudocode"
#To be honest, in retrospect this "problem" is a little dull.
#But it's good to have seen/heard of a well-known algorithm.

#4

def countToZero(n):
    print(n)
    if n > 0:
        countToZero(n-1)
    if n < 0:
        countToZero(n+1)

#countToZero(4)

#5

def tripleAndBack(n, original=None, backwards=False):
    if not original:   #None is treated as False in truth testing
        tripleAndBack(n, n)
    elif n >= original:
        print(n)
        if backwards or n == original * 3:
            tripleAndBack(n - 1, original, True)
        else:
            tripleAndBack(n+1, original, False)
            
#tripleAndBack(5)
            
# Explanation: I use default arguments to keep track of where
# we started-- 'original' is the first value of n. When the
# function is called with 1 argument (n), it simply calls itself
# over again with 'original' set to the same value. That way
# the user of the function doesn't have to worry about these
# little implementation details...they can just call it with one
# argument. After that, the function keeps moving up by 1 until
# it hits original*3, at which time it activates the backwards flag
# (which defaults to False) and starts moving in the other direction,
# and stops after n == original.

# Note that the above code is not compatible with negative ints...
# that would require a couple small tweaks.

#6

def join(strings, sep):
    result = ""
    for s in strings[:-1]:
        result += s + sep
    result += string[-1]
    return result

#join(["tarmac", "airfoil", "combustible", "genesis"], "XXX")

#I didn't include the last list element in the for loop because
#I didn't want to put the separator at the end of the result.
#So I append it separately afterwards.

#7

def findSubstringLocations(string, sub, i=0, result=None):
    if not result: #beginner note: why not set it to [] as default? This is discussed in Advanced Class 9.
        result = []
    if string[i:i+len(sub)] == sub:
            result.append(i)
    if i == len(string):
        return result
    return findSubstringLocations(string, sub, i+1, result)

#print(findSubstringLocations("cough thought ouchouou", "ou"))

#8

#See note from #3.

#9

#There are much cleverer methods of doing this using bitwise operators,
#which are for working with binary numbers, and which we have not learned,
#and which we are not going to learn.

def binary(n):
    if type(n) != int or n < 0:
        print("Bad argument: ", n)
        return
    result = ""
    highest = 0
    while n % 2**highest < n: #find the highest power of 2 by which n is divisible
        highest += 1
    highest -= 1 #the loop goes 1 too far
    while highest >= 0:  # we start whittling 'highest' down as we build the binary represenation
        if n % 2**highest < n:
            result += '1'
            n -= 2**highest
        else:
            result += '0'
        highest -= 1
    return result

#print(binary(110430))

#10

def anagrams(word):
    if len(word) <=1:
        return [word]
    result = []
    for a in anagrams(word[1:]):
        for i in range(len(word)):
            result.append( a[:i] + word[0] + a[i:] )
    return result

#print(anagrams("cat"))

#11

#Doesn't this scheme just make so much sense? OOP is wonderful.
#By dividing functionality into neat little methods, the whole
#thing becomes extremely intuitive and easy to write.

#random module for creating cardNumbers....think of them more like account numbers.
#This ATM can create new accounts on the fly, even creating new debit cards to go with them. AMAZING!
import random

class Account:
    def __init__(self, cardNum, PIN, balance):
        self.cardNum = cardNum
        self.PIN = PIN
        self.balance = balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            print("Insufficient funds.")
            return False
    def deposit(self, amount):
        self.balance += amount

class ATM:
    def __init__(self):
        self.accounts = {}
    def createAccount(self, cardNum, PIN, balance):
        newAccount = Account(cardNum, PIN, balance)
        self.accounts[cardNum] = newAccount
    def doesAccountExist(self, cardNum):
        return cardNum in self.accounts
    def isPinValid(self, cardNum, PIN):
        return self.accounts[cardNum].PIN == PIN
    def openNewAccount(self):
        cardNum = ""
        for n in range(8):
            cardNum += (str(random.randint(0,9)))
        #technically it's possible to generate the same card twice, so we should check for that,
        #but the probability of that actually happening is....very small.
        print("Your card number is " + cardNum + ".")
        user_PIN = input("Choose a 4-digit PIN: ")
        initial_deposit = int(input("How much would you like to initially deposit? "))
        self.createAccount(cardNum, user_PIN, initial_deposit)
    def withdraw(self):
        cardNum = input("Swipe your card. ") #unfortunately you'll have to actually type the card number in
        if self.doesAccountExist(cardNum):
            PIN_attempt = input("Enter your PIN: ")
            if self.isPinValid(cardNum, PIN_attempt):
                amount = int(input("Enter the amount to withdraw: "))
                if self.accounts[cardNum].withdraw(amount):
                    print("New balance is $" + str(self.accounts[cardNum].balance) + ".")
                print("Transaction complete.")
            else:
                print("Invalid PIN.")
        else:
            print("Account does not exist.")
    def deposit(self):
        cardNum = input("Swipe your card. ") #unfortunately you'll have to actually type the card number in
        if self.doesAccountExist(cardNum):
            PIN_attempt = input("Enter your PIN: ")
            if self.isPinValid(cardNum, PIN_attempt):
                amount = int(input("Enter checks/bills. ")) #unfortunately you'll have to actually type in how much you're depositing.
                self.accounts[cardNum].deposit(amount)
                print("New balance is $" + str(self.accounts[cardNum].balance) + ".")
                print("Transaction complete.")
            else:
                print("Invalid PIN.")
        else:
            print("Account does not exist.")
    def run(self):
        while True:
            user_input = int(input("\nEnter 1 to create a new account.\nEnter 2 to make a withdrawal.\nEnter 3 to make a deposit.\nEnter 4 to end transaction loop.\n"))
            print('\n')
            if user_input == 1:
                self.openNewAccount()
            elif user_input == 2:
                self.withdraw()
            elif user_input == 3:
                self.deposit()
            elif user_input == 4:
                break
            else:
                print("Invalid entry.")


##atm = ATM()
##atm.run()

#12

#I'm using a dirty trick in the lookup methods on the ContactManager class.
#If you read carefully, you'll see I'm using something you've probably never seen
#which almost looks like an indentation error. It's called a 'for else' loop.
#The for loop behaves exactly like you'd expect, and the else clause only executes
#if the break statement is never executed. That's all there is to it.
#If the loop ends via the break statement, the else clause is ignored.
#But if the loop ends on its own normally, then the else clause is executed.
#You don't have to write it this way of course...I just found it convenient.

class Contact:
    def __init__(self, name, number, address):
        self.name = name
        self.number = number
        self.address = address
    def __str__(self):
        return "Name: " + self.name + "\nNumber: " + self.number + "\nAddress: " + self.address + "\n"

class ContactManager:
    def __init__(self):
        self.contacts = []
    def addContact(name, number="", address=""):
        self.contacts.append(Contact(name, number, address))
    def lookupByName(self, name):
        for c in self.contacts:
            if c.name == name:
                print(c)
                break
        else:
            print("Name not found in contacts.")
    def lookupByPhone(self, number):
        for c in self.contacts:
            if c.number == number:
                print(c)
                break
        else:
            print("Number not found in contacts.")
    def lookupByAddress(self, address):
        for c in self.contacts:
            if c.address == address:
                print(c)
                break
        else:
            print("Address not found in contacts.")
    def displayAll(self):
        for c in self.contacts:
            print(c)
    
#13

#see separate upload cards.py

#14

#These method definitions should all be added to the Deck class definition.

def __add__(self, d):
    return Deck(self.cards + d.cards)

def __len__(self):
    return len(self.cards)

def __lt__(self, d):
    return len(self.cards) < len(d.cards)

def __gt__(self, d):
    return len(self.cards) > len(d.cards)

def __eq__(self, d):
    return len(self.cards) == len(d.cards)

# Random fact:
# If you create two lists such as [1,2] and [3,4,4],
# and you compare them DIRECTLY via < or > or >= or <=, it will compare their lengths
# automatically, without you needing to use the len() function.
# This will not work with == (or !=), which actually compares the CONTENTS of the list. The two lists
# would have to hold the exact same numbers to be equal.
# So that's an option for __lt__ and __gt__, just omitting the len() calls and comparing directly.
# Probably the best way to do it, honestly....clear and readable, makes sense, less code. Win!

# That same functionality works with strings, too, now that I think of it...but that's not as intuitive.
# Better to use len() there, in my opinion.




                 
