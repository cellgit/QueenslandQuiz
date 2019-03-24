# """
#
# """

__author__ = ""
__date__ = ""


from destinations import Destinations



def main():
    # Task 1: Ask questions here

    continent = ""
    cost = ""
    crime = ""
    is_kid_friendly = True

    arrayM = []
    array_cost = []
    array_crime = []
    array_kids = []

    name = input("What is your name? ")
    print("Hello", name + "! ")
    # print("Which continent would you like to travel to?")
    print("  1) Asia")
    print("  2) Africa")
    print("  3) North America")
    print("  4) South America")
    print("  5) Europe")
    print("  6) Oceania")
    print("  7) Antarctica")

    print("> ")



    #-----------------------------------------------------------------


    print('Which continent would you like to travel to?:')

    choice = str(input())

    print(choice)

    if choice == '1':
        continent = "asia"
        print('choice1:' + choice)
        print('continent====:' + continent)
    elif choice == "2":
        continent = "africa"
    elif choice == "3":
        continent = "north america"
    elif choice == "4":
        continent = "south america"
    elif choice == "5":
        continent = "europe"
    elif choice == "6":
        continent = "oceania"
    elif choice == "7":
        continent = "antarctica"
    else:
        print('invailid')

    for destination in Destinations().get_all():
        if continent == destination.get_continent():
            arrayM.append(destination)

    # -----------------------------------------------------------------



    print("What is money to you?")
    print("  1) No object")
    print("  2) Spendable, so long as I get value from doing so")
    print("  3) Extremely important; I want to spend as little as possible")


    choice = str(input(""))

    if choice == '1':
        cost = "$"
    elif choice == "2":
        cost = "$$"
        print('cost2-2-2-2-2====:' + cost)
    elif choice == "3":
        cost = "$$$"
    else:
        print('invailid')

    for destination in arrayM:
        # print("destination=========:" + destination.get_name())
        if cost == "$":
            if destination.get_cost() == "$":
                array_cost.append(destination)
                print('cost$:-=-=-=-===---==--== ' + str(destination.get_name()))
        elif cost == "$$":
            print('cost2$$:-=-=-=-===---==--== ' + str(destination.get_cost()))
            if (destination.get_cost() == "$") or (destination.get_cost() == "$$"):
                array_cost.append(destination)
                print('cost$$:-=-=-=-===---==--== ' + str(destination.get_name()))
        elif cost == "$$$":
            if (destination.get_cost() == "$") or (destination.get_cost() == "$$") or (destination.get_cost() == "$$$"):
                array_cost.append(destination)
                print('cost$$$:-=-=-=-===---==--== ' + str(destination.get_name()))
        else:
            print('invailid')


#----------------------------------------------------------------------

    print("How much crime is acceptable when you travel?")
    print("1) low")
    print("2) average")
    print("3) high")

    choice = str(input(""))

    if choice == '1':
        crime = "low"
    elif choice == "2":
        crime = "average"
        print('cost2-2-2-2-2====:' + cost)
    elif choice == "3":
        crime = "high"
    else:
        print('invailid')


    for destination in array_cost:
        # print("destination=========:" + destination.get_name())
        if cost == "$":
            if destination.get_crime() == "low":
                array_crime.append(destination)
                print('crime$:-=-=-=-===---==--== ' + str(destination.get_name()))
        elif cost == "$$":
            print('cost2$$:-=-=-=-===---==--== ' + str(destination.get_cost()))
            if (destination.get_crime() == "low") or (destination.get_crime() == "average"):
                array_crime.append(destination)
                print('crime$$:-=-=-=-===---==--== ' + str(destination.get_name()))
        elif cost == "$$$":
            if (destination.get_crime() == "low") or (destination.get_crime() == "average") or (destination.get_crime() == "high"):
                array_crime.append(destination)
                print('crime$$$:-=-=-=-===---==--== ' + str(destination.get_name()))
        else:
            print('invailid')


#-----------------------------------------------------------------

    print("Will you be travelling with children?")
    print("  1) Yes")
    print("  2) No")
    choice = str(input(""))


    if choice == '1':
        is_kid_friendly = True
        print('is_kid_friendly--==-=-=-=:-=-=-=-===---==--== ' + str(is_kid_friendly))
    elif choice == "2":
        is_kid_friendly = False
    else:
        print('invailid')


    for destination in array_crime:
        if destination.is_kid_friendly() == is_kid_friendly:
            array_kids.append(destination)
            print('Result ======== :-=-=-=-===---==--== ' + str(destination.get_name()))



if __name__ == "__main__":
    main()
