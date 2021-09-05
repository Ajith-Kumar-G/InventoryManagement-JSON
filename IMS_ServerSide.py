import json
no_of_Products = int(input("Enter the Number of Products to save: "))
prod = {}


def get_product_details(n):
    for j in range(n):
        print("\n Enter the Product details :\n ")
        product_id = int(input("ID:"))
        product_name = input("Name:")
        product_price = float(input("Price:"))
        product_quantity = int(input("Quantity:"))
        prod[product_id] = {"name": product_name, "price": product_price, "quantity": product_quantity}


def write_product():
    # first Time use
    """jFile = open("inventory.json", 'w')
    jFile.write(json.dumps(prod))
    jFile.close()"""

    # continued  use
    jFile = open("inventory.json", 'r+')
    old_prod = json.load(jFile)

    # print(old_prod)
    for p in prod:
        if str(p) not in old_prod:
            old_prod[p] = prod[p]
        else:
            prod[p]["quantity"] += old_prod[str(p)]["quantity"]
            old_prod.update({str(p): prod[p]})
    jFile.seek(0)
    json.dump(old_prod, jFile)
    jFile.close()


def check_product():
    # checking it
    jFile = open("inventory.json", 'r')
    print(jFile.read())


get_product_details(no_of_Products)
write_product()
check_product()




