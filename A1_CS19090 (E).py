import os, sys

print("                                                                                   #######################################               ")
print("                                                                                   THE ARBII.XD BAKERS AND BOUTIQUE  \U0001f600 \U0001f600")
print("                                                                                   #######################################              ")

samosa_in_stock = 0
rolls_in_stock = 0
samosa_unit_value = 10
rolls_unit_value = 15
add_samosas_in_stock = 0
add_rolls_in_stock = 0
total_rolls_sales = 0
total_samosas_sale = 0
rolls_sales = 0
samosas_sale = 0
total_sales = 0
total_sale = 0
target_sale = 1500
Tshirts_in_stock = 80
Jeans_in_stock = 75
cotton_suit_in_stock = 40
lawn_suit_in_stock = 45
Tshirt_unit_price = 700
Jeans_unit_price = 1000
cotton_suit_unit_price = 1200
lawn_suit_unit_price = 1200
total_Tshirts_sale = 0
total_Jeans_sale = 0
total_cotton_suits_sale = 0
total_lawn_suits_sale = 0
total_boutique_sale = 0
target_sale_boutique = 10000

emp_A_wage_rate = 180
emp_B_wage_rate = 150
emp_C_wage_rate = 130
emp_D_wage_rate = 100

total_stock_samosas = int(samosa_in_stock)
total_stock_rolls = int(rolls_in_stock)
total_stock = ((int(samosa_in_stock) + int(rolls_in_stock)))
bonus = 1000

def add_items_to_stock():
    print()
    global samosa_in_stock, rolls_in_stock
    print(":::::::::::::::::::::::::::::")
    print("ADDING BAKERY ITEMS TO STOCK ")
    print(":::::::::::::::::::::::::::::")
    print()
    samosa_in_stock = samosa_in_stock + int(input("Enter Quantity of samosas you want to add ? "))
    #print(samosa_in_stock)
    rolls_in_stock = rolls_in_stock + int(input("Enter Quantity of rolls you want to add ? "))
    #print(rolls_in_stock)
    return " "

def remaining_items():
    print()
    global samosa_in_stock
    global rolls_in_stock
    print("::::::::::::::::::::::::")
    print(" REMAINING BAKERY STOCK ")
    print("::::::::::::::::::::::::")
    print()
    print("The Remaining Stock of samosas left : ", samosa_in_stock)
    print("The remaining Stock of Rolls left : ", rolls_in_stock)
    return ""

