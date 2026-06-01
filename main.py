from read import read_products
from operation import process_sale, restock, display_products

def main():
    products = read_products()
 
    while True:
        print("\n--- WeCare Product Sales System ---")
        print("1. Display Products")
        print("2. Process Sale")
        print("3. Restock Products")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            display_products(products)
        elif choice == "2":
            process_sale(products)
        elif choice == "3":
            restock(products)
        elif choice == "4":
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
