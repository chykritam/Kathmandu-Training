# 1. Here is our starting dictionary of groceries in US Dollars (USD)
usd_prices = {
    "butter": 4.00,
    "curd": 2.50,
    "bread": 2.9,
    "milk": 5.00,
    "apples": 2.00
}

# 2. The Exchange Rate
exchange_rate = 151.80

# 3. The Dictionary Comprehension (The Vending Machine!)
# "Give me the item, and the new price, for every item and price in the old list"
npr_prices = {item: price * exchange_rate for item, price in usd_prices.items()}


# Let's print it nicely to the screen!
print("Prices in Nepali Rupees:")
print(npr_prices)



# Here is our dictionary from the last step
npr_prices = {
    'butter': 532.0, 
    'curd': 332.5, 
    'bread': 399.0
}

npr_prices["eggs"] = 250.0

npr_prices["bread"] = 450.0



new_items = {
    "tea": 150.0,      
    "coffee": 800.0,    
    "butter": 600.0    
}

npr_prices.update(new_items)



print(npr_prices)


us_prices = {
    "butter": 4.00,
    "curd": 2.50,
    "bread": 2.9,
    "milk": 5.00,
    "apples": 2.00
}

nep_prices ={}
for k, v in us_prices.items():
    if v < 5:
        nep_prices.update({k:v})

print(nep_prices)




us_prices = {
    "butter": 4.00,
    "curd": 2.50,
    "bread": 2.9,
    "milk": 5.00,
    "apples": 2.00,
    "television": 700.00,
    "Smartphone": 1000.00,
    "charger": 20.00,
}

#

price_with_tax = {
    k: round(v * 151.81 * 1.13, 2) if v < 5 else round(v * 151.81 * 1.20, 2) 
    for k, v in us_prices.items()
}

print(price_with_tax)