def take_order():
    print()
    global samosa_in_stock , add_samosas_in_stock , total_samosas_sale , samosas_sale
    global rolls_in_stock , add_rolls_in_stock , rolls_sales , total_rolls_sales
    global total_sales , quan
    total_sale = (int(total_samosas_sale) + int(total_rolls_sales))
    #print(total_sale)
    print(":::::::::::::::::::::::::::::::")
    print("WELCOME TO ARBII.XD BAKERS \U0001f600")
    print(":::::::::::::::::::::::::::::::")
    print()

    print("samosa_in_stock =", samosa_in_stock , "\n rolls_in_stock = ", rolls_in_stock)
    print("""samosa_unit_value = 10\nrolls_unit_value =  15\n""")
    print("1. PRESS 1 if you want to buy Samosas")
    print("2. PRESS 2 if you want to buy Rolls ")
    #print("3. PRESS 3 TO CLOSE THIS PROGRAM")
    x = int(input("ENTER YOUR CHOICE 1 OR 2 :"))

    print()

    while True :

        if 2>0 :
            if (x == 1) or (x ==2) :

                if x == 1 :

                    if samosa_in_stock >= 1:
                        quan = int(input("Enter Quantity of SAMOSAS you want : "))
                        print()
                        if samosa_in_stock >= quan:

                            print("THANKS FOR YOUR ORDER SIR..\nYou just bought", quan, "Samosas and your bill generates as :",
                            samosa_unit_value * quan, "rupeees")

                            samosas_sale = samosa_unit_value * quan
                            total_samosas_sale = total_samosas_sale + samosas_sale
                            #print(total_samosas_sale)
                            print()

                            print()
                            samosa_in_stock = samosa_in_stock - quan
                            #print("Now the remaining Samosas in our stock are :", samosa_in_stock)
                            if samosa_in_stock <= 0:
                                return "Now Samosas OUT OF STOCK"
                            print()

                        else:
                            print("Actually we have remaining ", samosa_in_stock,
                            "Samosas in our stock. We are running out of out stock")

                    else:
                        print("!!.. Samosas are OUT OF STOCK ..!!")
                        break

                if x == 2 :

                    if rolls_in_stock >= 1:
                        quan = int(input("Enter Quantity of ROLLS you want : "))
                        if rolls_in_stock >= quan:
                            print("THANKS FOR YOUR ORDER SIR..\nYou just bought", quan, "Rolls and your bill generates as :",
                            rolls_unit_value * quan, "rupeees")


                            rolls_sales = rolls_unit_value* quan
                            total_rolls_sales = total_rolls_sales + rolls_sales
                            #print(total_rolls_sales)
                            print()
                            rolls_in_stock = rolls_in_stock - quan


                            if rolls_in_stock <= 0:
                                return "Now Rolls are OUT OF STOCK"
                            print()
                        else:
                            print("Actually we have remaining ", rolls_in_stock,
                            "Rolls in our stock. We are running out of out stock")

                        # elif rolls_in_stock <= 0:
                        # print("Rolls are OUT OF STOCK")

                    else :
                        print("!!.. Rolls are OUT OF STOCK.. !!")
                        break
            else:
                print()
                print("INVALID KEY. Please press 1 OR 2")
                x = int(input("Enter your choice again : "))
                print()
                continue
                #x = int(input("ENTER YOUR CHOICE 1 OR 2......................: "))

        return " "

def total_sale_till_now():
    global total_samosas_sale , total_rolls_sales , total_sale
    total_sale = total_rolls_sales + total_samosas_sale
    print(":::::::::::::::::::::::::::::::::::::::::::::::")
    print("THANK YOU SO MUCH FOR VISITING OUR BAKERY \U0001f600")
    print(":::::::::::::::::::::::::::::::::::::::::::::::")
    print()
    print("Up till now you've purchased items of ",total_sale , "pkr")
    print()

    print("Total amount of Samosas purchased is",total_samosas_sale, "pkr for", int(int(total_samosas_sale)/10) , "Samosas" )
    print("Total amount of Rolls purchased is",total_rolls_sales , "pkr for", int(int(total_rolls_sales)/15) , "Rolls")
    return ""

def emp_wage_rates():
    print(":::::::::::::::::::::::::")
    print("WAGE RATES FOR EMPLOYEES")
    print(":::::::::::::::::::::::::")
    print()
    emp_A_wage = emp_A_wage_rate
    print("The wage of HEAD CASHIER per hour is",emp_A_wage, "pkr")
    emp_B_wage = emp_B_wage_rate
    print("The wage of CAKE BAKER per hour is",emp_B_wage , "pkr")
    emp_C_wage = emp_C_wage_rate
    print("The wage of BREAD BAKER per hour is", emp_C_wage , "pkr")
    emp_D_wage = emp_D_wage_rate
    print("the wage of PASTRY CHEF per hour is", emp_D_wage , "pkr")
    return  ""

