import csv

def csv2dirc():
    with open('carlist.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            carlist.append(row)
         

carlist=[]      
csv2dirc()
print(carlist)