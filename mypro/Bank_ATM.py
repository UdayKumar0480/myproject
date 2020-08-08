print("Welcome to My Cooperative Bank ATM")
restart = ("Y")
chance = 3
balance = 999.12
while chance >= 0:
	pip = int(input('Please Enter your 4 Digits Pin: '))
	if pin ==(0480):
		print("You enter your pin correctly")
		print("please press 1 for your balance enquiry")
		print("please press 2 to Make a withdrawl")
		print("please press 3 to pay")
		print("please press 4 to return card\n")
		while restart not in("n","NO","no","N"):
			print("You enter your pin correctly")
			print("please press 1 for your balance enquiry")
			print("please press 2 to Make a withdrawl")
			print("please press 3 to pay")
			print("please press 4 to return card")
			option = int(input("what would you like to choose?: "))
			if option ==1:
				print("Your Balance is /-",balance)
				restart = input("would you like to go back? ")
				if restart in("n","NO","no","N"):
					print("Thank You")
					break
			elif option == 2:
				option2 = ("y")
				withdrawl = float(input("How much would like to withdrawl? 10,20,40,60,80,100 for other enter 1: ")
if withdrawl in [10,20,40,60,80,100]:
					balance = balance - withdrawl
					print 