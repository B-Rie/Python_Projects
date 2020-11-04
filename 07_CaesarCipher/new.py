SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = len(SYMBOLS)

def getMode():
	# Return users request.
	while True:
		print('Do you wish to encrypt, decrypt, or brute-force a message?')
		mode = input().lower()
		
		if mode[0] in ['e','encrypt','d','decrypt','b','brute-force']:
			return mode
			
def getMessage():
	# Retrieve message from user to encrypt or decrypt
	print("Enter your message.")
	return input()
	
def getKey():
	while True:
		print('Enter your key (0-52)')
		key = int(input())
		if key > 0 and key <=  MAX_KEY_SIZE:
			return key
		else:
			print('Please enter a key number between 0 and %s' % MAX_KEY_SIZE)

def getTranslation(mode, message, key):
	
	if mode[0] == 'd':
		key = -key
		
	translated = ''
	for symbol in message:
		symbolIndex = SYMBOLS.find(symbol)
		print('symbolIndex: ', symbolIndex)
		print(len(SYMBOLS))
		if symbolIndex == -1: # Symbol not found in SYMBOLS
			# Just add this symbol without any changes.
			translated += symbol
		else:
			# Encrypt or Decrypt
			symbolIndex += key
			
			if symbolIndex >= len(SYMBOLS):
				symbolIndex -= len(SYMBOLS)
			elif symbolIndex < 0:
				symbolIndex += len(SYMBOLS)
			
			translated +=SYMBOLS[symbolIndex]
	return(translated)
	
	
	
mode = getMode()
message = getMessage()
if mode[0] != 'b':
	key = getKey()
	print(getTranslation(mode, message, key))
else:
	print(MAX_KEY_SIZE)
	for key in range(1, MAX_KEY_SIZE+1):
		print(key, getTranslation('decrypt', message, key))

