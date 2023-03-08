import random 

# variable To assign 

lower_text = "abcdefghijklmnopqrstuvwxyz"
upper_text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeric_text = "0123456789"
symbols_text = "{}[]<>?/\|-_+!@#$^&*()"

is_upper , is_lower , is_nums , is_symbols = True ,True ,True ,True
all = ""

if is_upper:
    all += upper_text
if is_lower:
    all += lower_text
if is_nums:
    all += numeric_text
if is_symbols:
    all += symbols_text

def getnum():
    while True:
        temp = input(" Enter The Password Length : ")
        if temp.isdigit():
            return int(temp)
        else:
            print(" Please Enter Number to generate the Password ")

def passgenarator(all):
    length = getnum() 
    password = "".join(random.sample(all,length))
    print(password)
    again = input(" Do You Want Another password ?  ")
    if again.lower() in ['yes','ý','i want']:
        passgenarator(all)

passgenarator(all)