# First example from instructions
def print_every_other(x):
    while x >= 0:  # x is the loop variable
        print(x)
        x = x - 2
    # when indentation stops, while loop is over
    print("Done!")


# Activity 1: print_every_fifth
def print_every_fifth(x):
    """Counts down by 5 from starting number x until reaching 0 or below"""
    while x >= 0:
        print(x)
        x = x - 5  # subtract 5 each time
    print("Done!")


# Activity 2: Experimentation Comments
# We need TWO input() calls because of how while loops work with user input.
# First input happens BEFORE the loop starts - this gives user_num its first value
# so Python knows what to compare in the while condition. If we skip this, Python
# crashes because it doesn't know what user_num is.
# Second input happens INSIDE the loop - this gets a new number each time through.
# Without this inside input, we'd be stuck checking the same number forever and
# the loop would never end (infinite loop!).

# Second example from instructions
def square_user_nums():
    """Squares numbers from user until they type a negative number to stop"""
    # Get first number before loop starts
    user_inp = input("Enter the next number (negative to quit): ")
    user_num = int(user_inp)

    while user_num >= 0:  # keep going while number is positive
        print(user_num, "squared is", user_num ** 2)
        # Get next number inside loop
        user_inp = input("Enter the next number (negative to quit): ")
        user_num = int(user_inp)


# Third example from instructions
def sum_to_n(topNum):
    """
    Takes in a number and computes and returns the sum of the numbers
    from zero to the input number.
    """
    curr_val = 0  # starts at 0 and counts up
    total = 0  # keeps track of running sum

    while curr_val < topNum:
        total = total + curr_val  # add current number to our sum
        curr_val = curr_val + 1  # move to next number

    return total


# Activity 3: add_user_nums
def add_user_nums():
    """Keeps adding numbers until user enters 0, then returns the total"""
    sum_of_nums = 0  # this will hold our total
    user_num = int(input("Enter a number (0 to quit): "))  # get first number

    while user_num != 0:  # continue until they type 0
        sum_of_nums = sum_of_nums + user_num  # add it to running total
        user_num = int(input("Enter a number (0 to quit): "))  # ask for next number

    return sum_of_nums  # send back the final sum


# Fourth example from instructions
def nextWord(text):
    """
    Takes in a string of text and builds and returns a new string
    that is the next "word" in the text. In other words, the next
    sequence of characters up to a space, tab, or newline.
    """
    wordStr = ""  # build word here letter by letter
    i = 0
    for ch in text:  # go through each character
        if ch in " \t\n":  # found whitespace - word is done
            break  # stop the loop
        else:
            wordStr = wordStr + ch  # add letter to word
    return wordStr


# Activity 4: square_user_nums2
def square_user_nums2():
    """Better version - uses break instead of reading input twice"""
    while True:  # infinite loop - we'll break out when ready
        user_inp = input("Enter the next number (negative to quit): ")
        user_num = int(user_inp)

        if user_num < 0:  # time to stop?
            break  # yes - jump out of loop

        # if we got here, number was positive so square it
        print(user_num, "squared is", user_num ** 2)