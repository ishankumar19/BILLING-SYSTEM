import datetime as dt

# Greeting based on time
print("Welcome to BIHAR JUICE AND SHAKE")
hour = dt.datetime.now().hour
if 6 < hour < 12:
    print("Good Morning, what would you like to order?")
elif 12 <= hour < 18:
    print("Good Afternoon, what would you like to order?")
else:
    print("Good Evening, what would you like to order?")

# Menu
menu = {
    'd1': ('Chocolate milk shake', 65),
    'd2': ('Mojito', 75),
    'd3': ('Oreo X KitKat shake', 90),
    'd4': ('Blue Lagoon', 85),
    'd5': ('Strawberry smash', 70),
    'd6': ('Banana Shake', 30),
    'd7': ('Mango Shake', 35),
    'd8': ('Mix fruit tongue twister', 50)
}

print('''
------------------------------------------------------------------
                        DRINK AND SHAKES 
------------------------------------------------------------------
Sno.        CODE               DRINKS                    PRICE          
1.           d1             Chocolate milk shake          ₹65
2.           d2             Mojito                        ₹75
3.           d3             Oreo X KitKat shake           ₹90
4.           d4             Blue Lagoon                   ₹85
5.           d5             Strawberry smash              ₹70
6.           d6             Banana Shake                  ₹30
7.           d7             Mango Shake                   ₹35
8.           d8             Mix fruit tongue twister      ₹50
------------------------------------------------------------------
''')

bill = 0
while True:
    ch = input("Do you want to order drinks/shakes? (y/n): ").lower()
    if ch != 'y':
        break
    code = input("Enter Drink Code: ").lower()
    if code in menu:
        drink, price = menu[code]
        print(f"You have ordered {drink}")
        try:
            qty = int(input("Enter Quantity: "))
            bill += price * qty
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    else:
        print("Invalid code. Please try again.")

# Final billing
print("------------------------------------------------------------")
nm = input("Enter your name: ")
mb = input("Enter your mobile number: ")
add = input("Enter your address: ")
print("===========================================================")
print("********************* INOVANCE ****************************")
print("===========================================================")
print(f"Name: {nm}   Mobile No: {mb}")
print(f"Address: {add}")
print("-----------------------------------------")
print(f"T O T A L   A M O U N T: ₹{bill:.2f}")
print("-----------------------------------------")
print("THANK YOU FOR ORDERING. PLEASE VISIT AGAIN!")