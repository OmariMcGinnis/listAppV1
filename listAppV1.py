"""
Program Goals:
1. Get input fromt he user (at multiple stages)
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
6. Print contents of list
7. Quit Program    """)
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
                linearSearch
            elif choice == "6":
                print(myList)
            else:
                break
        except:
            print("You caught an error!")

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!  ")
    myList.append(int(newItem))

def addMany():
    print("We're gonna adda bunch of integers to your list!")
    numToAdd = input("How many numbers do you want to add   ")
    numRange = input("How high do you want the numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.appent(random.randit(0, int(numRange)))
    print("Your list is complete")

def indexValues():
    print("Curious about an index position? ME TOO!")
    indexPos = input("What index position would you like to check out?  ")
    print(myList[int(indexPos)])

def randomSearch():
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're going to search each item one by one!")
    searchItem = input("What are you looking for...?   ")
    for x in range(len(yList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))
    
#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
    mainProgram()
