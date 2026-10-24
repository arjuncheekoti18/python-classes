word=input("letter: ")
up_word=""
for lowercase_letter in word:
    match lowercase_letter: 
        case "a":
            up_word+=(".-")
        case "b":
            up_word+=("-...")
        case "c":
            up_word+=("-.-.")
        case "d":
            up_word+=("-..")
        case "e":
            up_word+=(".")
        case "f":
            up_word+=("..-.")
        case "g":
            up_word+=("--.")
        case "h":
            up_word+=("....")
        case "i":
            up_word+=("..")
        case "j":
            up_word+=(".---")
        case "k":
            up_word+=("-.-")
        case "l":
            up_word+=(".-..")
        case "m":
            up_word+=("--")
        case "n":
            up_word+=("-.")
        case "o":
            up_word+=("---")
        case "p":
            up_word+=(".--.")
        case "q":
            up_word+=("--.-")
        case "r":
            up_word+=(".-.")
        case "s":
            up_word+=("...")
        case "t":
            up_word+=("-")
        case "u":
            up_word+=("..-")
        case "v":
            up_word+=("...-")
        case "w":
            up_word+=(".--")
        case "x":
            up_word+=("-..-")
        case "y":
            up_word+=("-.--")
        case "z":
            up_word+=("--..")
        case _:
            up_word+=(lowercase_letter)
print(up_word)