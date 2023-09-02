alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

while not direction.lower() == "encode" and not direction.lower() == "decode":
     direction = input("you must select either encode or decode\n")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    text = [*text]
    newAlphabet = alphabet.copy()
    for _ in range(shift):
        first_letter = newAlphabet.pop(0)
        newAlphabet.append(first_letter)

    for position in range(len(text)):
        if not text[position] == " ":
            letter_index = alphabet.index(text[position]) 
            text[position] = newAlphabet[letter_index]
 
    encodedText = ''.join(text)
    print(encodedText)

def decrypt(text,shit):
    text = [*text]
    newAlphabet = alphabet.copy()
    for _ in range(shift):
        first_letter = newAlphabet.pop(0)
        newAlphabet.append(first_letter)

    for position in range(len(text)):
        if not text[position] == " ":
            letter_index = newAlphabet.index(text[position]) 
            text[position] = alphabet[letter_index]
 
    dencodedText = ''.join(text)
    print(dencodedText)

def caesar(text, shift, direction):
    if direction == 'encode':
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    
caesar(text, shift, direction)
