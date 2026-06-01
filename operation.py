from write import generate_invoice, write_products

def display_products(products):
    print("\nAvailable Products:")
    for i, p in enumerate(products):
        selling_price = p['cost_price'] * 2
        print(f"{i+1}. {p['name']} ({p['brand']}) - Rs. {selling_price} | Stock: {p['quantity']} | Country: {p['country']}")

def process_sale(products):
    display_products(products)
    items = []
    total = 0
    name = input("\nEnter customer name: ")

    while True:
        choice = input("Enter product number to buy (or 'done' to finish): ")
        if choice.lower() == "done":
            break
        try:
            index = int(choice) - 1
            product = products[index]
            quantity = int(input(f"Enter quantity for {product['name']}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                continue
            total_items = quantity + (quantity // 3)
            if product["quantity"] >= total_items:
                product["quantity"] -= total_items
                cost = product["cost_price"] * 2 * quantity
                items.append(f"{product['name']} ({product['brand']}): {quantity} + {quantity // 3} free")
                total += cost
            else:
                print("Insufficient stock.")
        except (ValueError, IndexError):
            print("Invalid input.")

    if items:
        generate_invoice(name, items, total, "sale")
        write_products(products)

def restock(products):
    display_products(products)
    name = input("\nEnter supplier name: ")
    items = []
    total = 0

    while True:
        choice = input("Enter product number to restock (or 'done' to finish): ")
        if choice.lower() == "done":
            break
        try:
            index = int(choice) - 1
            product = products[index]
            quantity = int(input(f"Enter quantity to add for {product['name']}: "))
            new_price = float(input(f"Enter new cost price (or 0 to keep {product['cost_price']}): "))
            product["quantity"] += quantity
            if new_price > 0:
                product["cost_price"] = new_price
            cost = product["cost_price"] * quantity
            items.append(f"{product['name']} ({product['brand']}): +{quantity} @ Rs.{product['cost_price']}")
            total += cost
        except (ValueError, IndexError):
            print("Invalid input.")

    if items:
        generate_invoice(name, items, total, "restock")
        write_products(products)
