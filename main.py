import os
from datetime import datetime
import platform
import sys

purchasefile = open("purchase.txt","a")
purchasefile.truncate(0)

billfile = open("bill.txt","a")
billfile.truncate(0)

incomefile = open("income.txt","a")
incomefile.truncate(0)

format = "%m/%d/%Y"

name = ""
date = ""
amount = ""
choice = ""

while(choice != "4"):
    print("Hello! Welcome to Leo's Budgeting App\n\nIf you would like to enter a purchase into your budget, enter 1\n\nIf you would like to enter a bill into your budget, enter 2\n\nIf you would like to enter a income into your budget, enter 3\n\nIf you would like to close the program enter 4\n\n")
    choice = input("Your Choice: ")

    while(choice != "1" and choice != "2" and choice != "3" and choice != "4"):
        print("\nPlease enter a number between 1 and 4 to make your selection (1 - purchases) (2 - bills) (3 - income) (4 - quit)\n")
        choice = input("Your Choice: ")

    if(choice == "4"):
        quit()

    while(name != "0" and date != "0" and amount != "0" ):
        if(choice == "1"):
            if(platform.system() == "Windows"):
                os.system('cls')
            else:
                os.system('clear')
            print("This page allows you to enter a purchase into your budget so you can keep track of how much money you have spent\n\nEnter 0 at any time to return to home screen\n\n")
            name = input("Enter purchase name: ")
            if (name == "0"):
                name = ""
                break
            print("\n")
            date = input("Enter purchase date (MM/DD/YYYY) (Must type slashes): ")
            if (date == "0"):
                date = ""
                break
            res = True
            try:
                res = bool(datetime.strptime(date, format))
            except ValueError:
                res = False
            while(res == False):
                print("Date entered incorrectly. Please enter date as MM/DD/YYYY")
                date = input("Enter purchase date (MM/DD/YYYY): ")
                if (date == "0"):
                    break
                try:
                    res = bool(datetime.strptime(date, format))
                except ValueError:
                    res = False
            if (date == "0"):
                date = ""
                break
            print("\n")
            amount = input("Enter purchase amount: ")
            if (amount == "0"):
                amount = ""
                break
            print("\n")

            confirm = input("(WARNING confirming the entry will add it to your information and can not be undone!)\nConfirm entry (Yes/No): ")
            while(confirm != "Yes" and confirm != "No" and confirm != "yes" and confirm != "no" and confirm != "Y" and confirm != "N" and confirm != "y" and confirm !="n"):
                print("please enter either Yes or No to confirming your entry")
                confirm = input("(WARNING confirming the entry will add it to your information and can not be undone!)\nConfirm entry (Yes/No): ")
            if(confirm == "Yes" or confirm == "yes" or confirm == "Y" or confirm == "y"):
                purchasefile.write(name + ", " + date + ", " + amount)

        elif(choice == "2"):
            if(platform.system() == "Windows"):
                os.system('cls')
            else:
                os.system('clear')
            print("This page allows you to enter a bill into your budget so you can keep track of how much money you have to spend on bills\n\nEnter 0 at any time to return to home screen\n\n")
            name = input("Enter bill name: ")
            if (name == "0"):
                name = ""
                break
            print("\n")
            date = input("Enter bill date (MM/DD/YYYY) (Must type slashes): ")
            if (date == "0"):
                date = ""
                break
            res = True
            try:
                res = bool(datetime.strptime(date, format))
            except ValueError:
                res = False
            while(res == False):
                print("Date entered incorrectly. Please enter date as MM/DD/YYYY")
                date = input("Enter bill date (MM/DD/YYYY): ")
                if (date == "0"):
                    break
                try:
                    res = bool(datetime.strptime(date, format))
                except ValueError:
                    res = False
            if (date == "0"):
                    date = ""
                    break
            print("\n")
            amount = input("Enter bill amount: ")
            if(amount == "0"):
                amount = ""
                break
            print("\n")

            confirm = input("(WARNING confirming the entry will add it to your information and can not be undone!)\nConfirm entry (Yes/No): ")
            while(confirm != "Yes" and confirm != "No" and confirm != "yes" and confirm != "no" and confirm != "Y" and confirm != "N" and confirm != "y" and confirm !="n"):
                print("please enter either Yes or No to confirming your entry")
                confirm = input("(WARNING confirming the entry will add it to your information and can not be undone!)\nConfirm entry (Yes/No): ")
            if(confirm == "Yes" or confirm == "yes" or confirm == "Y" or confirm == "y"):
                billfile.write(name + ", " + date + ", " + amount)

        elif(choice == "3"):
            if(platform.system() == "Windows"):
                os.system('cls')
            else:
                os.system('clear')
            print("This page allows you to enter income into your budget so you can keep track of how much money you have earned\n\nEnter 0 at any time to return to home screen\n\n")
            name = input("Enter income name: ")
            if (name == "0"):
                name = ""
                break
            print("\n")
            date = input("Enter income date (MM/DD/YYYY) (Must type slashes): ")
            if (date == "0"):
                date = ""
                break
            res = True
            try:
                res = bool(datetime.strptime(date, format))
            except ValueError:
                res = False
            while(res == False):
                print("Date entered incorrectly. Please enter date as MM/DD/YYYY")
                date = input("Enter income date (MM/DD/YYYY): ")
                if (date == "0"):
                    break
                try:
                    res = bool(datetime.strptime(date, format))
                except ValueError:
                    res = False
            if (date == "0"):
                date = ""
                break
            print("\n")
            amount = input("Enter income amount: ")
            if (amount == "0"):
                amount = ""
                break
            print("\n")
            
            confirm = input("(WARNING confirming the entry will add it to your information and can not be undone!)\nConfirm entry (Yes/No): ")
            while(confirm != "Yes" and confirm != "No" and confirm != "yes" and confirm != "no" and confirm != "Y" and confirm != "N" and confirm != "y" and confirm !="n"):
                print("\nPlease enter either Yes or No to confirm your entry")
                confirm = input("(WARNING confirming the entry will add it to your information and can not be undone!)\nConfirm entry (Yes/No): ")
            if(confirm == "Yes" or confirm == "yes" or confirm == "Y" or confirm == "y"):
                incomefile.write(name + ", " + date + ", " + amount)
        elif(choice == "4"):
            end = True
