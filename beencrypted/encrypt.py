table = {
    "a": "According",
    "b": "To",
    "c": "All",
    "d": "Known",
    "e": "Laws",
    "f": "Of",
    "g": "Aviation",
    "h": "There",
    "i": "Is",
    "j": "No",
    "k": "Way",
    "l": "A",
    "m": "Bee",
    "n": "Should",
    "o": "Be",
    "p": "Able",
    "q": "Fly",
    "r": "Its",
    "s": "Wings",
    "t": "Are",
    "u": "Too",
    "v": "Small",
    "w": "Get",
    "x": "Fat",
    "y": "Little",
    "x": "Body",
    "1": "Off",
    "2": "The",
    "3": "Ground",
    "4": "Course",
    "5": "Flies",
    "6": "Anyway",
    "7": "Because",
    "8": "Bees",
    "9": "Do",
    "0": "Not",
    " ": "Care",
    ".": "What",
    ",": "Humans",
    "-": "Think",
    ":": "Posible",
    ";": "Yellow",
    "/": "Black"
}


def encrypt(string):
    try:
        lowered = string.lower()
        listed = [*lowered]
    except:
        raise Exception('The input was not valid')

    encrypted = ""
    for i in listed:
        if i in table:
            encrypted += table[i]
        else:
            encrypted += "Barry"
    return encrypted
