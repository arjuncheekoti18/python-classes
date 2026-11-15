def display_category():
    print("category: ")
    for i in range(len(categroy)):
        print(f"{i+1}. {category[i]}")
def display_items():
    print("animals: ")
    for animal in animals:
        print(f"{animal[0]} - {animal[1]}")
category = ("birds", "carnivores", "herbivores", "insects", "pets")
animals = []
options = """options:
1) add an animal
2)view the animals
3) exit the application
"""
while True:
    print("animal finder: ")
    print(options)
    choice = int(input("Enter your choice: ")