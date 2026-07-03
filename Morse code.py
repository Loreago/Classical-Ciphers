morse_code_dictionary={'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.','G': '--.', 
                       'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 
                       'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                       '1': '.----', '2':'..---','3':'...--','4':'....-', '5':'.....','6':'-....', '7':'--...','8':'---..','9':'----.','0':'-----', 
                       '.':'.-.-.-', ',':'--..--','?':'..--..'}


reverse_dictionary={'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', 
                    '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', 
                    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', 
                    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', 
                    '/':' ', '.-.-.-':'.', '--..--':',', '..--..':'?'}


def morse_code(text: str,coding_status: str):
    text=text.upper()
    formatted_text=text
    final_text=""
    if coding_status=="encrypt":
        for items in formatted_text:
            if items in morse_code_dictionary:
                final_text+=morse_code_dictionary[items]+" "
            elif items==" ":
                final_text+="/ "
            else:
                final_text+=items+" "
    elif coding_status=="decrypt":
        formatted_text=formatted_text.replace("_","-")
        if " " in formatted_text:
            formatted_text=formatted_text.split(" ")
        for items in formatted_text:
            if items in reverse_dictionary:
                final_text+=reverse_dictionary[items]
            else:
                final_text+=items
    return final_text


if __name__=="__main__":
    while True:
        encryption_status=input("If you want to encrypt morse code, enter 'encrypt' or if you want to decrypt, enter 'decrypt: ")
        user_text=input("Enter your text: ")
        if encryption_status=="encrypt" or encryption_status=="decrypt":
            final_text=morse_code(user_text,encryption_status)
        try:
            final_text=final_text
        except:
            print("Invalid text/encryption method. Try again!")
            continue
        print("Your final text is:")
        print(final_text)
        status=input("continue? enter any key to continue or else enter nothing to end: ")
        if status==" ":
            break
