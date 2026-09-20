ciphertext = [88, 111, 114, 95, 73, 115, 95, 69, 97, 115, 121]


key = 88 ^ ord('X')
print(f"the key found is the number : {key}")
print(f"which corresponds to character : '{chr(key)}'\n")

flag = ""
for number in ciphertext:
	decrypted_letter = chr(number ^ key)
	flag += decrypted_letter
	
print(f"the flag is : {flag}")
