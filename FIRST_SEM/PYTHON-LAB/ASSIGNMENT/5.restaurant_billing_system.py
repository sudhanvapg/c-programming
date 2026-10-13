# Question 5 - Restaurant Billing System
menu = {
    "paneer chilly": 180,
    "meals": 50,
    "gobi": 90,
    "coffee": 30,
    "dosa": 50,
    "veg kurma": 100,
    "veg roll": 120 }
def get_price(item):
     return menu.get(item.lower(), 0)
def item_cost(item, qty):
    price = get_price(item)
    return price * qty
def calculate_gst(amount, rate=0.05):
    return amount * rate
def generate_bill(subtotal, discount_percent=0):
    discount = subtotal * discount_percent / 100
    discounted_amount = subtotal - discount
    gst = calculate_gst(discounted_amount)
    final_total = discounted_amount + gst
    return discount, gst, final_total
def split_bill(total, people):
    each_person = int(total) // people
    remaining = int(total) % people
    return each_person, remaining
def take_order():
    persons = int(input("Enter number of people: "))
    subtotal = 0
    for person in range(1, persons + 1):
        print("\nPerson", person)
        item_count = int(input("How many different items? "))
        for item_no in range(1, item_count + 1):
            print("Item", item_no)
            item = input("Enter item name: ").lower()
            quantity = int(input("Enter quantity: "))
            cost = item_cost(item, quantity)
            if cost == 0:
                print("Item not available in the menu.")
            else:
                subtotal += cost
    return persons, subtotal

def display_bill(subtotal, discount, gst, total, each, remaining):
    print("\n========== FINAL BILL ==========")
    print("Subtotal       :", round(subtotal, 2))
    print("Discount       :", round(discount, 2))
    print("GST            :", round(gst, 2))
    print("Final Total    :", round(total, 2))
    print("Each Person Pays:", each)
    print("Rupees Left    :", remaining)
    print("================================")
# Main Program
print("========== RESTAURANT MENU ==========")
for item, price in menu.items():
    print(f"{item.title():15} : Rs.{price}")
people, subtotal = take_order()
discount, gst, total = generate_bill(subtotal, 10)
each, remaining = split_bill(total, people)
display_bill(subtotal, discount, gst, total, each, remaining)