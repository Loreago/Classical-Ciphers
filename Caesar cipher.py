# Caesar cipher encryptor
def dictionary_invertor(dictionary):
    reverse_dict={}
    for items in dictionary:
        key= dictionary[items]
        value=items
        reverse_dict[key]=value
    return reverse_dict
    
def alphabet_generator(alphabet_version):
    alphabet_dictionary={}
    alphabets={1:"abcdefghijklmnopqrstuvwxyz", 2:" .,?!abcdefghijklmnopqrstuvwxyz"
    ,3:"abcdefghijklmnopqrstuvwxyz0123456789",4: " .,?!abcdefghijklmnopqrstuvwxyz0123456789"}
    if int(alphabet_version) not in alphabets:
        alphabet=input("Enter your alphabet as a string. eg: abcde. ")
    else:
        alphabet=alphabets[alphabet_version]
    index=1
    for items in alphabet:
        alphabet_dictionary[items]=index
        index += 1
    return alphabet_dictionary

def caesar_cipher(standard_alphabet: dict, caesar_shift: int, text: str):
    if abs(caesar_shift)>len(standard_alphabet):
        caesar_shift=caesar_shift%len(standard_alphabet)
    if caesar_shift<0:
        caesar_shift=len(standard_alphabet)+caesar_shift
    text=text.lower()
    caesar_alphabet={}
    index=1
    for items in standard_alphabet:
        if standard_alphabet[items]>caesar_shift:
            caesar_alphabet[index]=items
            index+=1
    for items in standard_alphabet:
        if standard_alphabet[items]<caesar_shift+1:
            caesar_alphabet[index]=items
            index+=1
    final_string=""
    for characters in text:
        if characters in standard_alphabet:
            position=standard_alphabet[characters]
            encrypted_character=caesar_alphabet[position]
            final_string += encrypted_character
        else:
            final_string += characters
    return final_string


if __name__=="__main__":
    while True:
        alphabet=alphabet_generator(int(input("Enter the alphabet you want to use: 1: only letters, 2: letters and punctuation, 3: letters and numbers, 4: everything combined. 5: enter your own alphabet: ")))
        caesar_shift_number=int(input("Enter the ceasar shift you want to encrypt/decrypt with. Note: if decrypting enter only number and not sign. "))
        encryption_status=input("Do you want to encrypt or decrypt this text?, enter 'decrypt' or 'encrypt': ")
        if encryption_status=="decrypt":
            caesar_shift_number*=-1
        text=input("Enter your text: ")
        final_text=caesar_cipher(alphabet,caesar_shift_number,text)
        print("Your text after encryption after decryption is: ")
        print(final_text)
