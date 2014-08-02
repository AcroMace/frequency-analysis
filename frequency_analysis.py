# frequency_analysis: basic frequency analysis for cracking substitution
#                     ciphers; only letters in English

import sys

# English letters, ordered by frequency
# http://www.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
ENG_LET_DIST = 'etaoinsrhdlucmfywgpbvkxqjz'


def populate_frequency_dictionary(text):
	frequency_dictionary = {}
	for letter in text:
		if not letter.isalpha():
			continue
		key = letter.lower()
		if key in frequency_dictionary:
			frequency_dictionary[key] += 1
		else:
			frequency_dictionary[key] = 1
	return frequency_dictionary


def sort_frequency_dictionary(freq_dict):
	return sorted(freq_dict, key=freq_dict.get, reverse=True)


def substitute_original_text_with_freq_dict(text, freq_dict):
	new_sentence = ""
	for letter in text:
		if not letter.isalpha():
			new_sentence += letter
		else:
			order = freq_dict.index(letter.lower())
			new_letter = ENG_LET_DIST[order]
			if letter.isupper():
				new_sentence += new_letter.upper()
			else:
				new_sentence += new_letter
	return new_sentence


def frequency_analysis(file_path):
	encoded_file = open(file_path, 'r')
	decoded_file = open('unencrypted.txt', 'w')
	text = encoded_file.read()
	freq_dict = populate_frequency_dictionary(text)
	freq_dict = sort_frequency_dictionary(freq_dict)
	decoded_file.write(substitute_original_text_with_freq_dict(text, freq_dict))
	encoded_file.close()
	decoded_file.close()


if __name__ == '__main__':
	frequency_analysis(str(sys.argv[1]))
