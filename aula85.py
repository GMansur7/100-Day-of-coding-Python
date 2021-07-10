import ceaser_logo
loop = True
print(ceaser_logo.logo)
while loop:

	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	
	def ceaser(text=text, shift=shift, direction=direction):
		shift = shift % 26
		mensagem = []	
		for letter in text:
			if letter in alphabet:
				position = alphabet.index(letter)
				if direction == "encode":
					if ((position + shift) <= 25):
						mensagem.append(alphabet[position + shift])
					else:
						mensagem.append(alphabet[position + shift - 26])
				elif direction == "decode":
					mensagem.append(alphabet[position - shift])
				else:
					print("invalid function")
			else:
				mensagem.append(letter)
		print(f"Here is your {direction} result:" + "".join(mensagem))
	
	ceaser()

	again = input("Do you want to continue a run the Ceaser Cipher, 'yes' or 'no'?")
	if again == "no":
		loop = False
		print("Goodbay")