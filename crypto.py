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
        print(final_string) 
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
    pass

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
    pass

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
    print(decrypt_caesar("ERE", 3))

if __name__ == "__main__":
    main()
