print("~~~~~~~~~~~~Welcome to Foodsela~~~~~~~~~~~~")
print("-------------------MENU------------------------")
menu = {
    "Butter Chicken": 300,
    "Chicken Masala": 200,
    "Chicken Tandoori": 350,
    "Chicken Biryani": 250,
    "Mutton Masala": 380,
    "Mutton Biryani": 400,
}
cart = []
total = 0

# Display menu
for key, value in menu.items():
    print(f"{key:20}: ₹{value:.2f}")

# Order items
while True:
    food = input("\nSelect an item (type 'e' to exit): ").strip()
    if food.lower() == "e":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        print(f"{food} has been added to your cart.")
    else:
        print("Invalid selection. Please choose an item from the menu.")

# Print order summary
print("\n-------------------ORDER SUMMARY-------------------")
for i, food in enumerate(cart, start=1):
    total += menu[food]
    print(f"{i}. {food:20} - ₹{menu[food]:.2f}")

# Print final bill
print("\n-------------------BILL------------------------")
print(f"Total: ₹{total:.2f}")
