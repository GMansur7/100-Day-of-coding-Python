alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text=text, shift=shift, alphabet=alphabet):
	cipher_text = []
	cipher_index = []
	for letter in text:
		position = alphabet.index(letter)
		if ((position + shift) <= 25):
			cipher_index.append(position + shift)
		else:		
			cipher_index.append(position + shift - 26)	
	for index in cipher_index:
		cipher_text.append(alphabet[index])
	print( "".join(cipher_text))
#####################################################################	
def decrypt(text=text, shift=shift,alphabet=alphabet):
	cipher_text = []
	cipher_index = []
	mensagem = []
	for letter in text:
		cipher_text.append(letter)
		position = alphabet.index(letter)
		if (position - shift) > 0:
			cipher_index.append(position - shift)
		else:
			cipher_index.append(position - shift)	
	for index in cipher_index:
		mensagem.append(alphabet[index])
	print("".join(mensagem))

if direction == "encode":
	encrypt ()
elif direction == "decode":
    decrypt()
else:
    print("Invalid function")