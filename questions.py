brand_question=("\nFirstly may I ask what brand you want to buy? Please enter one of the following(enter 'quit' to exit, 'show' to show results):\n'BMW'\n'Toyota'\n'Benz\n'Mazda'\n'RAM'\n'Ford'\n'Volkswagen'\n'Holden'\n")
type_question = ("What type do you like? Please enter one of the following(enter 'quit' to exit, 'show' to show results):\n'Sedan'\n'SUV'\n'Ute'\n")
year_question1=("What year of the car do you want to buy? Please enter the min and max year(enter 'quit' to exit, 'show' to show results).\nmin:\n")
year_question2=("(enter 'quit' to exit, 'show' to show results)\nmax:\n")
km_question1=("How many KM of the car do you want to buy? Please enter the min and max KM(enter 'quit' to exit, 'show' to show results).\nmin:\n")
km_question2=("(enter 'quit' to exit, 'show' to show results)\nmax:\n")
price_question1=("What price do you prefer? Please enter the min and max price.(enter 'quit' to exit, 'show' to show results)\nmin:\n")
price_question2=("(enter 'quit' to exit, 'show' to show results)\nmax:\n")

def get_type():
    input(str(type_question))

def get_brand():
    input(str(brand_question))

def get_year_min():
    input(str(year_question1))

def get_year_max():
    input(str(year_question2))

def get_km_min():
    input(str(km_question1))

def get_km_max():
    input(str(km_question2))

def get_price_min():
    input(str(price_question1))

def get_price_max():
    input(str(price_question2))