def working_hours():
    print(":::::::::::::::::::::::::::::::::::")
    print("EMPLOYEESS WORKING HOURS AND BONUS ")
    print(":::::::::::::::::::::::::::::::::::")
    print()
    emp_A_hours = int(input("Enter No. of hours of Working of HEAD CASHIER (PER DAY) : "))
    emp_B_hours = int(input("Enter No. of hours of Working of CAKE BAKER (PER DAY) : "))
    emp_C_hours = int(input("Enter No. of hours of Working of BREAD BAKER (PER DAY) : "))
    emp_D_hours = int(input("Enter No. of hours of Working of PASTRY CHEF (PER DAY) : "))
    print()

    print("1. Total wage for a Week")
    print("2. Total wage for a month")

    while True :
        wage = int(input("Choose an option 1 OR 2 : "))
        if total_sale < target_sale :
            if (wage == 1) or (wage == 2) :

                if wage == 1 :
                    print()
                    hours_wage_A = (int(7)*((int(emp_A_hours) * (int(emp_A_wage_rate)))))
                    print("Weekly wage of HEAD CASHIER is",hours_wage_A, "pkr")

                    hours_wage_B = (int(7)*(int(emp_B_hours) * int(emp_B_wage_rate)))
                    print("Weekly wage of CAKE BAKER is", hours_wage_B, "pkr")

                    hours_wage_C = (int(7) * ((int(emp_C_hours) * (int(emp_C_wage_rate)))))
                    print("Weekly wage of BREAD BAKER is", hours_wage_C, "pkr")

                    hours_wage_D = (int(7) * (int(emp_D_hours) * int(emp_D_wage_rate)))
                    print("Weekly wage of PASTRY CHEF is", hours_wage_D, "pkr")

                    break

                elif wage==2 :
                    print()

                    hours_wage_A = (int(30) * ((int(emp_A_hours) * (int(emp_A_wage_rate)))))
                    print("Weekly wage of HEAD CASHIER is", hours_wage_A, "pkr")

                    hours_wage_B = (int(30) * (int(emp_B_hours) * int(emp_B_wage_rate)))
                    print("Weekly wage of CAKE BAKER is", hours_wage_B, "pkr")

                    hours_wage_C = (int(30) * ((int(emp_C_hours) * (int(emp_C_wage_rate)))))
                    print("Weekly wage of BREAD BAKER is", hours_wage_C, "pkr")

                    hours_wage_D = (int(30) * (int(emp_D_hours) * int(emp_D_wage_rate)))
                    print("Weekly wage of PASTRY CHEF is", hours_wage_D, "pkr")

                    break

            else:
                print()
                print("INVALID KEY. Please Enter 1 OR 2")

    # For BONUS
        if total_sale > target_sale :
            if (wage == 1) or (wage == 2):

                if wage == 1:
                    print()
                    hours_wage_A = (int(7) * ((int(emp_A_hours) * (int(emp_A_wage_rate)))))+ (int(bonus))
                    print("Weekly wage of HEAD CASHIER is", hours_wage_A, "pkr. Including", bonus , "as BONUS")

                    hours_wage_B = (int(7) * (int(emp_B_hours) * int(emp_B_wage_rate)))+(int(bonus))
                    print("Weekly wage of CAKE BAKER is", hours_wage_B, "pkr. Including", bonus , "as BONUS")

                    hours_wage_C = (int(7) * ((int(emp_C_hours) * (int(emp_C_wage_rate))))) + (int(bonus))
                    print("Weekly wage of BREAD BAKER is", hours_wage_C, "pkr. Including", bonus, "as BONUS")

                    hours_wage_D = (int(7) * (int(emp_D_hours) * int(emp_D_wage_rate))) + (int(bonus))
                    print("Weekly wage of PASTRY CHEF is", hours_wage_D, "pkr. Including", bonus, "as BONUS")

                    break

                elif wage == 2:
                    print()

                    hours_wage_A = (int(30) * ((int(emp_A_hours) * (int(emp_A_wage_rate)))))+(int(bonus)*3)
                    print("Weekly wage of HEAD CASHIER is", hours_wage_A, "pkr. Including", bonus*int(3), "as BONUS")

                    hours_wage_B = (int(30) * (int(emp_B_hours) * int(emp_B_wage_rate)))+(int(bonus)*3)
                    print("Weekly wage of CAKE BAKER is", hours_wage_B, "pkr. Including", bonus*int(3), "as BONUS")

                    hours_wage_C = (int(30) * ((int(emp_C_hours) * (int(emp_C_wage_rate))))) + (int(bonus) * 3)
                    print("Weekly wage of BREAD BAKER is", hours_wage_C, "pkr. Including", bonus * int(3), "as BONUS")

                    hours_wage_D = (int(30) * (int(emp_D_hours) * int(emp_D_wage_rate))) + (int(bonus) * 3)
                    print("Weekly wage of PASTRY CHEF is", hours_wage_D, "pkr. Including", bonus * int(3), "as BONUS")

                    break

            else:
                print()
                print("INVALID KEY. Please Enter 1 OR 2")
    #print(int(total_stock) - (int(samosa_in_stock) + int(rolls_in_stock)))
    return ""

