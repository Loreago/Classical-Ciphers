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

def railfence_cipher_nulls(user_alphabet: int, key: int, string: str):
    alphabet=alphabet_generator(user_alphabet)
    while True:
        total_lists=[]
        current_row_index=1
        while current_row_index<=key:
            rail_index=1
            descending=True
            current_row=[]
            for letter in string:
                if letter not in alphabet:
                    continue
                if rail_index==current_row_index:
                    current_row.append(letter)
                if descending==True:
                    rail_index+=1
                elif descending==False:
                    rail_index-=1
                if rail_index==key:
                    descending=False
                if rail_index==1:
                    descending=True
            total_lists.append(current_row)
            current_row_index+=1
        if len(total_lists[0])==len(total_lists[-1]):
            return string
        else:
            string+="x"

def railfence_cipher(user_alphabet: int, key: int, string: str,nulls: bool, encryption: str):
    string=string.lower()
    if nulls==True:
        string=railfence_cipher_nulls(user_alphabet,key,string)
    alphabet=alphabet_generator(user_alphabet)
    final_string=""
    current_row_index=1
    if encryption=="encrypt":
        while current_row_index<=key:
            rail_index=1
            descending=True
            for letter in string:
                if letter not in alphabet:
                    continue
                if rail_index==current_row_index:
                    final_string+=letter
                if descending==True:
                    rail_index+=1
                elif descending==False:
                    rail_index-=1
                if rail_index==key:
                    descending=False
                if rail_index==1:
                    descending=True
            current_row_index+=1
    elif encryption=="decrypt":
        original_string_length=len(string)
        total_rows=[["padding"]] # I've added padding in order to make row operations easier as row 1 will be the actual first row in the cipher.
        while current_row_index<=key:
            rail_index=1
            descending=True
            current_row=[]
            for letter in range(0,original_string_length):
                if rail_index==current_row_index:
                    current_row.append(string[0])
                    string=string[1:]
                if descending==True:
                    rail_index+=1
                elif descending==False:
                    rail_index-=1
                if rail_index==key:
                    descending=False
                if rail_index==1:
                    descending=True
            total_rows.append(current_row)
            current_row_index+=1
        rail_index=1
        descending=True
        row_completion=0
        while row_completion<=key:
            if len(total_rows[rail_index])==0:
                row_completion+=1
                if descending==True:
                    rail_index+=1
                elif descending==False:
                    rail_index-=1
                if rail_index==key:
                    descending=False
                if rail_index==1:
                    descending=True
                continue
            else:
                final_string+=total_rows[rail_index][0]
                total_rows[rail_index].pop(0)
                if descending==True:
                    rail_index+=1
                elif descending==False:
                    rail_index-=1
                if rail_index==key:
                    descending=False
                if rail_index==1:
                    descending=True
    return final_string.upper()
            

print(railfence_cipher(4,5,"Chinnu is a topper.",True,"Encrypt"))
print(railfence_cipher(4,5,"CSEHI PRI AP.NU OXNTX",False,"Decrypt"))

if __name__=="__main__":
    while True:
        user_encryption=input("Do you want to encrypt or decrypt? Enter 'encrypt' for encryption and 'decrypt' for decryption: ") 
        if user_encryption!="encrypt":
            if user_encryption!="decrypt":
                print("Invalid encryption process. Try again!")
                continue
        if user_encryption=="encrypt":
            print("What alphabet are you using?")
            print("Standard Alphabet: abcdefghijklmnopqrstuvwxyz. Enter 1")
            print("Alphabet with punctuation:  .,?!abcdefghijklmnopqrstuvwxyz. Enter 2")
            print("Alphabet with numbers: abcdefghijklmnopqrstuvwxyz0123456789. Enter 3")
            print("Alphabet with both punctuation and numbers:  .,?!abcdefghijklmnopqrstuvwxyz0123456789. Enter 4")
            print("Enter your own alphabet: Enter 5")
            print()
            user_alphabet=int(input("Enter Alphabet number: "))
            user_key=int(input("Enter the encrypting key, i.e. the number of rows: "))
            user_null_status=input("Do you want to use nulls at the end of your text? enter y/n: ")
            if user_null_status=="y":
                user_null_status=True
            else:
                user_null_status=False
            user_text=input("Enter your encryption text: ")
            print()
            user_encrypted_text=railfence_cipher(user_alphabet,user_key,user_text,user_null_status,user_encryption)
            print(f"Your encrypted text is '{user_encrypted_text}'")
            print()
        else:
            user_alphabet=1
            user_null_status=False
            user_key=int(input("Enter the decrypting key, i.e. the number of rows: "))
            user_text=input("Enter your decryption text: ")
            print()
            user_encrypted_text=railfence_cipher(user_alphabet,user_key,user_text,user_null_status,user_encryption)
            print(f"Your decrypted text is '{user_encrypted_text}'")
            print()
        program_status=input("Would you like to continue? y/n: ")
        if program_status=="n":
            break