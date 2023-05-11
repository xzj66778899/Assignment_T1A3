
import pytest
import loan_calculator

# print_brand test: 
# This is a test for the function that can print the brand name without duplication, when given of a lists of cars in dict_in_list format.

def print_brand(stocklist):
    brand=[]
    for item in stocklist:
        if item['Brand'] not in brand:
            print (item['Brand'])
            brand.append(item['Brand'])
    return brand

def test_print_brand():
    assert  print_brand([{'Brand':'a','Year':'b'},
           {'Brand':'a','Year':'b'},
           {'Brand':'c','Year':'d'},
           {'Brand':'c','Year':'d'},
           {'Brand':'e','Year':'f'},
           {'Brand':'e','Year':'f'},
           {'Brand':'g','Year':'h'},
           {'Brand':'g','Year':'h'}
           ])==[
               'a','c','e','g'
               ]
    

# look wishlist test
# whenever user input'look', this function will be activated. 
# Use 'pytest -s' to test the printed results are correct.

def look_wishlist(wishlist):
    k=1
    for i in wishlist: 
        print(k,":")
        k+=1
        for key,value in i.items():
            print(key,":",value,)
    return k
    
def test_look_wishlist():
    assert look_wishlist(({'A':'a','B':'b','C':'c'},{'D':'d','E':'e','F':'f'},{'G':'g','H':'h',"I":'i'}))==4