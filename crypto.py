import random
import math

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
    final_string = "" #string that will be returned later
    for x in plaintext:
        if x.isalpha():
            if ord(x) != 32:
                value_int = ord(x) + offset
                if value_int > ord('Z'):
                    #at this point value_int represents the remainder if there is one, so you need to add it to the starting point which is A, because it doesnt start at 0
                    value_int = value_int - ord('Z') - 1 + ord('A')
                final_string += chr(value_int)
            if ord(x) == 32:
                final_string += x
        else:
            final_string += x
    return final_string 
    
# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset): 
    final_string = "" #string that will be returned later
    for x in ciphertext:
        if x.isalpha():
            if ord(x) != 32:
                value_int = ord(x) - offset
                if value_int < ord('A'):
                    #at this point value_int represents the remainder if there is one, so you need to add it to the starting point which is A, because it doesnt start at 0
                    value_int += 26
                final_string += chr(value_int)
            if ord(x) == 32:
                final_string += x
        else:
            final_string += x
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
        key += keyword[0: len(keyword) - difference]
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
        key += keyword[0: len(keyword) - difference]
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
    
def encrypt_mhkc(plaintext, public_key):
    C = [] #final list that we return
    #eventually this will represent the total of C1
    total = 0
    for x in plaintext: #for each character in the plaintext (loops through each byte) 
        value_int = ord(x)
        #takes the character, and gets the ascii value and then the binary version of that
        binary_value = bin(value_int)
        bit_val_arr = []
        #converts to string so that we can loop through it
        str(binary_value)
        #takes out the "0b" or "1b" part of the binary value
        binary_value = binary_value[2: 10]
        #make sure it is 8 bits by adding necessary leading zeros
        if len(binary_value) != 8:
            missing = 8 - len(binary_value)
            while missing != 0:
                bit_val_arr.append(0)
                missing -= 1
        for elem in binary_value: #for each bit in the byte of the plaintext (loops through each bit within the byte) 
            bit_val_arr.append(elem)
        for y in range(len(bit_val_arr)):
            #for each bit in the byte, it multiplies that bit with the corresponding value in the public key 
            total += int(bit_val_arr[y])*public_key[y]
        C.append(total)
        #resets total to 0 so that it doesn't accumulate across different bytes. Total is the total of the bit val arr * public_key for a given byte
        total = 0
        #right now the different bits multiplied are different elements in the array, but we need to sum them instead 
    C = tuple(C)
    return C
 
# Arguments: list of integers, private key (W, Q, R) with W a tuple.
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    #separating W, Q, and R and making other variables
    W = private_key[0]
    R = private_key[1]
    Q = private_key[2]
    S = 1
    final_string = ""
    while Q * S % R != 1:
        S += 1
    for x in ciphertext:
        m = []
        C1 = x * S % R
        for i in range(len(W)):
            if  C1 >= W[len(W) - i - 1]:
                C1 -= W[len(W) - i - 1]
                m.append(1)
            else:
                m.append(0)
        m.reverse()
        m1 = ""
        for y in m:
            m1 += str(y) 
        final_string += chr(int(m1, 2))
    return final_string


def main(): 
    print(decrypt_mhkc(encrypt_mhkc("MICHAELTHIBODEAUX", (6728, 5993, 4838, 6421, 2334, 1849, 6121, 3438)), ((4, 11, 22, 75, 182, 527, 1099, 2418), 7148, 7043)))
if __name__ == "__main__":
    main()