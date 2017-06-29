#groceryList = ["cake", "juice", "lunchables", "cookies", "avocado"]

#for item in groceryList:
    #print(item)
groceryList = []
add = True

while add == True:
    print("Do you want to add something to your grocery list?(y/n)")
    answer = input()
    if answer == "y":
        print("What would you like to add to your list?")
        item = input()
        groceryList.append(item)
        print("Here is your grocery list.")
        for item in groceryList:
            print(item)
         
    elif answer == "n":
        add == False
        print("Ok then, have a great day.")
        exit()

    else:
        print("Please choose the options given.")
