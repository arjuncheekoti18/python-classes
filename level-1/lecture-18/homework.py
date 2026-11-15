#this is the task you gave to me at the end of class
def generate_bill(items):
    print("Your Order:")
    for item, price in items.items():
        print(f"{item.capitalize()}: ${price}")
    print("=" * 13)
    print(f"Total: ${sum(items.values())}")
order = {
    "pizza": 20,
    "burger": 15,
    "coke": 10
}
generate_bill(order)

#homework 1-5:
username = input()
level = int(input())
game = input()
player = {
    "username": username,
    "level": level,
    "game": game
}
player["level"] += 1
player["rank"] = "Bronze"
for key, value in player.items():
    print(f"{key}: {value}")

votes = input().split()
counts = {}
for topping in votes:
counts[topping] = counts.get(topping, 0) + 1
for topping, count in counts.items():
print(f"{topping}: {count}")

menu = {"tea": 20, "coffee": 30, "juice": 40}
remove_item = input()
new_item = input()
new_price = int(input())
removed_price = menu.pop(remove_item, None)
if removed_price is not None:
    print(f"Removed {remove_item} (was {removed_price})")
else:
    print(f"{remove_item} is not on the menu")
menu.setdefault(new_item, new_price)
print(menu)

def scorecard(**goals):
    total = 0
    for player, score in goals.items():
        print(f"{player.title()} scored {score}")
        total += score
    print(f"Team total: {total}")
scorecard(ravi=2, sita=1, kiran=0)

register = dict.fromkeys(
    ["Asha", "Bala", "Chitra", "Dev"],
    "Absent"
)
arrivals = input().split()
for name in arrivals:
    if name in register:
        register[name] = "Present"
    else:
        print(f"{name} is not in this class")
print(register)