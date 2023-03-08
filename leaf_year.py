def is_check(temp):
    if str(temp).count('0') >= 2 and temp % 100 == 0:
        print(f" This Century Year {temp}")
        return True 
    return False

def getnum():
    while True:
        temp = input(" Enter the Year :  ")
        if temp.isdigit() and len(temp) < 5:
            return int(temp)
        else:
            print(" Please Enter the Year Cannot have String or Symbols ")

def main():
    year = getnum()
    year_Century = is_check(year)
    
    if year_Century:
        if (year%4 == 0) and (year%400 == 0) and (year%100 == 0):
            print(f" {year} is Leaf Year ")
        else:
            print(f" {year} is Not Leaf Year ")
    else:
        if year%4 == 0:
            print(f" {year} is Leaf Year ")
        else:
            print(f" {year} is Not Leaf Year ")
    again = input(" Do You Want Another password ?  ")
    if again.lower() in ['yes','y','i want']:
        main()

if __name__ == "__main__":
    main()