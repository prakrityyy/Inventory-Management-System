def read_products(file_path="products.txt"):
    products = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                parts = line.strip().split(", ")
                if len(parts) == 5:
                    name, brand, quantity, cost_price, country = parts
                    products.append({
                        "name": name,
                        "brand": brand,
                        "quantity": int(quantity),
                        "cost_price": float(cost_price),
                        "country": country
                    })
    except FileNotFoundError:
        print("Product file not found.")
    return products
