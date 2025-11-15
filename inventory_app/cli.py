# cli.py
import requests

API_URL = "http://127.0.0.1:5000"

def list_items():
    r = requests.get(f"{API_URL}/inventory")
    for item in r.json():
        print(item)

def add_item():
    item_id = input("ID: ")
    name = input("Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    r = requests.post(f"{API_URL}/inventory", json={
        "id": item_id,
        "name": name,
        "quantity": quantity,
        "price": price
    })
    print(r.json())

def delete_item():
    item_id = input("ID to delete: ")
    r = requests.delete(f"{API_URL}/inventory/{item_id}")
    print(r.json())

def main():
    while True:
        print("\n1) List Items\n2) Add Item\n3) Delete Item\n4) Quit")
        choice = input("Choice: ")
        if choice == "1":
            list_items()
        elif choice == "2":
            add_item()
        elif choice == "3":
            delete_item()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
