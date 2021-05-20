"""
Program Goals:
1. Get input from the user (at multiple stages)
2. Convert some, but not all, inputs to ints from strings.
3. We need to provide the user with choices:
    a. Add more values to a list
    b. Return a value at a specific index position
4. Add search algorithms to pogram:
    a. Random Search
    b. Linear Search
    c. Binary Search (2 types)

"""
import random
myList = []
unique_list = []

"""
mainProgram() is as it states, the main program. It holds the choice variable
that takes user input, and determines what pathway it will take. It also has an
error catching print statement at the end for whenever a user prints a number that
is not made a choice.
"""

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number!")
            choice = input("""1. Add to a list or
2. Add a bunch of numbers to the list
3. Return a value at an index
4. Random Search
5. Linear Search
6. Sort List
7. Recursive Binary Search
8. Iterative Binary Search
9. Print List
10. Clear List
11. Quit Program    """)
            #add a way to catch bad user responses
            if choice == "1":
                addToList()
            elif choice == "2":
                addMany()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
               sortLists(myList)
            elif choice == "7":
                binSearch = input("What number are you looking for   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are you looking for   ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != 1:
                    print("Your number is a index position []".format(result))
                else:
                    print("Your number is not found in that list, bud!")
            elif choice == "9":
                printLists()
            elif choice == "10":
                clearList()
            else:
                break
        except:
            print("You caught an error!")
"""
addToList is another function that takes user input and adds it to a list
called "myList". It makes sure that the user can only input integers, or else
it will not work properly.
"""

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

"""
addMany() inputs multiple integers into myList at once. To do this, it gets a
range, as well as the amount of numbers that should be added to the list from
the user. It then gathers random integers ranging from the user's input, and
adds them all in. 
"""
def addMany():
    print("We're gonna add a bunch of integers to your list!")
    numToAdd = input("How many numbers do you want to add   ")
    numRange = input("How high do you want the numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randit(0, int(numRange)))
    print("Your list is complete")

"""
indexValues allows a user to find the index position of a certain integer in
myList. It uses a variable called "indexPos" that uses user input to determine
the number that the system should be searching for. Once found, it prints.
"""

def indexValues():
    print("Curious about an index position? ME TOO!")
    indexPos = input("What index position would you like to check out?  ")
    print(myList[int(indexPos)])

"""
randomSearch finds a random integer in myList, and prints it.
"""
def randomSearch():
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1)])

"""
linearSearch is a function that helps to find certan numbers one by one. It asks the user
what they want to find in myList, and then helps to create a range to look for that number at.
It then prints the number's index position, and the number of times it shows up in the list.
"""

def linearSearch():
    #try to add: 1) a count of how many times a number is present
    print("We're going to search each item one by one!")
    searchItem = input("What are you looking for...?   ")
    appCount = 0
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))
            appCount = appCount + 1
    print("You number appeared {} times in the list".format(appCount))

"""
recursiveBinarySearch essencially helps to find the index position of a number.
The way it does this is by splitting the list into sections to make finding your
number easier. If it does not find your number, it prints an error message.
"""

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Your number is at index position {}".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid -1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)

    else:
        print("Your number isn't here!")

"""
sortLists sorts each list and makes sure that there are no copies of specific numbers.
If it finds a copy, it ignores it, and only prints one of the mimicked number.
"""

def sortLists(myList):
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Do you want to see your list of unique, sorted items?  Y/N   ")
    if showMe.lower == "y":
        print(unique_list)

"""
printLists is a function that asks the user which list they want to see. Based on
the user's response, it will print the list. 
"""
def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see? Sorted or unsorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)
        else:
            print(myList)

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2

        if unique_list[mid] == x:
            print("Your number is at index position {}".format(mid))
            return mid
    
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)

        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)

    else:
        print("Your number isn't here!")

"""
iterativeBinarySearch is the same thing as recursiveBinarySearch, but the only difference is that it does not loop as much
as recursiveBinarySearch does.
"""
def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if unique_list[mid] < x:
            low = mid + 1

        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

"""
clearList does exactly what it's called, and erases myList completely.
"""

def clearList():
    print("Time to wipe this list!")
    choose = input("Are you sure you want to clear your list?   Y/N   ")
    if choose.lower == "y":
        myList.clear()



    
#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
    mainProgram()
