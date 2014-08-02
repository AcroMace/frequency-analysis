import sys

def increase_letters_by_one(text):
	new_sentence = ""
	for letter in text:
		if not letter.isalpha():
			new_sentence += letter
		elif letter == 'z':
			new_sentence += 'a'
		elif letter == 'Z':
			new_sentence += 'A'
		else:
			new_sentence += chr(ord(letter) + 1)
	return new_sentence


if __name__ == '__main__':
	unencrypted_file = open(str(sys.argv[1]), 'r')
	encrypted_file = open('encrypted.txt', 'w')
	encrypted_file.write(increase_letters_by_one(unencrypted_file.read()))
	unencrypted_file.close()
	encrypted_file.close()
