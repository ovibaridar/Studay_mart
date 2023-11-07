item_prices = {
    "item1": 10,
    "item2": 20,
    "item3": 30,
    "item4": 40
}

search_price = int(input("Enter the price you want to search for: "))

found_items = []

for item, price in item_prices.items():
    if price == search_price:
        found_items.append(item)

if found_items:
    print("Items with price", search_price, "are:")
    for item in found_items:
        print(item)
else:
    print("No items found with the specified price.")
