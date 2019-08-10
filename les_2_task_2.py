import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('orders.json', 'w') as data:
        data.write(json.dumps(dict_to_json, indent=4))


item, quantity, price, buyer, date = input().split()
write_order_to_json(item, quantity, price, buyer, date)
