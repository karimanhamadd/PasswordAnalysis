#!/usr/bin/env python3

import sys
import re

def main():
	""" This script reads a text from standard input,
	analyzes the validity of a password in each line,
	if valid assesses the strength of the password,
	and writes results of the password analysis into
	the standard output  """

	# if no arguments provided --> show error message
	if len(sys.argv) != 1:
		print("No arguments should be provided.")
		print("Usage: %s" % sys.argv[0])
		return 1;


	for password in sys.stdin:
		#iterate over passwords from stdin
		password = password.strip()
		validity_errors = []
		#check for validity errors using regular expressions 
		if not re.match(r'.{8,}', password):
			validity_errors.append("TOO_SHORT")
			
		if not re.match(r'^[\x00-\x7F]+$', password):
			validity_errors.append("NONASCII")
		#print validity errors and continue to the next password if invalid 
		if validity_errors:
			print(f"0,INVALID,{','.join(validity_errors)}")
			continue
			
		#check password strength
		strength = 1
		details = []
	
		if re.search(r'[A-Z]', password):
			strength+=1
			details.append("UPPERCASE")
		
		if re.search(r'[a-z]', password):
			strength+=1
			details.append("LOWERCASE")
		
		if re.search(r'\d', password):
			strength+=1
			details.append("NUMBER")
		
		if re.search(r'[!#$%&()*+,\-./:;<=>?@[\]^_`{|}~]', password):
			strength+=1
			details.append("SPECIAL")
		#check for the sequence of 3 characters
		if re.search(r'(.)\1\1', password):
			strength-=1
			details.append("sequence")
		
		output = f"{strength}," if details else f"{strength},"
	
	   #determine strength level + add details 
		if strength ==1:
			output+= "VERY_WEAK,"
		elif strength == 2:
			output+= "WEAK,"
		elif strength == 3:
			output+= "MEDIUM,"
		elif strength == 4:
			output += "STRONG,"
		elif strength == 5:
			output += "VERY_STRONG,"
		if details:
			output += ",".join(details)
		print(output)
	return 0

if __name__ == "__main__":
	main()
