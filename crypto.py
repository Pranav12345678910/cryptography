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
        
    
    #return final_string

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main(): 
    print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))

if __name__ == "__main__":
    main()