def add_items_to_boutique():
    global Tshirts_in_stock , Jeans_in_stock
    global cotton_suit_in_stock , lawn_suit_in_stock
    print("::::::::::::::::::::::")
    print("ADDING BOUTIQUE ITEMS")
    print("::::::::::::::::::::::")
    print()

    Tshirts_in_stock = Tshirts_in_stock + int(input("Enter Number of T-Shirts you want to add ? "))
    Jeans_in_stock = Jeans_in_stock + int(input("Enter Number of Jeans you want to add ?  "))
    cotton_suit_in_stock = cotton_suit_in_stock + int(input("Enter Number Of Cotton suits you want to add ? "))
    lawn_suit_in_stock = lawn_suit_in_stock + int(input("Enter Number of Lawn Suits you want to add ?  "))

    return ""

def remaining_items_in_boutique():
    global Tshirts_in_stock , Jeans_in_stock , cotton_suit_in_stock , lawn_suit_in_stock
    global total_Tshirts_sale , total_Jeans_sale
    print("::::::::::::::::::::::::::")
    print("REMAINING BOUTIQUE ITEMS")
    print("::::::::::::::::::::::::::")
    print()
    print("The remaining stock of T-shirts left :",Tshirts_in_stock)
    print("The remaining stock of Jeans left :",Jeans_in_stock)
    print("The remaining stock of Cotton suits left :", cotton_suit_in_stock)
    print("The remaining stock of lawn suits left :", lawn_suit_in_stock)
    return ""

