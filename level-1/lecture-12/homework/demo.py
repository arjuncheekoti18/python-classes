wanted = int(input("enter number of cookies: "))
jar = 50
given = 0
while given < wanted and jar > 0:
    given += 1
    jar -= 1
print("Cookies given:", given)
print("Cookies left:", jar)

welcomed_count = 0
while True:
    name = input("enter the names: ")
    if name == "close":
        break
        
    print("Welome", name)
    welcomed_count += 1
print("Guests welcomed:", welcomed_count)

num = int(input("enter your number: "))
digits = 0
while num > 0:
    num = num // 10
    digits += 1
print(digits)

target = int(input("Enter the bacteria count: "))
population = 1
hours = 0
while population < target:
    population *= 2
    hours += 1
print("Hours:", hours)
print("Population:", population)

num = int(input("enter the number: "))
digit_sum = 0
while num > 0:
    last_digit = num % 10
    digit_sum += last_digit
    num = num // 10
print("Digit sum:", digit_sum)