import csv

# import csv data as dicts in a list
stocklist=[]   
def csv_to_dirc():
    with open('carlist.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stocklist.append(row)
csv_to_dirc()

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
            b=9999
            pass
        elif b == 'quit':
            exit()
        elif str.isdigit(b)==False:
            print("Please enter a number! 'quit' to exit or 'skip' tp pass")
            continue
        else:
            b=int(b)

        list=[x for x in list if a <= int(x[criteria]) <= b]
        if list==[]:
            print("No available car found.Please extend the range.")
            continue
        break


print("G'day! Welcome to our 'Save Your Money' car seller!\nFollow the steps with us you will find your dream car!")

# filter the Brand
print("Please select your car brand:\n(You can enter 'quit' to exit or 'skip' tp pass this criteria")
# print the Brand in stocklist with no repetions
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
print(*stocklist, sep="\n")




    # if brand == 'skip':
    #     pass
    # elif brand == 'quit':
    #     exit()
    # else:
    #     stocklist=[x for x in stocklist if type == x['Type']]



    # year_min=int(questions.get_year_min())
    # year_max=int(questions.get_year_max())
    # car=[x for x in stocklist if year_min<=int('Year')<=int(year_max)]



        

    # km_min=int(questions.get_km_min())
    # km_max=int(questions.get_km_max())
    # price_min=questions.get_price_min()
    # price_max=questions.get_price_max()





    # car=[x for x in stocklist if km_min <=int(x['KM']) <= km_max]

    # print(car)