def boutiquePurchasing():
    global  Tshirts_in_stock , Jeans_in_stock , cotton_suit_in_stock , lawn_suit_in_stock
    global total_Tshirts_sale , total_Jeans_sale , total_cotton_suits_sale , total_lawn_suits_sale
    print(":::::::::::::::::::::::::::")
    print("WELCOME TO ARBII.XD BOUTIQUE \U0001f600 ")
    print(":::::::::::::::::::::::::::")
    print()
    print("T-shirt unit price : 700 \n Jeans unit price : 1000 \n Cotton Suits unit price : 1200 \n Lawn Suits unit price : 1200")
    print()
    print("Press 1. if you want you purchase T-shirts. \n Press 2. if you want to purchase Jeans. \n Press 3. if you want to purchase Cotton Suits. \n Press 4. if you want to purchase Lawn Suits.")
    print()
    q = int(input("ENTER YOUR CHOICE 1 TO 4 : "))
    while True :
        if 2 > 0 :

            if (q == 1) or (q==2) or (q == 3) or (q == 4) :
                if q==1 :
                    if Tshirts_in_stock >= 1:
                        quantity = int(input("Enter Quantity T-SHIRTS you want : "))
                        print()
                        if Tshirts_in_stock >= quantity:

                            print("THANKS FOR YOUR ORDER SIR..\nYou just bought", quantity,
                                "T-Shirts and your bill generates as :",
                                Tshirt_unit_price * quantity, "rupeees")

                            Tshirts_sale = Tshirt_unit_price * quantity
                            total_Tshirts_sale = total_Tshirts_sale + Tshirts_sale
                            #print(total_Tshirts_sale)
                            print()

                            print()
                            Tshirts_in_stock = Tshirts_in_stock - quantity
                            # print("Now the remaining Tshirts in our stock are :", Tshirts_in_stock)
                            if Tshirts_in_stock <= 0:
                                return "Now T_Shirts are OUT OF STOCK"
                            print()

                        else:
                            print("Actually we have remaining ", Tshirts_in_stock,
                                "T-Shirts in our stock. We are running out of out stock")

                    else:
                        print("!!.. T-Shirts are OUT OF STOCK ..!!")
                        break

                if q == 2 :
                    if Jeans_in_stock >= 1:
                        quantity = int(input("Enter Quantity of JEANS you want : "))
                        print()
                        if Jeans_in_stock >= quantity:

                            print("THANKS FOR YOUR ORDER SIR..\nYou just bought", quantity,
                                "Jeans and your bill generates as :",
                                Jeans_unit_price * quantity, "rupeees")

                            Jeans_sale = Jeans_unit_price * quantity
                            total_Jeans_sale = total_Jeans_sale + Jeans_sale
                            # print(total_Jeans_sale)
                            print()

                            print()
                            Jeans_in_stock = Jeans_in_stock - quantity
                            # print("Now the remaining Jeans in our stock are :", Jeans_in_stock)
                            if Jeans_in_stock <= 0:
                                return "Now Jeans are OUT OF STOCK"
                            print()

                        else:
                            print("Actually we have remaining ", Jeans_in_stock,
                                "Jeans in our stock. We are running out of out stock")

                    else:
                        print("!!.. Jeans are OUT OF STOCK ..!!")
                        break

                if q == 3 :
                    if cotton_suit_in_stock >= 1:
                        quantity = int(input("Enter Quantity of COTTON SUITS you want : "))
                        print()
                        if cotton_suit_in_stock >= quantity:

                            print("THANKS FOR YOUR ORDER SIR..\nYou just bought", quantity,
                                "Cotton Suits and your bill generates as :",
                                cotton_suit_unit_price * quantity, "rupeees")

                            cotton_suits_sale = cotton_suit_unit_price * quantity
                            total_cotton_suits_sale = total_cotton_suits_sale + cotton_suits_sale
                            # print(total_cotton_suits_sale)
                            print()

                            print()
                            cotton_suit_in_stock = cotton_suit_in_stock - quantity
                            # print("Now the remaining cotton_suits in our stock are :", cotton_suits_in_stock)
                            if cotton_suit_in_stock <= 0:
                                return "Now Cotton_Suits are OUT OF STOCK"
                            print()

                        else:
                            print("Actually we have remaining ", cotton_suit_in_stock,
                                "cotton_suits in our stock. We are running out of out stock")

                    else:
                        print("!!.. cotton_suits are OUT OF STOCK ..!!")
                        break

                if q == 4 :
                    if lawn_suit_in_stock >= 1:
                        quantity = int(input("Enter Quantity of LAWN SUITS you want : "))
                        print()
                        if lawn_suit_in_stock >= quantity:

                            print("THANKS FOR YOUR ORDER SIR..\nYou just bought", quantity,
                                "Lawn Suits and your bill generates as :",
                                lawn_suit_unit_price * quantity, "rupeees")

                            lawn_suits_sale = lawn_suit_unit_price * quantity
                            total_lawn_suits_sale = total_lawn_suits_sale + lawn_suits_sale
                            # print(total_lawn_suits_sale)
                            print()

                            print()
                            lawn_suit_in_stock = lawn_suit_in_stock - quantity
                            # print("Now the remaining lawn_suits in our stock are :", lawn_suits_in_stock)
                            if lawn_suit_in_stock <= 0:
                                return "Now lawn_Suits are OUT OF STOCK"
                            print()

                        else:
                            print("Actually we have remaining ", lawn_suit_in_stock,
                                  "Lawn_suits in our stock. We are running out of out stock")

                    else:
                        print("!!.. Lawn_suits are OUT OF STOCK ..!!")
                        break

            else:
                print()
                print("INVALID KEY. Please press 1 TO 4")
                q = int(input("Enter your choice again : "))
                print()
                continue

        return ""


