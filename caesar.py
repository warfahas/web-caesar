def alphabet_position(letter):
    if letter == letter.lower():
        return ord(letter) - 97
    elif letter == letter.upper():
        return ord(letter) - 65

def rotate_character(char, rot):
    if (ord(char) >= 97) and (ord(char) <= 122):
        return chr(97+(alphabet_position(char)+rot)%26)
    elif (ord(char) >= 65) and (ord(char) <= 90):
        return chr(65+(alphabet_position(char)+rot)%26)
    else:
        return char

def encrypt(text, rot):
    new_text = ""
    for char in text:
        new_text += rotate_character(char, rot)
    return new_text
