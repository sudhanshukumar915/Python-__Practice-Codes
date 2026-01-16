alphabete=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
choose_direction=input("TYPE ENCODE TO ENCODE : TYPE DECODE TO DECODE :\n").lower()
text=input("TYPE YOUR MASSAGE \n").lower()
shift_letter=int(input("ENTER YOU WANT TO HOW MANY LETTER SHIFTED...\n"))

def encrypt(original_text,shifted_number):
     store_text= ""
     for letter in original_text:
        shifted_position  = alphabete.index(letter)+shifted_number
        shifted_position %=len(alphabete)

        store_text += alphabete[shifted_position]

     print(f"YOUR ENCODED RESULT :{store_text}")

#function defining in dycrept
def decrypet(original_text, shifted_number):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabete.index(letter) - shifted_number
        shifted_position %= len(alphabete)

        output_text += alphabete[shifted_position]

    print(f"YOUR DECODED RESULT :{output_text}")




encrypt(original_text=text,shifted_number=shift_letter)
decrypet(original_text=text,shifted_number=shift_letter)