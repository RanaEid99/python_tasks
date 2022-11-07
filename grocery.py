# Python program for grocery shop

import datetime
print("	*********	Welcome to ITI shop    **********\n" \
          "     1  for Owner Mode\n" \
          "     2  for User Mode\n" \
	      "     3  for Exit\n")
		  
#================================================================

grocery_shop = {"banana":[55,15],
                 "apple":[45,25],
				 "orange":[65,15],
				 "kiwi":[35,20]}
items_bought = {}

grocery_menu = {"banana":15, "apple":25, "orange":15, "kiwi":20}
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
          "     2- Add product\n" \
	      "     3- change cost\n"
		  "     4- delete product\n" \
		  "     5- exit")
	
	owner_oper = int(input(" select owner operation from 1 , 2 , 3 , 4 , 5 : "))
	while (owner_oper !=0):
		if owner_oper == 1:
			print("   products in grocery shop\n ")
			print(grocery_shop)
			print("-----------------------------------------")
			
		elif owner_oper == 2:
			print("  Add product ")
			#id = int(input(" Enter ID : "))
			product = input(" Enter a new product : ")
			
			if product in grocery_shop:
				print(" product already in grocery shop ")
				quantity = int(input(" Enter quantity : "))
				grocery_shop[product][0] += [quantity]
			else:
				quantity = int(input(" Enter quantity : "))
				price = int(input(" Enter price : "))
				#grocery_shop[product] += [quantity,price]
				grocery_shop.update({'item_name':product , 'quantity':quantity , 'price':price})
				print(grocery_shop)
			
		elif owner_oper == 3:
			print("  Change cost ")
			#id = input(" Enter an ID to change it cost  : ")
			product = input(" Enter an product to change it cost  : ")
			new_cost = int(input(" Enter a new cost "))
			grocery_shop[product][1]=new_cost
			grocery_menu[product]=new_cost
			
		elif owner_oper == 4:
			print("  Delete product ")
			product = input(" Enter a product to delete it : ")
			del(grocery_shop[product])
			del(grocery_menu[product])
			
		elif owner_oper == 5:
			print("   Exit operation")
			exit()
		
		else:
			print(" You didn't enter a valid operation \n")
			
		owner_oper = int(input(" select owner operation from 1 , 2 , 3 , 4 ,5 : "))
#============================================================================================
# function of user 
def User_Mode():
	print(" ====#Welcome to ITI grocery shop#==== ")
	customer_name = input(" Please enter your name : ")
	print("	-----  User Operation  -----\n" \
          "     1- show products\n" \
          "     2- buy product\n" \
	      "     3- print bill\n")
	
	user_oper = int(input(" select user operation from 1 , 2 , 3 : "))
	if user_oper == 1:
		print("  '''*products in grocery shop*'''  ")
		print(grocery_menu)
		print("----------------------------------------------------")
		again()
	elif user_oper == 2:
		choice=input("Do you want to buy (yes/no): ")
		item_added =0
		item_qty =0
		
		while choice.lower()=="yes":
			item_added=input("Add an item: ")
			if item_added in grocery_menu:
				item_qty=int(input("Add quantity: "))
				grocery_shop[item_added][0] -= item_qty
				TotalPrice = grocery_shop[item_added][1]*item_qty
				items_bought = {'item_name':item_added , 'quantity':item_qty , 'price':TotalPrice}
				print(grocery_shop)
				items_bought.update({'item_name':item_added , 'quantity':item_qty , 'price':TotalPrice})
				print(items_bought)
			else:
				print("unable to add unavailable item")
			choice=input("Do you want to add more items (yes/no): ")
            
		else:
			print("\n")
			print("****  Bill Summary  ***** ")
			print("  Mr/Ms : ",customer_name)
			print("  Item    Quantity    TotalPrice")
			total=0
			print(items_bought)
			total += TotalPrice
			print("Total: ",total)
			now = datetime.datetime.now()
			print (now.strftime("%Y-%m-%d %H:%M:%S"))
			print("***********Thank You********")
			print("Hope to see you back soon!")
		
#============================================================================================

def again():
    again = input(
"  Do you want to continue ?\n \
   Please type Y for YES or N for NO.\n")

    if again.upper() == 'Y':
        User_Mode()
    elif again.upper() == 'N':
        print('	See you later.')
    else:
        again()

#============================================================================================
# main program
# select mode ==> owner , user , exit
select_mode = int(input(" select mode from 1 , 2 ,3 :"))

if select_mode == 1:
	Owner_Mode()
elif select_mode == 2:
	User_Mode()
elif select_mode == 3:
	print('exit')
	exit()
	
#===============================================================

