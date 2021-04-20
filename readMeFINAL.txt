Section 1: Instructions

Using this program is extremely easy, as the program uses user inputs in order to direct a user to different functions.
The reason behind creating two lists is due to the fact that for starters, some of the functions being used will "edit" one
of the lists, and not edit the other. Secondly, some of the functions require a specific list in order to properly work.
Not following each of the instructions carefully may result in the program giving errors, or in the program breaking entirely.


Section 2: Binary Search

Binary Search in simple terms is a basic search algorithm. There are different types of Binary Search engines that work 
differently. Binary Search only works on integers, so any and all words, special characters, or decimals will not work. There
is also the fact that Binary Search can sometimes be innaccurate, or error prone. 

Recursive Binary Search takes a list, and splits it into sections. It uses user input to search for a digit in different groups.
This helps to find your number faster. The reason it is faster is because it sorts AND ranges each of the numbers. 

Iterative Binary Search also does this, however, there is a very split difference. While Recursive Binary Search loops until it
finds your number, iterative binary search does not. This saves your computer's storage, ensuring that your computer does 
not break the program. 


Section 3: Changes Made / Want to be made

Currently, the program is made to where it only works with a two lists. However, I want to increase the number of lists the
program can actually work with. To do this, I could add more choice variables to the program, allowing the user to choose lists,
and also add a way for a user to create a list. I also added a new change, which allows the user to wipe the data in a list...

NEW CHANGE!

def clearList():
    print("Time to wipe this list!")
    choose = input("Are you sure you want to clear your list?   Y/N   ")
    if choose.lower == "y":
        myList.clear()