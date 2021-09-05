import json
from datetime import datetime

jFile = open("inventory.json", "r+")
prod_dict = json.load(jFile)
prod_list = {}
prod_selected = {}
prod_sales = {}
prod_outOfStock = {}


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
        p_n = prod_dict[i[:-17]]
        total_sum += prod_selected[i]["total_price"]
        print("\n "+p_n["name"] + " ( Qn= " + str(p_s['Qn']) + ") ( Total Price= " + str(p_s['total_price']) + " )")
    print("\n Total Amount = " + str(total_sum))


def sales():
    bill = {}
    for i in prod_selected:
        pID = i[:-17]
        bill[pID] = prod_selected[i]
        bill[pID].update({"name": prod_dict[pID]["name"]})
    return bill


def commit_purchase():
    jFile.seek(0)
    json.dump(prod_dict, jFile, indent=4)

    pSFile = open("sales.json", 'r+')
    prod_sales[datetime.now().strftime(" %d/%m/%Y %H:%M:%S")] = sales()
    prod_sales.update(json.load(pSFile))
    pSFile.seek(0)
    json.dump(prod_sales, pSFile, indent=4)
    pSFile.close()

    SFile = open("productSales.json", 'r+')
    prod_selected.update(json.load(SFile))
    SFile.seek(0)
    json.dump(prod_selected, SFile, indent=4)
    SFile.close()

    OFile = open("outOfStock.json", 'r+')
    prod_outOfStock.update(json.load(OFile))
    OFile.seek(0)
    json.dump(prod_outOfStock, OFile, indent=4)
    OFile.close()


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
            commit_purchase()
            break
    else:
        qn = int(input(" Qn: "))
        if prod_dict[prod_list[int(no)]]["quantity"] >= qn:
            dt = datetime.now().strftime(" %d/%m/%Y %H:%M")
            prod_selected[prod_list[int(no)] + dt] = {"Qn": qn, "total_price": prod_dict[prod_list[int(no)]]["price"] * qn}
            prod_dict[prod_list[int(no)]]["quantity"] -= qn
            if prod_dict[prod_list[int(no)]]["quantity"] == 0:
                prod_sel = prod_dict[prod_list[int(no)]]
                timeDetail = datetime.now().strftime(" %d/%m/%Y %H:%M:%S")
                prod_outOfStock[prod_list[int(no)] + dt] = {"name": prod_sel["name"], "price": prod_sel["price"],
                                                            "TimeDetail": timeDetail}
        else:
            print(" Quantity Exceeded the stock!!")

print("\n Thank you! \\(*.*)/ Visit Again !! ~")
jFile.close()

date = datetime.now().strftime("\n %d/%m/%Y %H:%M:%S")
print(date)
