import csv


# import csv data as dicts in a list
def csv_to_dirc():
    stocklist.clear()
    with open('carlist.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stocklist.append(row)

# function to show the watchlist
def look_wishlist():
    k=1
    for i in wishlist: 
        print(k,":")
        k+=1
        for key,value in i.items():
            print(key,":",value,)
    return k


# function to filter number in range(Year,KM and Price)
def filter_number_range(word1,word2,criteria,list):
    global in_wishlist
    global m
    global flag1
    while flag1==True:
        a=input(word1)
        if a == 'skip':
            a=0
            pass
        elif a == 'quit':
            exit()

        elif a =='look':
            if wishlist==[]:
                print('\nWishlist is empty!')
                continue
            else:
                in_wishlist=1
                m =look_wishlist()
                flag1=0
            break

        elif str.isdigit(a)==False:
            if wishlist==[]:
                print("\nPlease enter a number! 'quit' to exit or 'skip' to pass")
            if wishlist !=[]:
                print("\nPlease enter a number! 'quit' to exit or 'skip' to pass or 'look' to wishlist")
            continue
        else:
            a=int(a)

        b=input(word2)
        if b == 'skip':
            b=9999999999999999999
            pass
        elif b == 'quit':
            exit()
        
        elif b =='look':
            if wishlist==[]:
                print('\nWishlist is empty!')
                continue
            else:
                in_wishlist=1
                m =look_wishlist()
                flag1=0
            break

        elif str.isdigit(b)==False:
            if wishlist==[]:
                print("\nPlease enter a number! 'quit' to exit or 'skip' to pass")
            if wishlist !=[]:
                print("\nPlease enter a number! 'quit' to exit or 'skip' to pass or 'look' to wishlist")
            continue
        else:
            b=int(b)

        i=[x for x in list if a <= int(x[criteria]) <= b]
        if i==[]:
            print("\nNo available car found.Please extend the range.")
            continue
        else:
            list.clear()
            list.extend(i)
        break


stocklist=[] 
wishlist=[]

print("G'day! Welcome to our 'Save Your Money' car seller!\nFollow the steps with us you will find your dream car!")

# filter the Brand
flag=1
while flag==True:
    in_wishlist=0

     # print the Brand in stocklist with no repetions
    while True:
        brand=[]
        if wishlist==[]:
            print("\nPlease select your car brand:\n('quit' to exit, or 'skip' to pass)")
            csv_to_dirc()
        if wishlist !=[]:
            print("\nPlease select your car brand:\n('quit' to exit, or 'skip' to pass, or 'look' to wishlist) ")
            csv_to_dirc()
        for item in stocklist:
            if item['Brand'] not in brand:
                print (item['Brand'])
                brand.append(item['Brand'])        
        a=input()
        if a == 'skip':
            pass
        elif a == 'quit':
            exit()
        elif a =='look':
            if wishlist ==[]:
                print("\nWishlist is empty!")
                continue
            else:
                in_wishlist=1
                m=look_wishlist()
            break
        elif a not in brand:
            print("\nPlease enter a valid option!")
            continue
        else:
            stocklist=[x for x in stocklist if a == x['Brand']]
        break
    
    while in_wishlist !=1:
        while True:
            flag1=1
            # won't give user guide to enter 'look' if wishlist is empty
            if wishlist==[]: 
                # filter the Year
                filter_number_range("\nPlease enter the min year of your car:\n('quit' to exit or 'skip' to pass)\n","\nPlease enter the max year of your car:\n('quit' to exit or 'skip' to pass)\n",'Year',stocklist)
                # filter the KM
                filter_number_range("\nPlease enter the min KM of your car:\n('quit' to exit or 'skip' to pass)\n","\nPlease enter the max KM of your car:\n('quit' to exit or 'skip' to pass)\n",'KM',stocklist)
                # filter the Price
                filter_number_range("\nPlease enter the min price of your car:\n('quit' to exit or 'skip' to pass)\n","\nPlease enter the max price of your car:\n('quit' to exit or 'skip' to pass)\n",'Price',stocklist)
                
            if wishlist !=[]:
                # filter the Year
                filter_number_range("\nPlease enter the min year of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n","\nPlease enter the max year of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n",'Year',stocklist)
                # filter the KM
                filter_number_range("\nPlease enter the min KM of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n","\nPlease enter the max KM of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n",'KM',stocklist)
                # filter the Price
                filter_number_range("\nPlease enter the min price of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n","\nPlease enter the max price of your car:\n('quit' to exit or 'skip' to pass or 'look' to wishlist)\n",'Price',stocklist)


            if flag1==True:
                print("\nWe have chosen the cars below for you!\n")
                n=1
                for i in stocklist: 
                    print(n,":")
                    n+=1
                    for key,value in i.items():
                        print(key,":",value,)
            
            if flag1==False:
                n=len(wishlist)+1
            break
        break
    #  user decide to save, choose or select again.
    while True:
        if wishlist==[]:
            answer=input("\nDo you want to:\n'save' or 'choose' any of the cars above?\n('quit' to exit, 'again' to choose car again)\n")
        if wishlist!=[]:
            answer=input("\nDo you want to:\n'save' or 'choose' any of the cars above?\n('quit' to exit, 'again' to choose car again, or 'look' to see wishlist\n")
        if answer=='save':
            for i in range(n-1):
                print(i+1,' ' ,end='')
            wishlist.append(stocklist[int(input("which one you wanna save?\n"))-1])
            wishlist=[dict(t) for t in set([tuple(d.items()) for d in wishlist])] # remove potential duplicates 
            break
        elif answer=='choose':
            flag=0      
            break
        elif answer=='look':
            if wishlist==[]:
                print("\nWishlist is empty!")
                continue
            if wishlist !=[]:
                in_wishlist=1
                m=look_wishlist()
                continue
        elif answer=='quit':
            exit()
        elif answer=='again':
            break
        else:
            print("\nPlease enter valid answer!")
    continue


if in_wishlist==False:   
    for i in range(n-1):
        print(i+1,' ' ,end='')
    car_chosen=stocklist[int(input("\nwhich one you wanna choose?"))-1]

if in_wishlist==True:
    for i in range(m-1):
        print(i+1,' ' ,end='')
    car_chosen=wishlist[int(input("\nwhich one you wanna choose?"))-1]


print(car_chosen)





