import csv
import datetime
import pandas
import loan_calculator

Interest_rate = 1.07

# import csv data as dicts in a list
def csv_to_dirc():
    stocklist.clear()
    with open('carlist.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stocklist.append(row)

# function to show the watchlist
def look_wishlist():
    k = 1
    for i in wishlist: 
        print(k,":")
        k += 1
        for key, value in i.items():
            print(key,":",value,)
    return k

# function to filter number in range(Year,KM and Price)
def filter_number_range(word1,word2,criteria,list):
    global in_wishlist
    global m
    global flag1
    while flag1:
        a = input(word1)
        if a == 'skip':
            a = 0
            pass
        elif a == 'quit':
            print("Sorry to see you leave, you can run this program again to choose a car for you.")
            exit()

        elif a =='look':
            if wishlist == []:
                print('\nWishlist is empty!')
                continue
            else:
                in_wishlist = 1
                m = look_wishlist()
                flag1 = 0
            break

        elif str.isdigit(a) == False:
            if wishlist == []:
                print("\nPlease enter a number! 'quit' to exit or 'skip' to pass")
            if wishlist != []:
                print("\nPlease enter a number! 'quit' to exit or 'skip' to pass or 'look' to wishlist")
            continue
        else:
            a = int(a)

        b = input(word2)
        if b == 'skip':
            b=9999999999999999999
            pass
        elif b == 'quit':
            print("Sorry to see you leave, you can run this program again to choose a car for you.")
            exit()
        
        elif b =='look':
            if wishlist == []:
                print('\nWishlist is empty!')
                continue
            else:
                in_wishlist = 1
                m = look_wishlist()
                flag1 = 0
            break

        elif str.isdigit(b) == False:
            if wishlist == []:
                print("\nPlease enter a number! 'quit' to exit or 'skip' to pass")
            if wishlist != []:
                print("\nPlease enter a number! 'quit' to exit or 'skip' to pass or 'look' to wishlist")
            continue
        else:
            b = int(b)

        i = [x for x in list if a <= int(x[criteria]) <= b]
        if i == []:
            print("\nNo available car found.Please extend the range.")
            continue
        else:
            list.clear()
            list.extend(i)
        break

stocklist = [] 
wishlist = []

print("G'day! Welcome to our 'Save Your Money' car seller!\nFollow the steps with us you will find your dream car!")
# filter the Brand
flag = 1
while flag:
    in_wishlist = 0
     # print the Brand in stocklist with no repetions
    while True:
        brand = []
        if wishlist == []:
            print("\nPlease select your car brand:\n('quit' to exit, or 'skip' to pass)")
            csv_to_dirc()
        if wishlist != []:
            print("\nPlease select your car brand:\n('quit' to exit, or 'skip' to pass, or 'look' to wishlist) ")
            csv_to_dirc()
        for item in stocklist:
            if item['Brand'] not in brand:
                print (item['Brand'])
                brand.append(item['Brand'])        
        a = input()
        if a == 'skip':
            pass
        elif a == 'quit':
            print("Sorry to see you leave, you can run this program again to choose a car for you.")
            exit()
        elif a =='look':
            if wishlist == []:
                print("\nWishlist is empty!")
                continue
            else:
                in_wishlist = 1
                m = look_wishlist()
                n = len(wishlist) + 1
            break
        elif a not in brand:
            print("\nPlease enter a valid option!")
            continue
        else:
            stocklist = [x for x in stocklist if a == x['Brand']]
        break
    
    while in_wishlist != 1:
        while True:
            flag1 = 1
            # won't give user guide to enter 'look' if wishlist is empty
            if wishlist == []: 
                # filter the Year
                filter_number_range("\nPlease enter the min year of your car:\n('quit' to exit or 'skip' to pass)\n",
                                    "\nPlease enter the max year of your car:\n('quit' to exit or 'skip' to pass)\n",
                                    'Year',stocklist)
                # filter the KM
                filter_number_range("\nPlease enter the min KM of your car:\n('quit' to exit or 'skip' to pass)\n",
                                    "\nPlease enter the max KM of your car:\n('quit' to exit or 'skip' to pass)\n",
                                    'KM',stocklist)
                # filter the Price
                filter_number_range("\nPlease enter the min price of your car:\n('quit' to exit or 'skip' to pass)\n",
                                    "\nPlease enter the max price of your car:\n('quit' to exit or 'skip' to pass)\n",
                                    'Price',stocklist)
                
            if wishlist != []:
                # filter the Year
                filter_number_range("\nPlease enter the min year of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n",
                                    "\nPlease enter the max year of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n",
                                    'Year',stocklist)
                # filter the KM
                filter_number_range("\nPlease enter the min KM of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n",
                                    "\nPlease enter the max KM of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n",
                                    'KM',stocklist)
                # filter the Price
                filter_number_range("\nPlease enter the min price of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n",
                                    "\nPlease enter the max price of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n",
                                    'Price',stocklist)

            if flag1:
                print("\nWe have selected the cars below for you!\n")
                n = 1
                for i in stocklist: 
                    print(n,":")
                    n += 1
                    for key,value in i.items():
                        print(key, ":", value,)
            
            if not flag1:
                n = len(wishlist)+1
            break
        break

    #  user decide to save, choose or select again.
    while True:
        if wishlist == []:
            answer = input("\nDo you want to:\n'save' or 'choose' any of the cars above?\n('quit' to exit, 'again' to choose car again)\n")
        if wishlist != []:
            answer = input("\nDo you want to:\n'save' or 'choose' any of the cars above?\n('quit' to exit, 'again' to choose car again, or 'look' to see wishlist)\n")
        if answer == 'save':
            for i in range(n-1):
                print(i + 1,' ' ,end = '')
            while True:    
                try:
                    wishlist.append(stocklist[int(input("which one you wanna save?\n"))-1])
                except:
                    print("\nPlese enter valid number!")
                    continue
                else:
                    wishlist = [dict(t) for t in set([tuple(d.items()) for d in wishlist])] # remove potential duplicates 
                break
            break
        elif answer == 'choose':
            flag = 0      
            break
        elif answer == 'look':
            if wishlist == []:
                print("\nWishlist is empty!")
                continue
            if wishlist != []:
                in_wishlist = 1
                m = look_wishlist()
                continue
        elif answer == 'quit':
            print("Sorry to see you leave, you can run this program again to choose a car for you.")
            exit()
        elif answer == 'again':
            break
        else:
            print("\nPlease enter valid answer!")
    continue

if in_wishlist == False:   
    for i in range(n - 1):
        print(i + 1,' ' ,end='')
    while True:
        try:
            car_chosen=stocklist[int(input("\nwhich one you wanna choose?\n"))-1]
        except:
            print("Please enter valid Number!")
            continue
        else:
            break
        
if in_wishlist == True:
    for i in range(m-1):
        print(i+1, ' ', end = '')
    while True:
        try:
            car_chosen = wishlist[int(input("\nwhich one you wanna choose?\n"))-1]
        except:
            print("\nPlease enter valid Number!")
            continue
        else:
            break


# print(car_chosen)
print("\nThanks for choosing the car!\n")
for k, v in car_chosen.items():
    print(k, ':', v)

if int(car_chosen['Discount']) != 0:
    print(f"\nAnd you have {car_chosen['Discount']}% of the product!")
    Price=int(car_chosen['Price'])*((100-int(car_chosen['Discount']))*0.01)

if int(car_chosen['Discount']) == 0:
    Price=int(car_chosen['Price'])

while True:
    offer_answer = input("\nWould you like to see our loan offer? 'Yes' or 'No'\n")
    if offer_answer == "Yes":
        flag3 = 1
        break
    if offer_answer == "No":
        flag3 = 0
        break
    else:
        print("Please enter 'Yes' or 'No'!\n")


# loan offer
now = datetime.datetime.now()
Date = now.strftime('20%y-%m-%d')

while flag3 == 1:
    flag4 = 1
    while flag4:
        term=input("Please enter the term(1-5 years) you want to have. ('quit' to exit)\n")
        if term == 'quit':
            print("Sorry to see you leave, you can run this program again to choose a car for you.")
            exit()
        try:
            1 <= int(term) <= 5 == True
        except:
            print("Please enter a valid number between 1 to 5 ! ('quit' to exit)")
            continue
        else:
            Term = int(term)
            print(f"Your monthly payment is ${round((loan_calculator.loan_summary(Price, Interest_rate, Term,Date)[1])/(Term*12))}!")
            offer_accept = input('Do you want to accept this offer? (y/n):')
            if offer_accept == "y":
                pass
                break
            if offer_accept == "n":
                print("You can choose another term")
                continue

    while True:
        complete = input("Please enter 'complete' to see the purchase order ('quit' to exit)\n")
        if complete == "complete":
            flag4 = 0
            break
        elif complete=="quit":
             print("Sorry to see you leave, you can run this program again to choose a car for you.")
             exit()
        else:
            print('Please enter valid value!')
            continue
    flag3 = "order_with_loan"

if flag3 == "order_with_loan":
    print("Here's your purchase order! Please find in TXT file!")
# output purchase order to txt with loan information
    with open('purchase_order.txt','w') as f:
        print('Pruchase Order\n\ncar details:',file = f)
        for k,v in car_chosen.items():
            print(k, ':', v, file = f)

        amount = loan_calculator.loan_summary(Price, Interest_rate, Term,Date)[1]
        interest = loan_calculator.loan_summary(Price, Interest_rate, Term,Date)[3]
        monthly_payment = round((loan_calculator.loan_summary(Price, Interest_rate, Term, Date)[1])/(12*Term), 2)

        print(f"\n\nloan amount:${amount}\nterm: {Term} years\ninterest:${interest}\ninterest rate:{Interest_rate}\nmonthly payment:${monthly_payment}\n\npurchase date:{Date}\nsales: online", file = f)
        
    print("\nThanks for chooing 'Save Your Money' car dealer!\nHave a nice day and looking forward to see you again!\n")

elif flag3 == 0:
    print("Here's your purchase order! Please find in TXT file!")
    # output purchase order to txt without loan information
    with open('purchase_order.txt','w') as f:
        print('Pruchase Order\n\ncar details:',file=f)
        for k,v in car_chosen.items():
            print(k,':',v,file=f)
        print(f"Price after discount: ${round(Price)}\n\npurchase date:\n{Date}\nsales:\nonline",file=f)
    print("\nThanks for chooing 'Save Your Money' car dealer!\nHave a nice day and looking forward to see you again!\n")


# update the car stocklist
# use pandas get the car list
csv_to_dirc()
car_list = pandas.read_csv('carlist.csv')

# find the sold car in carlist
index=stocklist.index(car_chosen)
car_sold = car_list.iloc[index:(index + 1)]

# copy it to sold list
car_sold.to_csv('car_sold.csv', mode = 'a', header = None, index = None)

# remove the car from carlist
car_list.drop([index]).to_csv('carlist.csv', index = None)
