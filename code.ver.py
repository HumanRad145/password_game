import statistics
from sympy import *

correct = False
rule1 = False
rule2 = False
rule3 = False
rule4 = False
rule5 = False
rule6 = False
rule7 = False
rule8 = False
rule9 = False
rule10 = False
rule11 = False

colour = ["red", "yellow", "blue"]
lencolour = [3,6,4]

subject = ["ict", "ths", "phy", "bio"]


rule = ["Rule 1: Your password must be at least 8 characters",
		"Rule 2: Your password must add up to 51",
		"Rule 3: Your password must include a colour from the 3 primary colour",
		"Rule 4: Your password must include at least 4 prime numbers from 1-10",
		"Rule 5: Your password must include something Mr.Poon gifted us last year in F.4 (Hint: it can bend)",
		"Rule 6: All vowel letters in your password should be capital",
		"Rule 7: Your password must include the year World War 2 ended.",
		"Rule 8: Your password must include the abbreviation of an elective in HYS of 3 letters",
		"Rule 9: The mode of your password must be 6",
		"Rule 10: The number of lowercase letters in your password should be 2 times to the number of uppercase letters.",
		"Rule 11: The length of your password must be a prime number."]


while correct == False:
	if rule1 == True:
		print("Previous: " + password)
	password = input("Password: ")
	count = 0

	print("\n" + rule[0])
	if len(password) >= 8: #rule 1
		count += 1
		rule1 = True
	else:
		print("Incorrect." + "\n")

	if rule1 == True: #rule 2
		print("\n" + rule[1])
		sum = 0
		for i in password:
			if i.isdigit():
				sum += int(i)
		if sum != 51:
			print("Incorrect.")
		else:
			count += 1
			rule2 = True
		print("\n")

	if rule2 == True: #rule 3
		print(rule[2])
		k2 = False
		for i in range (len(password)):
			for j in range (3):
				if password.lower()[i:int(lencolour[j])+i] == colour[j]:
					rule3 = True
					k2 = True
		if k2 == False:
			print("Incorrect.")
		else:
			count += 1
		print("\n")

	if rule3 == True: #rule 4
		print(rule[3])
		countPrime = 0
		for i in range(len(password)):
			if password[i] == '2' or password[i] == '3' or password[i] == '5' or password[i] == '7':
				countPrime += 1
		if countPrime >= 4:
			count += 1
			rule4 = True
		else:
			print("Incorrect.")
		print("\n")

	if rule4 == True: #rule 5
		k5 = False
		print(rule[4])
		for i in range (len(password)):
				if password.lower()[i:int(len("ruler"))+i] == "ruler":
					count += 1
					rule5 = True
					k5 = True
		if k5 == False:
			print("Incorrect.")
		print("\n")

	if rule5 == True: #rule 6
		k6 = False
		print(rule[5])
		for i in range(len(password)):
			if password[i] == 'a' or password[i] == 'e' or password[i] == 'i' or password[i] == 'o' or password[i] == 'u':
				k6 = True
		if k6 == True:
			print("Incorrect.")
		else:
			count += 1
			rule6 = True
		print("\n")

	if rule6 == True: #rule 7
		k7 = False
		print(rule[6])
		for i in range (len(password)):
			if password[i:4+i] == "1945":
				count += 1
				rule7 = True
				k7 = True
		if k7 == False:
			print("Incorrect.")
		print("\n")

	if rule7 == True: #rule 8
		k8 = False
		print(rule[7])
		for i in range (len(password)):
			for j in range (4):
				if password.lower()[i:3+i] == subject[j]:
					count += 1
					rule8 = True
					k8 = True
		if k8 == False:
			print("Incorrect.")
		print("\n")

	if rule8 == True: #rule 9
		k9 = False
		print(rule[8])
		temp = []
		for i in password:
			if (i.isnumeric()):
				temp.append(i)
		mode = statistics.mode(temp)
		if mode == '6':
			count += 1
			k9 = True
			rule9 = True
		if k9 == False:
			print("Incorrect.")
		print("\n")

	if rule9 == True: #rule 10
		k10 = False
		print(rule[9])
		lower = 0
		upper = 0
		number = 0
		for i in password:
			if (i.islower()):
				lower += 1
			elif (i.isupper()):
				upper += 1

		if lower == upper*2:
			count += 1
			rule10 = True
		else:
			print("Incorrect.")
		print("\n")

	if rule10 == True: #rule 11
		print(rule[10])
		length_pass = len(password)
		isPrime = isprime(length_pass)
		if isPrime == True:
			count += 1
		else:
			print("Incorrect.")
		print("Length of current password: " ,  length_pass)
		print("\n")

	if count == 11:
		correct = True
		print("\nCONGRATS, YOU'VE SOLVED THE PASSWORD GAME\n")
		print("Your password is: " + password + "\n")
