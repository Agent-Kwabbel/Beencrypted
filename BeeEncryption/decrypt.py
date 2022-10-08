table = {
 'According': 'a',
 'To': 'b',
 'All': 'c',
 'Known': 'd',
 'Laws': 'e',
 'Of': 'f',
 'Aviation': 'g',
 'There': 'h',
 'Is': 'i',
 'No': 'j',
 'Way': 'k',
 'A': 'l',
 'Bee': 'm',
 'Should': 'n',
 'Be': 'o',
 'Able': 'p',
 'Fly': 'q',
 'Its': 'r',
 'Wings': 's',
 'Are': 't',
 'Too': 'u',
 'Small': 'v',
 'Get': 'w',
 'Body': 'x',
 'Little': 'y',
 'Off': '1',
 'The': '2',
 'Ground': '3',
 'Course': '4',
 'Flies': '5',
 'Anyway': '6',
 'Because': '7',
 'Bees': '8',
 'Do': '9',
 'Not': '0',
 'Care': ' ',
 'What': '.',
 'Humans': ',',
 'Think': '-',
 'Posible': ':',
 'Yellow': ';',
 'Black': '/'
}

capitals = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decrypt(string):
    try:
        listed = [*string]
    except:
        raise Exception('The input was not valid')

    current_word = ""
    decrypted = ""
    first = True
    for i in listed:
        if i not in capitals:
            current_word += i
        else:
            if current_word in table:
                if current_word == "Barry":
                    break
                else:
                    decrypted += table[current_word]
                    current_word = ""
                    current_word += i
            else:
                if first:
                    current_word += i
                    first = False
                else:
                    raise Exception('The input was not a Beencrypted string')
    return decrypted
