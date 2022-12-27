# Python program for 2Sab  shop

print("	*********	Welcome to ITI 2Sab shop    **********\n" \
          "     1  for Owner Mode\n" \
          "     2  for User Mode\n" \
	      "     3  for Exit\n")
		  
#================================================================

_2Sab_shop = {"large":20,
                 "meduim":15,
				 "small":10}

_2Sab_file = open("_2Sab_file.txt",'w')
_2Sab_file.write(str(_2Sab_shop))
_2Sab_file.close()
# function of owner

def Owner_Mode():
	print(" Enter owner_name : ")
	owner_name = input()
	password = int(input(" Enter password : "))
	i=1
	
# checking password

	while i<3:
		if password == 1234:
			break
		else:
			print(" Wrong password try again ")
			password = int(input(" Enter password : "))
			i+=1
	print("	-----  owner Operation  -----\n" \
          "     1- show products\n" \
	      "     2- change cost\n"
		  "     3- exit")
	
	owner_oper = int(input(" select owner operation from 1 , 2 , 3 : "))
	while (owner_oper !=0):
		if owner_oper == 1:
			print("   products in 2Sab shop\n ")
			_2Sab_file = open("_2Sab_file.txt",'r')
			print(_2Sab_file.read())
			_2Sab_file.close()
			print("-----------------------------------------")
			
		elif owner_oper == 2:
			print("  Change cost ")
			type = input(" Enter a type to change it cost  : ")
			new_cost = int(input(" Enter a new cost "))
			_2Sab_shop[type]=new_cost
			_2Sab_file = open("_2Sab_file.txt",'w+')
			_2Sab_file.write("\n\n****Change cost****\n\n")
			_2Sab_file.write(str(_2Sab_shop));
			_2Sab_file.close()
					
		elif owner_oper == 3:
			print("   Exit operation")
			exit()
		
		else:
			print(" You didn't enter a valid operation \n")
			
		owner_oper = int(input(" select owner operation from 1 , 2 , 3 : "))
#============================================================================================
# function of user 
def User_Mode():
	print("\n ====#Welcome to ITI _2Sab_shop#==== ")
	print("=====================================================================")
	print("\n  '''*products in _2Sab_shop*'''  \n")
	print(_2Sab_shop)
	print("----------------------------------------------------")
	print("	-----  User Operation  -----\n" \
          "     1- select type large\n" \
          "     2- select type meduim\n" \
		  "     3- select type small\n")
	
	user_oper = int(input(" select user operation from 1 , 2 , 3 : "))
	if user_oper == 1:
		numbers = int(input(" How many numbers do you want ? "))
		cost = numbers * _2Sab_shop["large"]
		print(" The Total price : ",cost)
		
	elif user_oper == 2:
		numbers = int(input(" How many numbers do you want ? "))
		cost = numbers * _2Sab_shop["meduim"]
		print(" The Total price : ",cost)
		
	elif user_oper == 3:
		numbers = int(input(" How many numbers do you want ? "))
		cost = numbers * _2Sab_shop["small"]
		print(" The Total price : ",cost)
		
	_2Sab_Receipt = open("_2Sab_fileReceipts.txt",'a+')
	_2Sab_Receipt.write("\n\t****BILL****\n\n")
	_2Sab_Receipt.write("  TOTAL ITEMS purchased: ")
	_2Sab_Receipt.write(str(numbers))
	_2Sab_Receipt.write("\n  Total price: ")
	_2Sab_Receipt.write(str(cost))
	_2Sab_Receipt.write("\n=============================================================\n")
	_2Sab_Receipt.close()
		
	again()
		
#============================================================================================

def again():
    again = input(
"  Do you want to add more ?\n \
   Please type Y for YES or N for NO.\n")

    if again.upper() == 'Y':
        User_Mode()
    else:
        exit()
	
#============================================================================================
# main program
# select mode ==> owner , user , exit

select_mode = int(input(" select mode from 1 , 2 ,3 :"))

if select_mode == 1:
	Owner_Mode()
elif select_mode == 2:
	User_Mode()
elif select_mode == 3:
	print('''      Exit operation
	=============Thank You================''')
	exit()
	
#===============================================================

