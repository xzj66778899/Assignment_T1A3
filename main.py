import csv

# import csv data as dicts in a list
stocklist=[]   
wishlist=[]
def csv_to_dirc():
    with open('carlist.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stocklist.append(row)

# function for filtering number in range(Year,KM and Price)
def filter_number_range(word1,word2,criteria,list):
    while True:
        a=input(word1)
        if a == 'skip':
            a=0
            pass
        elif a == 'quit':
            exit()
        elif str.isdigit(a)==False:
            print("Please enter a number! 'quit' to exit or 'skip' tp pass")
            continue
        else:
            a=int(a)

        b=input(word2)
        if b == 'skip':
            b=9999999999999999999
            pass
        elif b == 'quit':
            exit()
        elif str.isdigit(b)==False:
            print("Please enter a number! 'quit' to exit or 'skip' tp pass")
            continue
        else:
            b=int(b)

        i=[x for x in list if a <= int(x[criteria]) <= b]
        if i==[]:
            print("No available car found.Please extend the range.")
            continue
        else:
            list.clear()
            list.extend(i)
        break


print("G'day! Welcome to our 'Save Your Money' car seller!\nFollow the steps with us you will find your dream car!")

# filter the Brand
flag=1
while flag==True:
    print("Please select your car brand:\n(You can enter 'quit' to exit or 'skip' tp pass this criteria")
    # print the Brand in stocklist with no repetions
    csv_to_dirc()
    brand=[]
    while True:
        for item in stocklist:
            if item['Brand'] not in brand:
                print (item['Brand'])
                brand.append(item['Brand'])        
        a=input()
        if a == 'skip':
            pass
        elif a == 'quit':
            exit()
        elif a not in brand:
            print("Please enter a valid option! 'quit' to exit or 'skip' tp pass")
            continue
        else:
            stocklist=[x for x in stocklist if a == x['Brand']]
        break

    # filter the Year
    filter_number_range("Please enter the min year of your car:\n(You can enter 'quit' to exit or 'skip' tp pass this criteria)\n","Please enter the max year of your car:\n(You can enter 'quit' to exit or 'skip' tp pass this criteria)\n",'Year',stocklist)

    #  filter the KM
    filter_number_range("Please enter the min KM of your car:\n(You can enter 'quit' to exit or 'skip' tp pass this criteria)\n","Please enter the max KM of your car:\n(You can enter 'quit' to exit or 'skip' tp pass this criteria)\n",'KM',stocklist)

    #  filter the Price
    filter_number_range("Please enter the min price of your car:\n(You can enter 'quit' to exit or 'skip' tp pass this criteria)\n","Please enter the max price of your car:\n(You can enter 'quit' to exit or 'skip' tp pass this criteria)\n",'Price',stocklist)

    print("We have chosen the cars below for you!\n")
    # print(*stocklist, sep="\n")
    n=1
    for i in stocklist: 
        print(n,":")
        n+=1
        for key,value in i.items():
            print(key,":",value,)

# user decide to save, choose or select again.
    while True:
        answer=input("\nDo you want to:\n'save' or 'choose' any of the cars?\nor you can type 'quit' to exit, 'again' to choose car again,'look' to see wishlist\n")
        if answer=='save':
            wishlist.extend(stocklist)
            wishlist=[dict(t) for t in set([tuple(d.items()) for d in wishlist])] # remove potential duplicates 
            break
        elif answer=='choose':
            flag=0      
            break
        elif answer=='look':
            print(wishlist)
            continue
        elif answer=='quit':
            exit()
        elif answer=='again':
            break
        else:
            print("Please enter valid answer!")
    continue

number=[]



for i in range(n-1):
    print(i+1,' ' ,end='')
input("which one you wanna choose?")





print(wishlist)


 




