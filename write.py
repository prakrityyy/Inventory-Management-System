from datetime import datetime
// This module contains functions to write product data and generate invoices for the WeCare Product Sales System.
def write_products(products, file_path="products.txt"):
    with open(file_path, "w") as file:
        for p in products:
            line = f"{p['name']}, {p['brand']}, {p['quantity']}, {p['cost_price']}, {p['country']}\n"
            file.write(line)

def generate_invoice(customer, items, total, invoice_type="sale"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{invoice_type}_invoice_{customer}_{timestamp}.txt"
    with open(filename, "w") as f:
        f.write(f"Invoice Type: {invoice_type.capitalize()}\n")
        f.write(f"Customer/Supplier: {customer}\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("Items:\n")
        for item in items:
            f.write(f"{item}\n")
        f.write(f"\nTotal: Rs. {total:.2f}\n")
