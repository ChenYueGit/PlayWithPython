textCard1 = "\n\t1 11 21 31 41 51\n"\
            "\t3 13 23 33 43 53\n"\
            "\t5 15 25 35 45 55\n"\
            "\t7 17 27 37 47 57\n"\
            "\t9 19 29 39 49 59\n"
textCard2 = "\n\t2 11 22 31 42 51\n"\
            "\t3 14 23 34 43 54\n"\
            "\t6 15 26 35 46 55\n"\
            "\t7 18 27 38 47 58\n"\
            "\t10 19 30 39 50 59\n"
textCard3 = "\n\t4 13 22 31 44 53\n"\
            "\t5 14 23 36 45 54\n"\
            "\t6 15 28 37 46 55\n"\
            "\t7 20 29 38 47 60\n"\
            "\t12 21 30 39 52 *\n"
textCard4 = "\n\t8 13 26 31 44 57\n"\
            "\t9 14 27 40 45 58\n"\
            "\t10 15 28 41 46 59\n"\
            "\t11 24 29 42 47 60\n"\
            "\t12 25 30 43 56 *\n"
textCard5 = "\n\t16 21 26 31 52 57\n"\
            "\t17 22 27 48 53 58\n"\
            "\t18 23 28 49 54 59\n"\
            "\t19 24 29 50 55 60\n"\
            "\t20 25 30 51 56 *\n"
textCard6 = "\n\t32 37 42 47 52 57\n"\
            "\t33 38 43 48 53 58\n"\
            "\t34 39 44 49 54 59\n"\
            "\t35 40 45 50 55 60\n"\
            "\t36 41 46 51 56 *\n"
print("\n==================================")            

print("\nPlease pick a number from 1 to 60 and keep it in your mind. Don't tell anyone.\n"\
      "You will read 6 cards. Press Y if the number in your mind is on the card.\n")

if(input("Are you reday? Y/N  ")=="y"):
    print(textCard1)
    if (input("Is the number on this card? Y/N ") == "y"):
        b1 = 1
    else:
        b1 = 0
    print(textCard2)
    if (input("Is the number on this card? Y/N ") == "y"):
        b2 = 1
    else:
        b2 = 0
    print(textCard3)
    if (input("Is the number on this card? Y/N ") == "y"):
        b3 = 1
    else:
        b3 = 0
    print(textCard4)
    if (input("Is the number on this card? Y/N ") == "y"):
        b4 = 1
    else:
        b4 = 0
    print(textCard5)
    if (input("Is the number on this card? Y/N ") == "y"):
        b5 = 1
    else:
        b5 = 0
    print(textCard6)
    if (input("Is the number on this card? Y/N ") == "y"):
        b6 = 1
    else:
        b6 = 0
        
    nNumberInMind = 1*b1 + 2*b2 + 4*b3 + 8*b4 + 16*b5 + 32*b6
    print("\nThe Number in Your Mind is : \n")
    print("\t"+str(nNumberInMind)+"\n")
else:
    pass
