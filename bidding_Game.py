import random as r
from datetime import datetime 

def getrandom():
    for i in range(5):
        temp = r.randint(1,100)
    return temp

def get_info(user):
    print("")
    print(f" HELLO {user.title()} IT IS TRUSTABLE NETWORK OF BIDDING PLATFORM")
    print("")
    print(" Option are You Played ... ")
    print("")
    print("      1.  Find the Exact Number - get 10x Money ")
    print("")
    print("      2.  Find the Closet Range of Number - get 5x Money ")
    print("")
    print("      3.  Find the Specific Range of Number - get 2x Money ")
    print("")
    print("      4.  Exit ")
    print("")

def getname(active):
    if active:
        while True:
            temp = input(" Enter the Username :  ")
            if temp.isalpha():
                return temp
            else:
                print(" Username can't have Numberic Value or Symbols ")
    if not active:
        while True:
            temp = input(" Are You Ready to Start Game  :  ")
            if  temp.lower() in ["start","yes","y","ok"] :
                return True
            elif temp.lower() in ["no","not intersted","stop","n"]:
                return False
            else:
                print("Please says (Yes or No ) / (OK or Not Intersted ) / (Start or Stop) or ( Y or N)")
def getnumber(access):
    if access == 1:
        while True:
            temp = input(" Enter  Account Number :  ")
            if temp.isdigit():
                return int(temp)
            else:
                print(" Account Number can't have Characteric Value or Symbols ")        
                print(" Account Number must have 12 NUmbers So please Enter Valid Account Number ")

    elif access == 2:
        while True:
            temp = input(" Enter Phone-Number :  ")
            if temp.isdigit():
                return int(temp)
            else:
                print(" Phone-Number can't have Characteric Value or Symbols ")        
                print(" Phone-Number must have 10 NUmbers So please Enter Valid Phone-Number ")

    elif access == 3:
        while True:
            temp = input(" Enter Account Balance :  $ ")
            if temp.isdigit():
                return int(temp)
            else:
                print(" Account Balance can't have Characteric Value or Symbols ")        
    
    elif access == 4:
        while True:
            temp = input(" Enter Option-Number :  ")
            if temp.isdigit():
                return int(temp)
            else:
                print(" Option-Number can't have Characteric Value or Symbols ")        
    
    else:
        print(" Please Enter the Valid Function Number ")

def getans(access):
    if access:
        while True:
            temp = input(" Enter the Number -->>  ")
            if temp.isdigit() and 0 < int(temp) < 101 :
                return int(temp)
            else:
                print(" Please Enter Numbers and it is specific range extends ")
    if not access:
        while True:
            temp = input(" Enter Bidding Money-->>  ")
            if temp.isdigit() :
                return int(temp)
            else:
                print(" Please Money and Numbric Value ")

# random_number = getrandom()
# print(f"random number is {random_number} ")

if __name__ == "__main__":
    print(" ")
    print("              Welcome To Bidding Com ")
    print(" ")
    user = getname(True)
    print(" ")
    account_no = getnumber(1)
    print(" ")
    phone_no = getnumber(2)
    print(" ")
    account_balance = getnumber(3)
    print(" ")
    get_info(user)
    count = 0
    start = getname(False)
    while start: 
        print(" ")
        print(f" Account Balance : $ {account_balance:,}")
        print("")
        option_no = getnumber(4)

        if option_no == 4:
            start = False

        elif option_no == 1:
            bidding_money = getans(False)
            print(" Guess the Number ---->> ")
            print(" Your Chance total 3 ")
            if bidding_money <= account_balance :
                while  count < 3:
                    random_number = getrandom()
                    print(f" {random_number }")
                    answer = getans(True)
                    if answer == random_number:
                        print(" Your Got Right Answer ")
                        print(" so you Got 10x Money ")
                        count = 4
                        pay = True
                    else:
                        print(f" You Got Wrong Answer You {count+1} Chance Left ")
                        pay = False
                    count += 1
                if pay:
                    account_balance += (10 * bidding_money)
                    print(" Payment Credited... ")
                    count = 0
                if not pay:
                    account_balance -= bidding_money
                    count = 0
                    print(" Lost Money Payment Debited..")
                    
            else:
                print(" Please Enter the Money you Have ")
                print(f" Account Number {account_no} Balance $ {account_balance:,} so Enter Money you have ")

        elif option_no == 2:
            bidding_money = getans(False)
            print(" Guess the Number ---->> ")
            print(" Your Chance total 3 ")
            if bidding_money <= account_balance :
                while  count < 3:
                    random_number = getrandom()
                    print(f" {random_number }")
                    answer = getans(True)
                    if  random_number - 15 < answer < random_number + 15:
                        print(" Your Got Right Answer ")
                        print(" so you Got 5x Money ")
                        count = 4
                        pay = True
                    else:
                        print(f" You Got Wrong Answer You {count+1} Chance Left ")
                        pay = False
                    count += 1
                if pay:
                    account_balance += (5 * bidding_money)
                    print(" Payment Credited... ")
                    count = 0
                if not pay:
                    account_balance -= bidding_money
                    count = 0
                    print(" Lost Money Payment Debited..")
                    
            else:
                print(" Please Enter the Money you Have ")
                print(f" Account Number {account_no} Balance $ {account_balance:,} so Enter Money you have ")       

        elif option_no == 3:
            bidding_money = getans(False)
            print(" Guess the Number ---->> ")
            print(" Your Chance total 3 ")
            if bidding_money <= account_balance :
                while  count < 3:
                    random_number = getrandom()
                    print(f" {random_number }")
                    answer = getans(True)
                    if random_number - 5 < answer < random_number + 5:
                        print(" Your Got Right Answer ")
                        print(" so you Got 2x Money ")
                        count = 4
                        pay = True
                    else:
                        print(f" You Got Wrong Answer You {count+1} Chance Left ")
                        pay = False
                    count += 1
                if pay:
                    account_balance += (2 * bidding_money)
                    print(" Payment Credited... ")
                    count = 0
                if not pay:
                    account_balance -= bidding_money
                    count = 0
                    print(" Lost Money Payment Debited..")
                    
            else:
                print(" Please Enter the Money you Have ")
                print(f" Account Number {account_no} Balance $ {account_balance:,} so Enter Money you have ")

    else:
        print(" I am assured Hope to enjoy Game ")