# List: Products-oda list (Basket)
products = ['Laptop', 'Mouse', 'Keyboard']

# Dictionary: Price-oda list (Ledger)
prices = {'Laptop': 1500, 'Mouse': 50, 'Keyboard': 100, 'Monitor': 500}

# Enna kanakkidu? Mouse-oda vilai enna?
print("Mouse-oda vilai:", prices['Mouse'])
print("Monitor-oda vilai:", prices['Monitor'])

# Ellathaiyum kootuvom
total_price = prices['Laptop'] + prices['Mouse'] + prices['Keyboard'] + prices['Monitor']
print("Ellathoda total vilai:", total_price)

# Oru customer-oda bill amount
bill_amount = 2150

# Logic: Bill 500-kku mela iruntha "Discounted" nu sollu, illana "No Discount" nu sollu
if bill_amount > 500:
    print("Super! Ungalukku 10% Discount kidaikum.")
else:
    print("Sorry, Discount illai.")

bill_amount = 200
if bill_amount > 500:
    print("Super! Ungalukku 10% Discount kidaiku.")
else:
    print("Sorry, Discount illai.")

# Namoda basket (List)
products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor']

# Loop: "Oru vadiyaa pōyi ellathaiyum eduthu kaattu"
for item in products:
    print("Kadai-la irukkura item:", item)

prices = [ 1500,  50,  100,  500]
for item in prices:
    print("Kadai-la irukkura itemda Prices:", item)