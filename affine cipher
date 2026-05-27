def alphabet_generator(alphabet_version):
    alphabet_dictionary={}
    alphabets={1:"abcdefghijklmnopqrstuvwxyz", 2:" .,?!abcdefghijklmnopqrstuvwxyz"
    ,3:"abcdefghijklmnopqrstuvwxyz0123456789",4: " .,?!abcdefghijklmnopqrstuvwxyz0123456789"}
    if int(alphabet_version) not in alphabets:
        alphabet=input("Enter your alphabet as a string. eg: abcde. ")
    else:
        alphabet=alphabets[alphabet_version]
    index=0
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

def affine_cipher(dictionary: dict,a: int, b: int, string: str, encryption_status: str):
    string=string.lower()
    affine_dictionary={}
    for characters in dictionary:
        value=((a*(dictionary[characters]))+b) % len(dictionary)
        affine_dictionary[value]=characters
    affine_dictionary_reverse=dictionary_invertor(affine_dictionary)
    dictionary_reverse=dictionary_invertor(dictionary)
    
    if encryption_status=="encrypt":
        encrypted_string=""
        for letters in string:
            if letters in dictionary:
                item_value=affine_dictionary_reverse[letters]
                encrypted_string+=dictionary_reverse[item_value]
            else:
                encrypted_string+=letters
    elif encryption_status=="decrypt":
        encrypted_string=""
        for numbers in range(1,len(dictionary)):
            if (numbers*a) % len(dictionary)==1:
                inverse=numbers
                break
        for letters in string:
            if letters in dictionary:
                value=dictionary[letters]
                new_value=(inverse*(value-b)) % len(dictionary)
                encrypted_string+= dictionary_reverse[new_value]
            else:
                encrypted_string+=letters
    return encrypted_string

if __name__=="__main__":
    dictionary=alphabet_generator(4)
    print(affine_cipher(dictionary,23,6,"a house divided against itself cannot stand.", "encrypt"))
