# Reverse Cipher
# Use python3
import sys
import optparse

parser = optparse.OptionParser()
parser.add_option('-c',
				action="store",
				dest="caesar")
# Key Shift
parser.add_option('-s',
				action="store",
				dest="shift")
# Encrypt or Decrypt
parser.add_option('-m',
				action="store",
				dest="mode")
# Placeholder for reversing
parser.add_option('-r',
				action="store",
				dest="reverse")

(opts, args) = parser.parse_args()

def reverse_string(message):
	i = len(message) - 1
	translated = ''
	while i >= 0:
		translated = translated + message[i]
		i = i - 1
	return translated

def caesar_cipher(message, key, mode):
	translated = ''
	for letter in message:
		ascii_letter = ord(letter)
		# + num (encrypt) - num (decrypt)?
		if mode == 'encrypt':
			ascii_letter = ascii_letter + key
		else:
			ascii_letter = ascii_letter - key
		# printable characters ofset
		if ascii_letter > 126 and mode == 'encrypt':
			ascii_letter = ascii_letter - 94
		elif ascii_letter > 126 and mode != 'encrypt':
			ascii_letter = ascii_letter + 94
		shift_letter = chr(ascii_letter)
		translated = translated + shift_letter
	print("Output: Key " + str(key) + " String: " + translated)

if opts.reverse:
	message = opts.reverse
	out_string = reverse_string(message)
	print("Reversed message: " + message)

if opts.caesar and opts.shift and opts.mode:
	message = opts.caesar
	key = int(opts.shift)
	mode = opts.mode
	print(message)
	print(key)
	print(mode)
	caesar_cipher(message, key, mode)
