food = input("Food name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print("--- RECEIPT ---")
print(f"Item: {food}")
print(f"Qty: {quantity}")
print(f"Total: ₦{total}")
print("---------------")
