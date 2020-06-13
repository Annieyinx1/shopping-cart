# shopping_cart.py
import os
import datetime
import pandas as pd

#csv_file_path = os.path.join(os.path.dirname(__file__),"data","products.csv")
csv_file_path = os.path.join("/Users/annieyin/Documents/GitHub/shopping-cart","data","products.csv")
products = pd.read_csv(csv_file_path)

# function to convert to USD
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

# TODO: write some Python code here to produce the desired output
# initialize variables
store_name = "Annie's"
store_website = "www.annies.com"
time = datetime.datetime.now()
format = '%Y-%m-%d %I:%M %p'
print(time.strftime(format))
checkout_item = []
subtotal = 0

id_list = products["id"].values

# initialize user input. Run while user input is not Done
user_input = 0
while (user_input != "Done"):
    # user input identifier
    user_input = input("Please input a product identifier: ")
    # exit loop if input Done
    if user_input == "Done":
        break
    # validaiton
    try:
        if float(user_input) not in id_list:
            print("Hey, are you sure that product identifier is correct? Please try again!")
        else:
            checkout_item.append(
                    {"name":products[products["id"]==float(user_input)]["name"].values[0],
                     "price":products[products["id"]==float(user_input)]["price"].values[0]})
            subtotal += products[products["id"]==float(user_input)]["price"].values[0]
    except ValueError:
        print("Hey, are you sure that product identifier is correct? Please try again!")

# calculate tax and total
tax = round(subtotal * 0.0875, 2)
total = subtotal + tax

# Print
print("---------------------------------")
print(store_name)
print(store_website)
print("---------------------------------")
print("CHECKOUT AT: " + time.strftime(format))
print("---------------------------------")
print("SELECTED PRODUCTS:")
for item in checkout_item:
    print("... " + item["name"] + " (" + to_usd(item["price"]) + ")")
print("---------------------------------")
print("SUBTOTAL: " + to_usd(subtotal))
print("TAX: " + to_usd(tax))
print("TOTAL: " + to_usd(total))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")
