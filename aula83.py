alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text=text, shift=shift, alphabet=alphabet):
		cipher_text = []
		cipher_index = []
		for letter in text:
			position = alphabet.index(letter)
			if ((position + shift) <= 25):
				cipher_index.append(position + shift)
#				print (cipher_index)
			else:		
				cipher_index.append(position + shift - 26)	
		print(cipher_index) 
		for index in cipher_index:
			cipher_text.append(alphabet[index])
		print( "".join(cipher_text))
###############################		
def decrypt(text=text, shift=shift,alphabet=alphabet):
	cipher_text = []
	cipher_index = []
	mensagem = []
	for letter in text:
		cipher_text.append(letter)
		position = cipher_text.index(letter)
		print (position)
		if (position - shift) > 0:	
			cipher_index.append(position - shift)
		else:
			cipher_index.append(position - shift)	
	print(cipher_text)
	print(cipher_index)
	for index in cipher_index:
		mensagem.append(alphabet[index])
	print("".join(mensagem))

if direction == "encode":
	encrypt ()
elif direction == "decode":
    decrypt()
else:
    print("Invalid function")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message