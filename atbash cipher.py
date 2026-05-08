# atbash cipher generator/decoder?
def alphabet_generator(encryption_level):
    alphabet_dictionary={}
    alphabets={1:"abcdefghijklmnopqrstuvwxyz", 2:" .,?!abcdefghijklmnopqrstuvwxyz"
    ,3:"abcdefghijklmnopqrstuvwxyz0123456789",4: " .,?!abcdefghijklmnopqrstuvwxyz0123456789"}
    alphabet=alphabets[encryption_level]
    index=1
    for items in alphabet:
        alphabet_dictionary[items]=index
        index += 1
    return alphabet_dictionary


def atbash_cipher(string,encryption_level,encryption_status):
    string=string.lower()
    atbash_alphabet={}
    normal_alphabet=alphabet_generator(encryption_level)
    index=len(normal_alphabet)
    for items in normal_alphabet:
        atbash_alphabet[index]=items
        index -= 1
    encrypted_string=""
    if encryption_status=="encrypt":
        for items in string:
            if items in normal_alphabet:
                item_position=normal_alphabet[items]
                final_item=atbash_alphabet[item_position]
                encrypted_string+=final_item
            else:
                encrypted_string+=items
        encrypted_string.upper()
    elif encryption_status=="decrypt":
        inverted_normal_alphabet={}
        inverted_atbash_alphabet={}
        for items in normal_alphabet:
            key= normal_alphabet[items]
            value=items
            inverted_normal_alphabet[key]=value
        for items in atbash_alphabet:
            key= atbash_alphabet[items]
            value=items
            inverted_atbash_alphabet[key]=value
        for items in string:
            if items in normal_alphabet:
                item_position=inverted_atbash_alphabet[items]
                final_item=inverted_normal_alphabet[item_position]
                encrypted_string+=final_item
            else:
                encrypted_string+=items

    return encrypted_string

if __name__=="__main__":
    string=input("Enter the text you want to encrypt/decrypt: ")
    encryption_status=input("Do you want to encrypt or decrypt this text? 'encrypt' for encrypting or 'decrypt for decrypting: ")
    encryption_level=int(input("Choose what you want to encrypt/decrypt. Only alphabets: 1, alphabets and punctuation: 2, alphabets and numbers: 3, everything: 4. "))
    print(atbash_cipher(string,encryption_level, encryption_status))