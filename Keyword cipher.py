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

def dictionary_invertor(dictionary):
    reverse_dict={}
    for items in dictionary:
        key= dictionary[items]
        value=items
        reverse_dict[key]=value
    return reverse_dict

def mixed_alphabet_cipher(alphabet_version,key,string, encryption):
    string=string.lower()
    key=key.lower()
    alphabet=alphabet_generator(alphabet_version)
    key_letter_list=[]
    for items in key:
        if items not in key_letter_list:
            key_letter_list.append(items)
    mixed_alphabet_dictionary={}
    index=1
    for items in key_letter_list:
        if items in alphabet:
            mixed_alphabet_dictionary[items]=index
            index+=1
    for letters in alphabet:
        if letters not in mixed_alphabet_dictionary:
            mixed_alphabet_dictionary[letters]=index
            index+=1
    if encryption=="encrypt":
        reverse_mixed_alphabet=dictionary_invertor(mixed_alphabet_dictionary)
        final_text=""
        for items in string:
            if items in alphabet:
                value=alphabet[items]
                final_text+=reverse_mixed_alphabet[value]
            else:
                final_text+=items
    elif encryption=="decrypt":
        reverse_alphabet=dictionary_invertor(alphabet)
        final_text=""
        for items in string:
            if items in alphabet:
                value=mixed_alphabet_dictionary[items]
                final_text+=reverse_alphabet[value]
            else:
                final_text+=items
    return final_text

if __name__=="__main__":
    while True:
        print("What alphabet are you using?")
        print("Standard Alphabet: abcdefghijklmnopqrstuvwxyz. Enter 1")
        print("Alphabet with punctuation:  .,?!abcdefghijklmnopqrstuvwxyz. Enter 2")
        print("Alphabet with numbers: abcdefghijklmnopqrstuvwxyz0123456789. Enter 3")
        print("Alphabet with both punctuation and numbers:  .,?!abcdefghijklmnopqrstuvwxyz0123456789. Enter 4")
        print("Enter your own alphabet: Enter 5")
        print()
        user_alphabet=int(input("Enter Alphabet number: "))
        user_key=input("Enter the encrypting key: ")
        user_text=input("Enter your encryption text: ")
        user_encryption=input("Do you want to encrypt or decrypt? Enter 'encrypt' for encryption and 'decrypt' for decryption: ")
        print()
        user_encrypted_text=mixed_alphabet_cipher(user_alphabet,user_key,user_text,user_encryption)
        print(f"Your encrypted/decrypted text is '{user_encrypted_text}'")
        print()