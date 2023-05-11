# Git repo link
https://github.com/xzj66778899/Assignment_T1A3.gi
<br>
<br>

# Code style guide
‘Style Guide for Python Code’ https://peps.python.org/pep-0008/  
<br>

# APP features:
## Feature 1:
As a sales, you can edit the carlist in the CSV file to let the buyers to choose.
Now there're 50 cars in the stock. Import the carlist in CSV format. 

The result is to output a purchase order with information such as 'car details', 'loan details' and 'sales date' in TXT format, and the stock list will automatically be updated when an order is completed.  

The sold car details will be put in a car sold list.  
<br>
## Feature 2:
As a buyer, you can choose or skip any criteria within 'Type', 'Brand', 'Year', 'KM' and 'Price' to find the right car.  

When cars have been selected, you can either save it to built-in wishlist, select again, or choose it to the next step. 
<br>

## Feature 3:
After a car has been 'chosen' by the buyer, system will ask the user whether to consider a loan offer.   
If the buyer has interest, system will show a monthly payment according to the term chosen. Buyer can accept offer or reject the offer.  
<br>
## General feature:
In any circumstance if wrong letters are input, APP will ask buyer to input again.  
Users can enter 'quit' to exit the program at most of the input points.  
User can call wishlist out at most of the input points.
<br>
# Implementation plan:
### 1. Lists of objects:
#### 1.1 feature 1
##### checklist : 
1. make car list
2. user requirements input
3. match the requirements to the car list
4. ask user whether select again or not
5. type 'quit' to exit
6. make a wishlist function  

#### 1.2. feature 2
##### checklist : 
1. find and import a third-party loan calculator package
2. collaborate package with user input
3. get ideal return from the package
4. input error handling
5. test the whole 'loan offer' function  

#### 1.3. feature 3
##### checklist :
1. find a way to output the purchase order
2. increase the carlist volume
3. update the carlist when a purchase order created
4. output the sold car into a sold list
5. test the I/O function  

#### 1.4. general feature: 
Make sure error handling is complete. User has enough freedom to reselect, exit and choose the saved car.  

#### 1.5.review and test: 
Make at least two tests for the application.  
<br>        

### 2. Scope statement:
This is a car sale terminal application that helps buyers to select a car in the stock then create a purchase order.  

System will update the stock list automatically when a purchase order created.  

Sales can edit the stock list manually to add/delete cars.  

Launch due date is 14/05/2023  
<br>
### 3. Task due dates:
feature 1: 05/05/2023  
feature 2: 08/05/2023  
feature 3: 09/05/2023  
general feature: 09/05/2023  
review and test: 12/05/2023  
launch: 14/05/2023  
    
Please refer to this Trello link to find more schedule control information: https://trello.com/b/wQstnYxO/assignmentt1a3