def BoutiqueSale():
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("THANK YOU SO MUCH FOR VISITING OUR BOUTIQUE AND PURCHASING OUR BOUTIQUE ITEMS \U0001f600 \n "
          "On purchasing items more than (10000 pkr), we have something more to give you \U0001f600")
    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print()
    global total_boutique_sale , total_lawn_suits_sale , total_cotton_suits_sale ,  total_Jeans_sale , total_Tshirts_sale
    global total_sale , samosa_in_stock , rolls_in_stock

    total_boutique_sale = int(total_Tshirts_sale) + int(total_Jeans_sale) + int(total_cotton_suits_sale) + int(
        total_lawn_suits_sale)
    #print(total_boutique_sale)

    print("Up till now you've purchased Boutique items of", total_boutique_sale , "pkr")
    print()
    print("You've purchased", int(int(total_Tshirts_sale)/700), "T-Shirts of", total_Tshirts_sale, "pkr")
    print("you've purchased", int(int(total_Jeans_sale)/1000),"Jeans of", total_Jeans_sale,"pkr")
    print("you've purchased", int(int(total_cotton_suits_sale)/1200),"Cotton-Suits of" ,total_cotton_suits_sale, "pkr")
    print("you've purchased",int(int(total_lawn_suits_sale)/1200),"Lawn-Suits of" ,total_lawn_suits_sale, "pkr")

    if total_boutique_sale > target_sale_boutique :
        if total_boutique_sale < 15000 :
            print()
            print("Yayy !! you got a GIFT \U0001f600")
            print("You have just crossed our (10000 pkr) purchasing mark so it is our policy to give you 1 dozen of SAMOSAS as a gift so , ENJOY \U0001f600")

            (samosa_in_stock) = int(samosa_in_stock) - int(12)
            #print(samosa_in_stock)
            print()
        elif total_boutique_sale > 15000 :
            print()
            print("Yayyy you got a GIFT \U0001f600")
            print("You have just crossed our (15000 pkr) purchasing mark so it is our policy to give you 1 dozen of ROLLS as a gift so , ENJOY \U0001f600 ")

            (rolls_in_stock) = int(rolls_in_stock) - int(12)
            #print(rolls_in_stock)
            print()
    elif total_boutique_sale <10000 :
        print()
        print("SORRY NO GIFT :(")
        print("Unfortunately your purchasing is less than (10000 pkr) so, there is no such GIFT for you \U0001F923")



    return ""

while True :
    print()
    print("                                                                                    1. Add Bakery Items to stock")
    print("                                                                                    2. Remaining Bakery Stock")
    print("                                                                                    3. Place Order for BAKERY ITEMS")
    print("                                                                                    4. Total BAKERY Sale uptil Now ")
    print("                                                                                    5. See EMPLOYEES wage rates")
    print("                                                                                    6. Employees working hours and BONUS")
    print("                                                                                    7. Add Items To BOUTIQUE")
    print("                                                                                    8. Cheak BOUTIQUE STOCK")
    print("                                                                                    9. Visit Our BOUTIQUE ")
    print("                                                                                    10. Total BOUTIQUE Sale uptil now and GIFT")
    print("                                                                                    11. Exit")
    print()

    d = int(input("                                                                                   Ënter your choice From 1 to 11 :  "))

    if d==1 :
        print(add_items_to_stock())

    if d == 2 :
        print(remaining_items())

    if d==3 :
        print(take_order())

    if d==4 :
        print(total_sale_till_now())

    if d==5 :
        print(emp_wage_rates())

    if d== 6:
        print(working_hours())


    if d == 7 :
        print(add_items_to_boutique())

    if d == 8:
        print(remaining_items_in_boutique())

    if d == 9 :
        print(boutiquePurchasing())

    if d==10 :
        print(BoutiqueSale())

    if d == 11 :
        print("Good Bye \U0001f600")
        os._exit(11)
