import random
import math
# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    final_string = "" #string that will be returned later
    for x in plaintext:
        #can't have the letter represent an ascii value that goes past the alphabet, so that is why use of modulus is necessary
        value_int = ord(x) + offset
        if value_int > ord('Z'):
            #at this point value_int represents the remainder if there is one, so you need to add it to the starting point which is A, because it doesnt start at 0
            value_int = value_int - ord('Z') - 1 + ord('A')
        final_string += chr(value_int)
    return final_string 
    

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset): 
    final_string = "" #string that will be returned later
    for x in ciphertext:
        value_int = ord(x) - offset
        #if the new number goes before the alphabet, then you want it to be in the alphabet so add 26
        if value_int < ord('A'):
            value_int += 26
        final_string += chr(value_int)
    return final_string

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
    #string that represents the length adjusted key
    encrypted_result = ""
    key = ""
    if len(keyword) < len(plaintext):
        repeats = len(plaintext) // len(keyword)
        key = keyword * repeats
        #in case the length of the plaintext is not a multiple of the length of the keyword
        if len(key) != len(plaintext):
            difference = len(plaintext) - len(key)
            #adding the part that is remaining
            key += keyword[0:difference]
    if len(keyword) > len(plaintext):
        difference = len(keyword) - len(plaintext)
        key += keyword[0:difference - 1]
    if len(keyword) == len(plaintext):
        key = keyword   
    x = 0
    while x < len(plaintext) and x < len(key):
        #number that corresponds to encrypted character
        char_value = ord(plaintext[x])
        key_char_value = ord(key[x]) - ord('A')
        char_value += key_char_value
        if char_value > ord('Z'):
            char_value = char_value - ord('Z') - 1 + ord('A') 
        encrypted_result += chr(char_value)      
        x += 1 
    return encrypted_result

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    decrypted_result = ""
    key = ""
    if len(keyword) < len(ciphertext):
        repeats = len(ciphertext) // len(keyword)
        key = keyword * repeats
        #in case the length of the plaintext is not a multiple of the length of the keyword
        if len(key) != len(ciphertext):
            difference = len(ciphertext) - len(key)
            #adding the part that is remaining
            key += keyword[0:difference]
    if len(keyword) > len(ciphertext):
        difference = len(keyword) - len(ciphertext)
        key += keyword[0:difference - 1]
    if len(keyword) == len(ciphertext):
        key = keyword   
    x = 0
    while x < len(ciphertext) and x < len(key):
        #number that corresponds to encrypted character
        char_value = ord(ciphertext[x])
        key_char_value = ord(key[x]) - ord('A')
        char_value -= key_char_value
        if char_value < ord('A'):
            char_value = char_value + ord('Z') + 1 - ord('A') 
        decrypted_result += chr(char_value)      
        x += 1 
    return decrypted_result

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
def generate_private_key(n=8):
    #creates a tuple of n elements by having a for loop
    W = [random.randint(1,35), 0, 0, 0, 0, 0, 0, 0]
    total = W[0]
    for x in range(len(W)):
        #adds to the tuple a random integer such that the sequence stays superincreasing
        W[x] = random.randint(total + 1, 2 * total)
        #finds total of tuple
        total += W[x]
    Q = random.randint(total + 1, 2 * total)
    r = 0
    while math.gcd(r,Q) != 1:
        #keeps looping until r and q are coprime
        r = random.randint(2, Q-1)
    private_key = (tuple(W), Q, r)
    return private_key

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: B - a length-n tuple of integers
def create_public_key(private_key):
    W, Q, r = private_key
    B = []
    for x in W:
        #turns B into the public key  
        B.append(r *  x % Q)
    return tuple(B)

# Arguments: string, tuple B
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

 
# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main(): 
  print(create_public_key(generate_private_key(n=8)))

if __name__ == "__main__":
    main()