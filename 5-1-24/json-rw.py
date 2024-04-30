#!/usr/bin/env python3

import json
filename = "orders.json"

def create_order(order_id, product_id, product_name, price):
    return {"order_id": order_id, "name": product_name, "product_id": product_id, "price": price}
def print_order(order):
    print("\n--------ORDER BEGIN--------")
    print("Order ID: ", order["order_id"])
    print("Product ID: ", order["product_id"])
    print("Product name: ", order["name"])
    print("Price: ", order["price"])
    print("--------ORDER END----------\n")
def find_order_by_id(orders, order_id):
    for i in orders:
        if i["order_id"] == order_id:
            return i
    return -1


def write_to_file(filename, order):
    with open(filename, "w") as file:
        json.dump(order, file)
        file.truncate()
def read_from_file(filename):
    orders = []
    with open(filename, "r") as file:
        orders = json.load(file)
    return orders

def main():
    allorders = []
    choice = int(input("1. Load file\n2. Create new file\n"))

    if choice == 2:
        write_to_file(filename, allorders)
    elif choice != 1:
        print("Choose only 1 or 2")
        exit()

    print("We will use file:", filename)
    allorders = read_from_file(filename)

    choice = 0
    while choice != 3:
        choice = int(input("1. Search by order id\n2. Create new order\n3. Exit\n"))
        if choice == 1:
            choice = input("Enter order ID: ")
            order = find_order_by_id(allorders, choice)
            if order == -1:
                print("Order not found")
                continue
            print_order(order)
        elif choice == 2:
            order_id = input("Order ID: ")
            product_id = input("Product ID: ")
            name = input("Name of the product: ")
            price = input("Price of the product: ")
            allorders.append(create_order(order_id, product_id, name, price))
        elif choice != 3:
            print("Please pick only options 1-3")

    write_to_file(filename, allorders)

main()
