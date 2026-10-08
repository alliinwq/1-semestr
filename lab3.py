products = [
    {"name": "Laptop", "price": 25000.00, "stock": 5},
    {"name": "Mouse", "price": 800.50, "stock": 10},
    {"name": "Keyboard", "price": 1500.00, "stock": 7},
    {"name": "Headphones", "price": 2200.75, "stock": 4}
]

cart = []


def show_catalog():
    print("\n Catalog ")

    for product in products:
        print(product["name"], "-", product["price"], "грн",
              "Left:", product["stock"])


def add_to_cart(name, quantity):
    for product in products:
        if product["name"] == name:
            if product["stock"] >= quantity:
                cart.append({
                    "name": product["name"],
                    "price": product["price"],
                    "quantity": quantity
                })
                print("Product added.")
                return
            else:
                print("Not enough products.")
                return

    print("Product not found.")


def show_cart():
    print("\n Cart ")

    if len(cart) == 0:
        print("Cart is empty.")
        return

    total = 0

    for product in cart:
        price = product["price"] * product["quantity"]
        total = total + price

        print(product["name"], "x", product["quantity"], "-", price, "грн")

    print("Total:", total, "грн")


def remove_from_cart(name):
    for product in cart:
        if product["name"] == name:
            cart.remove(product)
            print("Product removed.")
            return

    print("Product not found.")


def buy():
    if len(cart) == 0:
        print("Cart is empty.")
        return

    total = sum(map(lambda product:
                    product["price"] * product["quantity"], cart))

    for item in cart:
        for product in products:
            if product["name"] == item["name"]:
                product["stock"] = product["stock"] - item["quantity"]

    print("Purchase completed.")
    print("Total:", total, "грн")

    cart.clear()


def admin():
    login = input("Login: ")
    password = input("Password: ")

    if login == "admin" and password == "1234":
        print("\n Stock ")

        for product in products:
            print(product["name"], "-", product["stock"])
    else:
        print("Wrong login or password.")


def main():
    while True:
        print("\n SHOP ")
        print("1 - Catalog")
        print("2 - Add to cart")
        print("3 - Cart")
        print("4 - Remove from cart")
        print("5 - Buy")
        print("6 - Admin")
        print("0 - Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_catalog()

        elif choice == "2":
            name = input("Product name: ")
            quantity = int(input("Quantity: "))
            add_to_cart(name, quantity)

        elif choice == "3":
            show_cart()

        elif choice == "4":
            name = input("Product name: ")
            remove_from_cart(name)

        elif choice == "5":
            buy()

        elif choice == "6":
            admin()

        elif choice == "0":
            break

        else:
            print("Wrong choice.")

main()
