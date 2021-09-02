import json
from datetime import datetime

jFile = open("inventory.json", "r+")
prod_dict = json.load(jFile)
prod_list = {}
prod_selected = {}


def show_products():
    k = 1
    for i in prod_dict:
        prod = prod_dict[i]
        if prod["quantity"] != 0:
            print("\n"+str(k)+". " + prod["name"] + " - Rs." + str(prod["price"]) + "\n*Qns- " + str(prod["quantity"]))
            prod_list[k] = i
            k += 1


def buy_confirm():
    total_sum = 0
    for i in prod_selected:
        p_s = prod_selected[i]
        p_n = prod_dict[i]
        total_sum += prod_selected[i]["total_price"]
        print("\n "+p_n["name"] + " ( Qn= " + str(p_s['Qn']) + ") ( Total Price= " + str(p_s['total_price']) + " )")
    print("\n Total Amount = " + str(total_sum))


show_products()
no = ""

while no != '-1':
    no = input("\n Enter Product No , press -1 to cancel, press B to confirm : ")
    if no == '-1':
        break
    elif no == "B":
        if prod_selected == {}:
            break
        else:
            buy_confirm()
            break
    else:
        qn = int(input(" Qn: "))
        if prod_dict[prod_list[int(no)]]["quantity"] >= qn:
            prod_selected[prod_list[int(no)]] = {"Qn": qn, "total_price": prod_dict[prod_list[int(no)]]["price"] * qn}
            prod_dict[prod_list[int(no)]]["quantity"] -= qn
        else:
            print(" Quantity Exceeded the stock!!")

print("\n Thank you! \\(*.*)/ Visit Again !! ~")

jFile.seek(0)
json.dump(prod_dict, jFile)
jFile.close()

SFile = open("productSales.json", 'w')
json.dump(prod_selected, SFile)
date = datetime.now().strftime("\n %d/%m/%Y %H:%M:%S")
print(date)
